"""压线（online）/ 变道（lanechange）行为筛选。

判定逻辑对齐 prompts/online_prompt.md 与 prompts/lanechange_prompt.md：
- 压线 = 车道线处于车体正下方：线在车体纵向窗口 x∈[-rear, front] 内的带符号
  横向偏移 |d| <= 车体半宽（d 为 ego 系 y，左正右负；对与窗口相交的线段做
  线性插值求 d，车道线顶点稀疏，只看顶点会大面积漏帧）。
- 每帧 d 用当前帧自身标注的 ego 系点直接计算（标注按每帧 ±50m 视野截断，
  回投存量全局几何会丢数据，00051 双黄线穿越即因此漏检）；全局几何仅用于
  物理线合并（端点匹配 + 接缝方向一致，分叉时取方向最一致候选）。
- 压线时段（online）：同一物理线连续压线 >= 2 帧（一蹭即离不算）；非排除帧的
  单帧数据空洞按两侧线性插值桥接（两侧异号记 0，即穿越发生在洞内）。方向取时段内
  过中心帧之外的多数符号（LEFT/RIGHT），平票取最后一个有效帧符号，全为 0 记 BOTH
  （BOTH 的严格含义"同时骑跨左右两线"由两个独立事件分别表达）；起止时间按实际
  timestamp 差（纳秒）计算（容许段内缺帧）。
- 完整变道（lanechange，两种完成情形）：
  A. 可见穿越：压线时段前 d>+half、后 d<-half（或反向）；before/after 允许
     最多 2 帧数据空洞（向前/后找最近非 None d，但**不跨路口/斑马线排除帧借 d**）。
  B. 截断穿越：线穿越车轴后不再压线（碎片结束、跨路口未拼接等）——要求进入侧
     |before|>half、时段末 d 已过中心、其后不再压线、非视频末尾，且【车道占有】：
     自车参考段（取时段末+2 帧处，容忍入道滑行）与回溯到的起始参考段不同且无
     纵向前后继关系。
  每段只取时间上第一个完整变道。
- 路口/人行横道排除：① ic 段的线不参与；② 自车参考段在 ic 段内（多边形在
  ego 系直接判定，左右线重采样等长后闭合防自交）或车体与 pedestrian_crossing
  相交的帧，整帧不算压线/变道并打断时段。
"""
import argparse
import csv
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import cv2
import numpy as np
from shapely.geometry import Point, Polygon

import openlanev2.lanesegment.visualization.bev as ls_bev
from openlanev2.lanesegment.visualization import assign_attribute, draw_annotation_bev

from render_bev_video import PACIFICA, draw_ego_vehicle

LINETYPE_NAME = {0: "NONE", 1: "SOLID", 2: "DASH"}
FRAME_DT = 0.5  # 标称 2Hz（仅用于时段末尾 +0.5s 的结束偏移）
REAR, FRONT, EGO_WIDTH = PACIFICA
HALF = EGO_WIDTH / 2
EGO_CENTER_X = (FRONT - REAR) / 2  # 自车几何中心在 ego 系的 x


def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter OpenLane-V2 frames with online / lanechange behavior")
    parser.add_argument("--root", default=str(REPO_ROOT / "data/OpenLane-V2"))
    parser.add_argument("--data-dict", default="data_dict_subset_A.json")
    parser.add_argument("--splits", nargs="*", default=["train", "val"])
    parser.add_argument("--out-dir", default=str(Path(__file__).resolve().parent / "out"))
    parser.add_argument("--sample-vis", type=int, default=4, help="每类行为抽样渲染帧数")
    parser.add_argument("--limit-segments", type=int, default=0, help="调试用:每 split 只处理前 N 段")
    return parser.parse_args()


def ego_to_global(pts_xy, translation, rotation):
    return pts_xy @ rotation.T + translation


def ego_footprint_local():
    """自车矩形（ego 系常量）。"""
    return Polygon([(-REAR, -HALF), (-REAR, HALF), (FRONT, HALF), (FRONT, -HALF)])


def load_frame(info_dir, timestamp):
    with open(info_dir / f"{timestamp}-ls.json", "r") as f:
        return json.load(f)


def frame_pose(frame):
    t = np.array(frame["pose"]["translation"], dtype=np.float64)[:2]
    R = np.array(frame["pose"]["rotation"], dtype=np.float64)[:2, :2]
    return t, R


def signed_lateral(pts, rear=REAR, front=FRONT):
    """车道线（折线）相对车体纵轴（ego y=0）在纵向窗口 x∈[-rear, front] 内的
    带符号最近距离。左正右负；线在窗口内穿过纵轴则 0；线完全在窗口外则 None。
    对与窗口相交的线段做线性插值（顶点稀疏，只看顶点会大面积漏帧）。
    """
    e = np.asarray(pts, dtype=np.float64)[:, :2]
    if len(e) < 2:
        return None
    x0, x1 = -rear, front
    ys = []
    for (ax, ay), (bx, by) in zip(e[:-1], e[1:]):
        if ax == bx:
            if not (x0 <= ax <= x1):
                continue
            seg_ys = [ay, by]
        else:
            ta = (x0 - ax) / (bx - ax)
            tb = (x1 - ax) / (bx - ax)
            lo, hi = sorted((ta, tb))
            lo, hi = max(lo, 0.0), min(hi, 1.0)
            if lo > hi:
                continue
            seg_ys = [ay + (by - ay) * lo, ay + (by - ay) * hi]
        if (seg_ys[0] <= 0 <= seg_ys[1]) or (seg_ys[1] <= 0 <= seg_ys[0]):
            return 0.0
        ys.extend(seg_ys)
    if not ys:
        return None
    return float(min(ys, key=abs))


def resample_n(pts, n):
    """折线按弧长重采样到 n 点（左右线等长后闭合多边形才不自交）。"""
    p = np.asarray(pts, dtype=np.float64)[:, :2]
    if len(p) < 2:
        return p
    d = np.linalg.norm(np.diff(p, axis=0), axis=1)
    cum = np.concatenate([[0.0], np.cumsum(d)])
    if cum[-1] <= 0:
        return np.repeat(p[:1], n, axis=0)
    t = np.linspace(0.0, cum[-1], n)
    return np.stack([np.interp(t, cum, p[:, 0]), np.interp(t, cum, p[:, 1])], axis=1)


def reference_segment(segments, center_pt):
    """自车中心（ego 系常量点）落在哪个车道段多边形内（全程 ego 系，不做全局变换）。
    返回 (id, is_intersection_or_connector)。"""
    best_id, best_area, best_ic = None, -1.0, False
    for seg in segments:
        left = resample_n(seg["left_laneline"], 20)
        right = resample_n(seg["right_laneline"], 20)
        if len(left) < 2 or len(right) < 2:
            continue
        poly = Polygon(np.concatenate([left, right[::-1]]))
        if not poly.is_valid:
            poly = poly.buffer(0)
        if poly.covers(center_pt) and poly.area > best_area:
            best_id, best_area = seg["id"], poly.area
            best_ic = bool(seg.get("is_intersection_or_connector", False))
    return best_id, best_ic


def in_crosswalk(footprint_ego, areas):
    """自车矩形与任何 pedestrian_crossing（category=1，ego 系）相交。"""
    for area in areas:
        if area.get("category", 0) != 1:
            continue
        pts = np.array(area["points"], dtype=np.float64)[:, :2]
        if len(pts) < 3:
            continue
        poly = Polygon(pts)
        if not poly.is_valid:
            poly = poly.buffer(0)
        if footprint_ego.intersects(poly):
            return True
    return False


def merge_pieces(pieces, tol=0.3):
    """把 (seg_id, side)->(全局折线, linetype) 的碎片按端点匹配拼成物理线。

    同一条物理边线常被切成多块（相邻段接缝、A.right==B.left 共享边界）。
    拼接要求接缝处行进方向一致（夹角<60°），避免路口节点误接垂直线；
    分叉处多个候选同时满足端点匹配时，取方向最一致（余弦最大）者。
    """
    unused = {k: [v[0], v[1]] for k, v in pieces.items()}
    chains = []

    def near(a, b):
        return abs(a[0] - b[0]) < tol and abs(a[1] - b[1]) < tol

    def fwd(p, i, step):
        j = i + step
        if j < 0 or j >= len(p):
            j = i - step
        return p[j] - p[i]

    def cos_dir(v1, v2):
        n1, n2 = np.linalg.norm(v1), np.linalg.norm(v2)
        if n1 == 0 or n2 == 0:
            return 1.0
        return float(np.dot(v1, v2) / (n1 * n2))

    while unused:
        key = next(iter(unused))
        pts, lt = unused.pop(key)
        members = {key}
        changed = True
        while changed:
            changed = False
            best = None  # (cos, k2, mode)
            for k2, (p2, _lt2) in unused.items():
                cands = []
                if near(pts[-1], p2[0]):
                    cands.append((cos_dir(fwd(pts, len(pts) - 1, -1), fwd(p2, 0, 1)), 0))
                if near(pts[-1], p2[-1]):
                    cands.append((cos_dir(fwd(pts, len(pts) - 1, -1), fwd(p2, len(p2) - 1, -1)), 1))
                if near(pts[0], p2[-1]):
                    cands.append((cos_dir(fwd(p2, len(p2) - 1, -1), fwd(pts, 0, 1)), 2))
                if near(pts[0], p2[0]):
                    cands.append((cos_dir(fwd(p2, 0, 1), fwd(pts, 0, 1)), 3))
                for c, mode in cands:
                    if c > 0.5 and (best is None or c > best[0]):
                        best = (c, k2, mode)
            if best:
                _, k2, mode = best
                p2 = unused.pop(k2)[0]
                members.add(k2)
                if mode == 0:
                    pts = np.vstack([pts, p2[1:]])
                elif mode == 1:
                    pts = np.vstack([pts, p2[::-1][1:]])
                elif mode == 2:
                    pts = np.vstack([p2[:-1], pts])
                else:
                    pts = np.vstack([p2[::-1][:-1], pts])
                changed = True
        chains.append((key, pts, lt, members))
    return chains


def longitudinal_pairs(segments, topology_lsls):
    """topology_lsls[i][j]==1 的 (id_i, id_j) 纵向前后继集合。"""
    topo = np.array(topology_lsls, dtype=np.int8)
    ids = [s["id"] for s in segments]
    pairs = set()
    rows, cols = np.nonzero(topo)
    for i, j in zip(rows, cols):
        if i != j:
            pairs.add((ids[i], ids[j]))
    return pairs


def scan_segment(root, split, segment, timestamps):
    """逐帧收集 d（当前帧 ego 点直算）与全局线碎片；合并物理线。
    返回 (frames, series)：frames[i]=(ts, excluded, ref_id, pairs)；
    series[物理线label]=[(frame_idx, d|None, linetype), ...]（每帧都有条目）。"""
    info_dir = Path(root) / split / segment / "info"
    half = HALF
    frames = []
    per_frame_d = []
    pieces = {}
    footprint_ego = ego_footprint_local()
    center_ego = Point(EGO_CENTER_X, 0.0)
    for ts in sorted(timestamps, key=lambda x: int(x.split(".")[0])):
        ts = ts.split(".")[0]
        excluded = True
        ref_id = None
        pairs = set()
        dmap = {}
        frame = load_frame(info_dir, ts)
        if "annotation" in frame and frame["annotation"]:
            annotation = frame["annotation"]
            segments = annotation["lane_segment"]
            t, R = frame_pose(frame)
            ref_id, ref_in_ic = reference_segment(segments, center_ego)
            excluded = ref_in_ic or in_crosswalk(
                footprint_ego, annotation.get("area", []))
            if not excluded:
                pairs = longitudinal_pairs(segments, annotation["topology_lsls"])
            for seg in segments:
                if seg.get("is_intersection_or_connector", False):
                    continue
                for side in ("left", "right"):
                    key = (seg["id"], side)
                    pts = np.array(seg[f"{side}_laneline"],
                                   dtype=np.float64)[:, :2]
                    if len(pts) >= 2 and key not in pieces:
                        pieces[key] = (ego_to_global(pts, t, R),
                                       seg[f"{side}_laneline_type"])
                    if excluded:
                        continue
                    d = signed_lateral(pts)
                    if d is not None:
                        dmap[key] = (d, seg[f"{side}_laneline_type"])
        frames.append((ts, excluded, ref_id, pairs))
        per_frame_d.append(dmap)

    series = {}
    for label, _pts, _lt, members in merge_pieces(pieces):
        seq = []
        for idx in range(len(frames)):
            exc = bool(frames[idx][1])
            best = None
            if not exc:
                for k in members:
                    if k in per_frame_d[idx]:
                        d, lt = per_frame_d[idx][k]
                        if best is None or abs(d) < abs(best[0]):
                            best = (d, lt)
            seq.append((idx, best[0] if best else None,
                        best[1] if best else None, exc))
        series[label] = _bridge_gaps(seq, half)
    return frames, series


def _bridge_gaps(seq, half):
    """桥接**非排除帧**的单帧数据空洞：两侧都压线而中间一帧该线恰好没有数据
    （顶点稀疏/截断边缘）时，按两侧 d 线性插值补上（两侧异号则记 0，即穿越）。
    排除帧（路口/斑马线）不桥接——那是真实的时段打断。"""
    out = [list(e) for e in seq]
    for i in range(1, len(out) - 1):
        if out[i][1] is not None or out[i][3]:
            continue
        _p, pd, plt, pexc = out[i - 1]
        _n, nd, nlt, nexc = out[i + 1]
        if pexc or nexc or pd is None or nd is None:
            continue
        if abs(pd) > half or abs(nd) > half:
            continue
        d = 0.0 if pd * nd < 0 else (pd + nd) / 2.0
        out[i][1] = d
        out[i][2] = plt if plt is not None else nlt
    return [tuple(e) for e in out]


def _nearest_d(seq, pos, step, max_gap):
    """从 pos 起沿 step 方向在 max_gap 帧内找最近非 None 的 d（容忍数据空洞）。
    遇到排除帧（路口/斑马线）立即停止——不得跨路口借 d 拼"完整穿越"。"""
    for k in range(max_gap + 1):
        i = pos + step * k
        if i < 0 or i >= len(seq):
            return None
        _idx, d, _lt, exc = seq[i]
        if exc:
            return None
        if d is not None:
            return d
    return None


def _event_times(frames, start_idx, end_idx):
    # OpenLane-V2 timestamp 单位为纳秒（相邻帧差 5e8 = 0.5s）
    t0 = int(frames[0][0])
    return (round((int(frames[start_idx][0]) - t0) / 1e9, 1),
            round((int(frames[end_idx][0]) - t0) / 1e9 + FRAME_DT, 1))


def merge_events(events):
    """相邻碎片链对同一次物理压线重复计事件时，合并方向与线型相同且帧区间
    重叠/相接的事件。"""
    merged = []
    for e in sorted(events, key=lambda x: (x["start_idx"], x["end_idx"])):
        if merged and e["direction"] == merged[-1]["direction"] \
                and e["line_type"] == merged[-1]["line_type"] \
                and e["start_idx"] <= merged[-1]["end_idx"] + 1:
            prev = merged[-1]
            prev["end_idx"] = max(prev["end_idx"], e["end_idx"])
            prev["end_ts"] = e["end_ts"] if e["end_idx"] >= prev["end_idx"] else prev["end_ts"]
            prev["n_frames"] = max(prev["n_frames"], e["n_frames"],
                                   prev["end_idx"] - prev["start_idx"] + 1)
        else:
            merged.append(dict(e))
    return merged


def _mk_event(frames, run, seg_id, side, direction=None):
    start_idx, end_idx = run[0][0], run[-1][0]
    linetypes = {LINETYPE_NAME[lt] for _, _, lt in run if lt is not None}
    if direction is None:
        signs = [1 if d > 0 else -1 for _, d, _ in run if d is not None and abs(d) > 0.05]
        s = sum(signs)
        if not signs:
            direction = "BOTH"
        elif s > 0:
            direction = "LEFT"
        elif s < 0:
            direction = "RIGHT"
        else:
            # 平票（左右帧数相等）：取时段内最后一个有效帧的符号
            direction = "LEFT" if signs[-1] > 0 else "RIGHT"
    start_time_s, end_time_s = _event_times(frames, start_idx, end_idx)
    return {
        "seg_id": seg_id,
        "side": side,
        "line_type": "/".join(sorted(linetypes)),
        "direction": direction,
        "start_idx": start_idx,
        "end_idx": end_idx,
        "n_frames": len(run),
        "start_ts": frames[start_idx][0],
        "end_ts": frames[end_idx][0],
        "start_time_s": start_time_s,
        "end_time_s": end_time_s,
    }


def extract_online_events(frames, series, half=HALF):
    """连续 |d|<=half 且 >=2 帧 -> 压线时段（prompt: 仅一帧蹭线不算）。"""
    events = []
    for (seg_id, side), seq in series.items():
        run = []
        for idx, d, lt, _exc in seq:
            online = d is not None and abs(d) <= half
            if online:
                run.append((idx, d, lt))
            else:
                if len(run) >= 2:
                    events.append(_mk_event(frames, run, seg_id, side))
                run = []
        if len(run) >= 2:
            events.append(_mk_event(frames, run, seg_id, side))
    return merge_events(events)


def extract_lanechange_events(frames, series, half=HALF):
    """完整变道两种情形：
    A. 可见穿越：压线时段前 d>+half、后 d<-half（或反向）；before/after 各允许
       最多 2 帧数据空洞（取最近非 None d）。
    B. 截断穿越：线穿越车轴后不再压线（碎片结束、跨路口未拼接等）——要求进入侧
       |before|>half、时段末 d 已过中心（符号翻转>0.05m）、其后不再压线、非视频
       末尾，且【车道占有】：自车参考段变为另一段且与回溯到的起始参考段无直接
       纵向前后继关系。
    每段只取时间上第一个完整变道（prompt 规则）。"""
    events = []
    m_gap = 2
    for (seg_id, side), seq in series.items():
        m = len(seq)
        i = 0
        while i < m:
            idx, d, lt, _exc = seq[i]
            if d is None or abs(d) > half:
                i += 1
                continue
            j = i
            while j < m and seq[j][1] is not None and abs(seq[j][1]) <= half:
                j += 1
            run = [e[:3] for e in seq[i:j]]
            before = _nearest_d(seq, i - 1, -1, m_gap)
            after = _nearest_d(seq, j, +1, m_gap)
            last_d = run[-1][1]
            direction = None
            if before is not None and after is not None:
                if before > half and after < -half:
                    direction = "LEFT"
                elif before < -half and after > half:
                    direction = "RIGHT"
            elif after is None and j < m and _no_more_online(seq, j, half):
                if before is not None and before > half and last_d < -0.05 \
                        and _occupies_new_lane(frames, run[0][0], run[-1][0]):
                    direction = "LEFT"
                elif before is not None and before < -half and last_d > 0.05 \
                        and _occupies_new_lane(frames, run[0][0], run[-1][0]):
                    direction = "RIGHT"
            if direction:
                events.append(_mk_event(frames, run, seg_id, side, direction))
            i = j
    events = merge_events(events)
    events.sort(key=lambda e: e["start_idx"])
    return events[:1]


def _no_more_online(seq, j, half):
    """压线时段之后该线在剩余视频中不再处于压线状态（允许远距离重现与排除帧）。"""
    return all(d is None or abs(d) > half for _, d, _, _ in seq[j:])


def _occupies_new_lane(frames, start_idx, end_idx):
    """prompt 条件1【车道占有】。ref0 从 run 起点向前回溯最近非 None 参考段
    （车骑在边界上时参考段可能为 None）；ref1 从 min(end+2, 末帧) 起向后找首个
    非 None 参考段——穿越刚结束时车可能仍在旧段内滑行，直接取时段后第一帧会误拒。"""
    ref0, pairs0 = None, set()
    for k in range(start_idx, -1, -1):
        if frames[k][2] is not None:
            ref0, pairs0 = frames[k][2], frames[k][3]
            break
    ref1 = None
    for k in range(min(end_idx + 2, len(frames) - 1), len(frames)):
        if frames[k][2] is not None:
            ref1 = frames[k][2]
            break
    if ref0 is None or ref1 is None or ref0 == ref1:
        return False
    return (ref0, ref1) not in pairs0 and (ref1, ref0) not in pairs0


def render_flag_frame(root, split, segment, timestamp, out_png):
    frame = load_frame(Path(root) / split / segment / "info", timestamp)
    annotation = assign_attribute(frame["annotation"])
    ls_bev.THICKNESS = 2
    # 验证图开启 attribute 着色与 area 绘制，便于目检路口（人行横道）与灯色
    image = draw_annotation_bev(
        annotation,
        with_attribute=True,
        with_linetype=True,
        with_centerline=True,
        with_laneline=True,
        with_area=True,
    )
    draw_ego_vehicle(image)
    bgr = cv2.cvtColor(np.clip(image, 0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_png), bgr)


def write_outputs(out_dir, name, events_by_seg, frames_by_seg):
    """events csv + data_dict json（事件覆盖帧）。返回 json 路径。"""
    csv_path = out_dir / f"{name}_events.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["split", "segment", "seg_id", "side", "line_type",
                           "direction", "start_ts", "end_ts", "n_frames",
                           "start_time_s", "end_time_s"])
        writer.writeheader()
        for (split, segment), events in events_by_seg.items():
            for e in events:
                row = {"split": split, "segment": segment}
                row.update({k: v for k, v in e.items()
                            if k not in ("start_idx", "end_idx")})
                writer.writerow(row)

    data = {}
    for (split, segment), events in events_by_seg.items():
        ts_set = set()
        frames = frames_by_seg[(split, segment)]
        for e in events:
            for i in range(e["start_idx"], e["end_idx"] + 1):
                ts_set.add(frames[i][0])
        if ts_set:
            data.setdefault(split, {})[segment] = sorted(ts_set, key=int)
    json_path = out_dir / f"data_dict_subset_A_{name}.json"
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    n_events = sum(len(v) for v in events_by_seg.values())
    n_frames = sum(len(v) for s in data.values() for v in s.values())
    print(f"[{name}] 事件 {n_events}，覆盖帧 {n_frames}，段数 "
          f"{sum(len(v) for v in data.values())}")
    print(f"  CSV: {csv_path}")
    print(f"  data_dict: {json_path}")
    return json_path, events_by_seg


def main():
    args = parse_args()
    root = Path(args.root)
    with open(root / args.data_dict, "r") as f:
        data_dict = json.load(f)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    frames_by_seg = {}
    online_by_seg = {}
    change_by_seg = {}
    for split in args.splits:
        segments = sorted(data_dict.get(split, {}))
        if args.limit_segments:
            segments = segments[: args.limit_segments]
        for i, segment in enumerate(segments):
            timestamps = data_dict[split][segment]
            frames, series = scan_segment(root, split, segment, timestamps)
            if not frames:
                continue
            frames_by_seg[(split, segment)] = frames
            ov = extract_online_events(frames, series)
            lv = extract_lanechange_events(frames, series)
            if ov:
                online_by_seg[(split, segment)] = ov
            if lv:
                change_by_seg[(split, segment)] = lv
            print(f"[{i + 1}/{len(segments)}] {split}/{segment}: "
                  f"{len(frames)} frames, online={len(ov)}, lanechange={len(lv)}",
                  flush=True)

    write_outputs(out_dir, "online", online_by_seg, frames_by_seg)
    write_outputs(out_dir, "lanechange", change_by_seg, frames_by_seg)

    n = args.sample_vis
    for kind, ev_by_seg in (("online", online_by_seg), ("lanechange", change_by_seg)):
        shown = 0
        for (split, segment), events in ev_by_seg.items():
            for e in events:
                if shown >= n:
                    break
                png = out_dir / "vis" / (
                    f"{kind}_{split}_{segment}_{e['start_ts']}.png")
                render_flag_frame(root, split, segment, e["start_ts"], png)
                shown += 1
            if shown >= n:
                break
    print(f"抽样验证图: {out_dir / 'vis'}")


if __name__ == "__main__":
    main()

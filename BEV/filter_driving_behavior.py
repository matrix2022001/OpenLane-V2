"""压线（online）/ 变道（lanechange）行为筛选。

判定逻辑对齐 prompts/online_prompt.md 与 prompts/lanechange_prompt.md：
- 压线 = 车道线处于车体正下方：优先在几何中心 x=EGO_CENTER_X、其次后轴
  x=0 对折线插值求带符号横向距 d（左正右负）；两处都没有则回退短窗口
  x∈[-0.5, 2.0]。|d| <= 车体半宽即压线。不用整车 5.2m AABB，避免弯道误报。
- 每帧 d 用当前帧自身标注的 ego 系点直接计算（标注按每帧 ±50m 视野截断）；
  全局几何仅用于物理线合并与双线聚类。
- 物理线合并：同一 (seg_id, side) 保留弧长最长的一次观测，再按端点匹配
  + 接缝方向一致（夹角<60°）跨 key 拼接；零向量方向余弦为 0。跨侧
  （left<->right）拼接需重叠弧长 >=1m（共享边界可并，导流鼻节点收敛
  禁并，00096 假变道根因）。端点匹配失败的接缝（如 type-0 碎片全局几何
  退化）用 stitch_groups 兜底：共同/相邻帧 typed-priority d 差 <=0.25m
  且方向兼容（退化/闭合几何免检，否则 |cos|>=0.8）即并链。
- 时段物理连续性校验：进入/离开/内部相邻帧 d 跳变均 <= SERIES_JUMP_MAX 才
  成事件，防 Y 形链 min|d| 分支切换制造的单帧假穿越（00233 导流斜线根因）。
- 线型：OpenLane 0/1/2 映射为不记/SOLID/DASH；平行间距 0.03~0.5m 的一对边线
  聚成 DOUBLE_* / LEFT_SOLID_RIGHT_DASH / LEFT_DASH_RIGHT_SOLID；间距<0.03m 的
  重合记录（共享边界 A.right==B.left）是同一物理线，先并成单线；AV2 地图里
  双黄中心线只存一条被相邻两段共享的线，共享的 SOLID 线升为 DOUBLE_SOLID
  （共享 DASH 仍为单线）。area.category=2 路沿记 CURB（按车左右侧分键防 area
  id 冲突）。NONE（type-0）线不产生压线事件，但其 ego 系 d 作为影子证据参与
  穿越前后判定与链缝合。
- 压线时段（online）：同一物理线连续压线 >= 2 帧；非排除帧最多 2 帧空洞
  按两侧线性插值桥接（两侧异号记 0，桥接帧不参与方向计票）。方向（prompt
  第三步）= 压线开始前该线所在侧：进入前数帧内最近 |d|>0.05 有效帧符号
  -> 无进入前证据回退时段内有效帧多数符号 -> 平票取时段内最后一个有效帧
  -> 再回退时段 mean d 符号。时间重叠且分居车左右的两条事件合并为 BOTH，
  线型取左侧。
- 完整变道（lanechange，prompt 第三步【占有/越线深度 满足任一】）：
  A. 可见穿越（= 越线深度成立，无需占有）：压线时段前 d>+half、后
     d<-half（或反向）；before/after 取最多 4 帧内最近的带外（|d|>half）
     读数（不跨路口排除帧借 d）。视频开头即骑线（无带外进入读数）的时段
     不判变道——越线前半程不在观测内，导流鼻/分合流处此类漂移多为道路
     结构分岔而非换道（00233 守卫）。
  B. 截断穿越：线穿越车轴后不再压线——要求进入侧 |before|>half、时段末 d
     已过中心、其后不再压线、非视频末尾，且【车道占有】。
  输出全部完整变道，按时间顺序（prompt"多次变道"，对应 line_events 数组）。
  压线段同样需 >= 2 帧；区间重叠方向相反的对（道路分合流）双双剔除，
  同向重叠/相接（一次变道扫过线对的多条链）合并为一次。
- 事件去重：同一物理线（含 A.right/B.left 共享边界碎片：区间重叠且共同时段
  帧 |Δd|<=0.25m 视为同线）方向相同、区间重叠/相接的时段合并。
- 线型：时段内逐帧原始线型（非零）多数投票；双线组用组类型；链首 NONE 不再
  升格为 SOLID。
- 路口排除：① ic 段的线不参与；② 自车参考段（与车体相交面积最大者）为 ic
  的帧整帧不算并打断时段。人行横道单独相交不再整帧打断。topology_lsls
  每帧都算。占有（prompt 条件1，视频结束时判定）：ref0 从时段起点回溯至多
  10 帧；ref1 取视频末尾向前最近的有效非排除帧；新段相交面积占车体 >0.5；
  若仅为纵向后继但中心线横向偏移 >1.5m（匝道分流）仍算占有。
"""
import argparse
import csv
import json
import sys
import warnings
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import cv2
import numpy as np
from shapely.geometry import Polygon

import openlanev2.lanesegment.visualization.bev as ls_bev
from openlanev2.lanesegment.visualization import assign_attribute, draw_annotation_bev

import config as C
from render_bev_video import apply_bev_overrides, draw_ego_vehicle

# OpenLane 0/1/2 + 路沿自定义 3。事件输出只用 prompt 八类（无 WIDE_DASH 推断）。
LINETYPE_CODE = {0: None, 1: "SOLID", 2: "DASH", 3: "CURB"}
PROMPT_TYPES = {
    "SOLID", "DASH", "WIDE_DASH", "DOUBLE_SOLID", "DOUBLE_DASH",
    "LEFT_SOLID_RIGHT_DASH", "LEFT_DASH_RIGHT_SOLID", "CURB",
}
# 全部可调参数见 config.py；以下为兼容别名（单一来源 = config）
FRAME_DT = C.FRAME_DT
REAR, FRONT, EGO_WIDTH = C.PACIFICA
HALF = C.EGO_HALF
EGO_CENTER_X = C.EGO_CENTER_X
SHORT_X0, SHORT_X1 = C.SHORT_WINDOW_X
DOUBLE_SEP = C.DOUBLE_SEP
DOUBLE_MIN_SEP = C.DOUBLE_MIN_SEP
DOUBLE_COS = C.DOUBLE_COS
OCCUPY_FRAC = C.OCCUPY_FRAC
RAMP_LATERAL = C.RAMP_LATERAL
LINE_DUP_TOL = C.LINE_DUP_TOL
CENTER_EPS = C.CENTER_EPS
DEFAULT_SAMPLE_SEGMENTS = list(C.SAMPLE_SEGMENTS)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter OpenLane-V2 frames with online / lanechange behavior")
    parser.add_argument("--root", default=str(C.DATA_ROOT))
    parser.add_argument("--data-dict", default=C.DATA_DICT)
    parser.add_argument("--splits", nargs="*", default=list(C.SPLITS))
    parser.add_argument("--out-dir", default=str(C.OUT_DIR))
    parser.add_argument("--sample-vis", type=int, default=C.SAMPLE_VIS,
                        help="每类行为抽样渲染帧数")
    parser.add_argument(
        "--sample-segments",
        nargs="*",
        default=list(C.SAMPLE_SEGMENTS),
        help="抽样优先段（有事件则先画），不足再按顺序补齐",
    )
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


def _y_at_x(pts, x_sta):
    """折线与竖线 x=x_sta 的交点 y；交在纵轴上则 0；无交则 None。"""
    e = np.asarray(pts, dtype=np.float64)[:, :2]
    ys = []
    for (ax, ay), (bx, by) in zip(e[:-1], e[1:]):
        if ax == bx:
            if abs(ax - x_sta) > 1e-9:
                continue
            if (ay <= 0 <= by) or (by <= 0 <= ay):
                return 0.0
            ys.extend([ay, by])
            continue
        xmin, xmax = (ax, bx) if ax <= bx else (bx, ax)
        if x_sta < xmin - 1e-9 or x_sta > xmax + 1e-9:
            continue
        t = (x_sta - ax) / (bx - ax)
        if t < -1e-9 or t > 1.0 + 1e-9:
            continue
        y = ay + (by - ay) * t
        if abs(y) < 1e-9:
            return 0.0
        ys.append(y)
    if not ys:
        return None
    return float(min(ys, key=abs))


def _window_nearest_y(pts, x0, x1):
    """短窗口内与条带相交的最近 |y|；穿过纵轴则 0。"""
    e = np.asarray(pts, dtype=np.float64)[:, :2]
    if len(e) < 2:
        return None
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


def signed_lateral(pts):
    """车体正下方的带符号横向距（ego y，左正右负）。

    优先几何中心 x=EGO_CENTER_X，其次后轴 x=0；两处都无交点则回退
    短窗口 x∈[-0.5, 2.0]（不用整车纵向跨度，避免弯道边线斜切车头/车尾）。
    """
    e = np.asarray(pts, dtype=np.float64)
    if len(e) < 2:
        return None
    for x_sta in (EGO_CENTER_X, 0.0):
        d = _y_at_x(e, x_sta)
        if d is not None:
            return d
    return _window_nearest_y(e, SHORT_X0, SHORT_X1)


def _lt_name(lt):
    if lt is None:
        return None
    if isinstance(lt, str):
        return lt if lt in PROMPT_TYPES else None
    return LINETYPE_CODE.get(int(lt))


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


def _lane_polygon(seg):
    for side in ("left_laneline", "right_laneline"):
        p = np.asarray(seg[side], dtype=np.float64)
        if p.size and not np.isfinite(p).all():
            return None
    left = resample_n(seg["left_laneline"], C.LANE_POLY_SAMPLES)
    right = resample_n(seg["right_laneline"], C.LANE_POLY_SAMPLES)
    if len(left) < 2 or len(right) < 2:
        return None
    poly = Polygon(np.concatenate([left, right[::-1]]))
    if not poly.is_valid:
        poly = poly.buffer(0)
    return poly


def reference_segment(segments, footprint):
    """与车体相交面积最大的车道段。返回 (id, is_ic, overlap_frac, lane_y)。"""
    best_id, best_ov, best_ic = None, 0.0, False
    lane_y = {}
    ego_area = float(footprint.area) or 1.0
    for seg in segments:
        cl = np.asarray(seg["centerline"], dtype=np.float64)[:, :2]
        if len(cl) and np.isfinite(cl).all():
            lane_y[seg["id"]] = float(np.mean(cl[:, 1]))
        poly = _lane_polygon(seg)
        if poly is None or poly.is_empty:
            continue
        with warnings.catch_warnings():
            # GEOS 对个别自交/退化多边形报 invalid value，结果已被后续
            # nan!=nan 与 is_empty 检查吸收，仅需静音输出
            warnings.simplefilter("ignore", RuntimeWarning)
            inter = footprint.intersection(poly)
        ov = float(inter.area) if not inter.is_empty else 0.0
        if ov > best_ov:
            best_id, best_ov = seg["id"], ov
            best_ic = bool(seg.get("is_intersection_or_connector", False))
    return best_id, best_ic, best_ov / ego_area, lane_y


def _arc_len(pts):
    p = np.asarray(pts, dtype=np.float64)[:, :2]
    if len(p) < 2:
        return 0.0
    return float(np.sum(np.linalg.norm(np.diff(p, axis=0), axis=1)))


def _side_of(key):
    """laneline 键的侧（'left'/'right'）；curb 键返回 None（不受跨侧重叠守卫约束）。"""
    return None if key[0] == "curb" else key[1]


def _max_run_len(pts, mask):
    best, run = 0.0, []
    for p, m in zip(pts, mask):
        if m:
            run.append(p)
        else:
            if len(run) >= 3:
                best = max(best, float(np.sum(
                    np.linalg.norm(np.diff(run, axis=0), axis=1))))
            run = []
    if len(run) >= 3:
        best = max(best, float(np.sum(np.linalg.norm(np.diff(run, axis=0), axis=1))))
    return best


def _overlap_len(a, b, tol):
    """两折线的最大重叠弧长：a 中距 b<=tol 的最长连续段与 b 中对称段取大。"""
    ra, rb = resample_n(a, 25), resample_n(b, 25)
    if len(ra) < 3 or len(rb) < 3:
        return 0.0
    d = np.linalg.norm(ra[:, None, :] - rb[None, :, :], axis=2)
    return max(_max_run_len(ra, d.min(axis=1) <= tol),
               _max_run_len(rb, d.min(axis=0) <= tol))


def merge_pieces(pieces, tol=C.MERGE_ENDPOINT_TOL):
    """把 key->(全局折线, linetype) 的碎片按端点匹配拼成物理线。

    拼接要求接缝处行进方向一致（夹角<60°），避免路口节点误接垂直线；
    分叉处多个候选同时满足端点匹配时，取方向最一致（余弦最大）者。
    跨侧（left<->right）拼接额外要求重叠弧长 >= BOUNDARY_OVERLAP_MIN：
    共享边界（A.right==B.left）沿整段平行重叠可并；导流鼻处左右边界仅
    在节点收敛（重叠~0）是不同物理线，禁并（00096 误报根因）。
    """
    unused = {k: [np.asarray(v[0], dtype=np.float64), v[1]] for k, v in pieces.items()}
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
            return 0.0
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
                cands = [x for x in cands if x[0] > C.SEAM_COS]
                if not cands:
                    continue
                s1, s2 = _side_of(key), _side_of(k2)
                if s1 and s2 and s1 != s2 \
                        and _overlap_len(pts, p2, tol) < C.BOUNDARY_OVERLAP_MIN:
                    continue
                c, mode = min(cands, key=lambda x: -x[0])  # 同分取最先候选
                if best is None or c > best[0]:
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


def _chain_dir(pts):
    p = np.asarray(pts, dtype=np.float64)[:, :2]
    if len(p) < 2:
        return None
    v = p[-1] - p[0]
    n = np.linalg.norm(v)
    if n < 1e-6:
        return None
    return v / n


def _mean_nn_dist(a, b):
    a = np.asarray(a, dtype=np.float64)[:, :2]
    b = np.asarray(b, dtype=np.float64)[:, :2]
    if len(a) == 0 or len(b) == 0:
        return 1e9
    d = np.linalg.norm(a[:, None, :] - b[None, :, :], axis=2)
    return float(np.mean(np.min(d, axis=1)))


def _double_type(lt_left, lt_right):
    left = _lt_name(lt_left)
    right = _lt_name(lt_right)
    if left not in ("SOLID", "DASH") or right not in ("SOLID", "DASH"):
        return None
    if left == "SOLID" and right == "SOLID":
        return "DOUBLE_SOLID"
    if left == "DASH" and right == "DASH":
        return "DOUBLE_DASH"
    if left == "SOLID" and right == "DASH":
        return "LEFT_SOLID_RIGHT_DASH"
    return "LEFT_DASH_RIGHT_SOLID"


def _mean_d(members, per_frame_d):
    vals = []
    for dmap in per_frame_d:
        for k in members:
            if k in dmap:
                vals.append(dmap[k][0])
    return float(np.mean(vals)) if vals else 0.0


def _chain_raw_name(members, per_frame_d):
    """链的线型 = 各帧 member 原始非零线型的多数（链首类型不可靠）。"""
    names = []
    for dmap in per_frame_d:
        for k in members:
            if k in dmap:
                n = _lt_name(dmap[k][1])
                if n:
                    names.append(n)
    if not names:
        return None
    return Counter(names).most_common(1)[0][0]


def _shared_solid_keys(pieces):
    """与另一段边线重合（间距<DOUBLE_MIN_SEP、重叠弧长>=BOUNDARY_OVERLAP_MIN）
    且两侧原始线型都是 SOLID 的 key 集合。AV2 地图把双黄中心线存成相邻两段
    共享的同一条线，重合 SOLID 记录即“地图单线代表的双实线”。"""
    keys = list(pieces)
    out = set()
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            ka, kb = keys[i], keys[j]
            if ka[0] == kb[0]:
                continue
            if int(pieces[ka][1]) != 1 or int(pieces[kb][1]) != 1:
                continue
            pa, pb = pieces[ka][0], pieces[kb][0]
            if min(_mean_nn_dist(pa, pb), _mean_nn_dist(pb, pa)) < DOUBLE_MIN_SEP \
                    and _overlap_len(pa, pb, C.MERGE_ENDPOINT_TOL) >= C.BOUNDARY_OVERLAP_MIN:
                out.add(ka)
                out.add(kb)
    return out


def _merge_coincident(chains):
    """把重合（间距<DOUBLE_MIN_SEP 且重叠弧长>=BOUNDARY_OVERLAP_MIN）的链并成
    一条——它们是同一物理线的共享边界记录，不是双线。"""
    n = len(chains)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                ri, rj = find(i), find(j)
                if ri == rj:
                    continue
                pi, pj = chains[ri][1], chains[rj][1]
                if min(_mean_nn_dist(pi, pj), _mean_nn_dist(pj, pi)) < DOUBLE_MIN_SEP \
                        and _overlap_len(pi, pj, C.MERGE_ENDPOINT_TOL) >= C.BOUNDARY_OVERLAP_MIN:
                    parent[rj] = ri
                    changed = True
    comp = {}
    for i in range(n):
        comp.setdefault(find(i), []).append(i)
    out = []
    for roots in comp.values():
        label, pts, lt, mem = chains[roots[0]]
        members = set(mem)
        for r in roots[1:]:
            members |= chains[r][3]
        out.append((label, pts, lt, members))
    return out


def cluster_double_lines(chains, per_frame_d):
    """重合观测（共享边界）先并成单线，再聚类双线。

    - _merge_coincident：间距<DOUBLE_MIN_SEP 且重叠弧长足够的一对记录是同一
      物理线（A.right==B.left 共享边界），并成一条，不算双线
    - 其余链：间距 0.03~0.5m 且近似平行的一对 SOLID/DASH 边线聚成双数组

    返回 (label, members, group_lt, is_double)；单线 group_lt 为 None，
    事件线型由逐帧原始线型多数决定；双数组统一用 group_lt。
    """
    chains = _merge_coincident(chains)
    n = len(chains)
    used = [False] * n
    groups = []
    for i in range(n):
        if used[i]:
            continue
        li, pts_i, lt_i, mem_i = chains[i]
        if _lt_name(lt_i) not in ("SOLID", "DASH"):
            used[i] = True
            groups.append((li, mem_i, None, False))
            continue
        di = _chain_dir(pts_i)
        best_j, best_sep = None, DOUBLE_SEP
        if di is not None:
            for j in range(i + 1, n):
                if used[j]:
                    continue
                _lj, pts_j, lt_j, _mem_j = chains[j]
                if _lt_name(lt_j) not in ("SOLID", "DASH"):
                    continue
                dj = _chain_dir(pts_j)
                if dj is None:
                    continue
                if abs(float(np.dot(di, dj))) < DOUBLE_COS:
                    continue
                sep = min(_mean_nn_dist(pts_i, pts_j),
                          _mean_nn_dist(pts_j, pts_i))
                if sep < best_sep:
                    best_j, best_sep = j, sep
        if best_j is None:
            used[i] = True
            groups.append((li, mem_i, None, False))
            continue
        lj, _pts_j, lt_j, mem_j = chains[best_j]
        used[i] = used[best_j] = True
        mean_i = _mean_d(mem_i, per_frame_d)
        mean_j = _mean_d(mem_j, per_frame_d)
        if mean_i >= mean_j:
            gtype = _double_type(lt_i, lt_j)
            label = li
        else:
            gtype = _double_type(lt_j, lt_i)
            label = lj
        groups.append((label, mem_i | mem_j, gtype, True))
    return groups


def upgrade_shared_solid(groups, shared_keys, per_frame_d):
    """AV2 地图把双黄中心线存成相邻两段共享的一条线。缝合完成后，组内含
    共享 SOLID 重合记录（shared_keys）且全帧原始线型多数为 SOLID 的单线组
    升为 DOUBLE_SOLID；多数为 DASH 的（虚线段延伸进实线段）不升。"""
    out = []
    for label, members, gtype, is_double in groups:
        if (not is_double and gtype is None and members & shared_keys
                and _chain_raw_name(members, per_frame_d) == "SOLID"):
            gtype = "DOUBLE_SOLID"
        out.append((label, members, gtype, is_double))
    return out


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


def _keep_longest_piece(pieces, key, pts_g, lt):
    if key not in pieces or _arc_len(pts_g) > _arc_len(pieces[key][0]):
        pieces[key] = (pts_g, lt)


def scan_segment(root, split, segment, timestamps):
    """逐帧收集 d（当前帧 ego 点直算）与全局线碎片；合并物理线并聚类双线。
    返回 (frames, series)：frames[i]=(ts, excluded, ref_id, pairs, overlap, lane_y)；
    series[物理线label]=(seq, double_lt)，
    seq 条目=(frame_idx, d|None, line_type|None, exc, bridged)。"""
    info_dir = Path(root) / split / segment / "info"
    half = HALF
    frames = []
    per_frame_d = []
    pieces = {}
    footprint_ego = ego_footprint_local()
    for ts in sorted(timestamps, key=lambda x: int(x.split(".")[0])):
        ts = ts.split(".")[0]
        excluded = True
        ref_id = None
        pairs = set()
        overlap_frac = 0.0
        lane_y = {}
        dmap = {}
        frame = load_frame(info_dir, ts)
        if "annotation" in frame and frame["annotation"]:
            annotation = frame["annotation"]
            segments = annotation["lane_segment"]
            t, R = frame_pose(frame)
            ref_id, ref_in_ic, overlap_frac, lane_y = reference_segment(
                segments, footprint_ego)
            excluded = bool(ref_in_ic)
            pairs = longitudinal_pairs(segments, annotation["topology_lsls"])
            for seg in segments:
                if seg.get("is_intersection_or_connector", False):
                    continue
                for side in ("left", "right"):
                    key = (seg["id"], side)
                    raw_lt = int(seg[f"{side}_laneline_type"])
                    pts = np.array(seg[f"{side}_laneline"],
                                   dtype=np.float64)[:, :2]
                    if len(pts) >= 2 and np.isfinite(pts).all():
                        _keep_longest_piece(
                            pieces, key, ego_to_global(pts, t, R), raw_lt)
                    if excluded or not np.isfinite(pts).all():
                        continue
                    d = signed_lateral(pts)
                    if d is not None:
                        # type-0（NONE）线作为影子证据：不触发压线，仅用于
                        # 穿越前后位置与链缝合（prompt：标线重现后"继续判定"）
                        dmap[key] = (d, raw_lt)
            for area in annotation.get("area", []):
                if area.get("category", 0) != 2:
                    continue
                pts = np.array(area["points"], dtype=np.float64)[:, :2]
                if len(pts) < 2 or not np.isfinite(pts).all():
                    continue
                cside = "L" if float(np.mean(pts[:, 1])) >= 0 else "R"
                key = ("curb", str(area.get("id", -1)), cside)
                _keep_longest_piece(
                    pieces, key, ego_to_global(pts, t, R), 3)
                if excluded:
                    continue
                d = signed_lateral(pts)
                if d is not None:
                    dmap[key] = (d, 3)
        frames.append((ts, excluded, ref_id, pairs, overlap_frac, lane_y))
        per_frame_d.append(dmap)

    chains = merge_pieces(pieces)
    shared_keys = _shared_solid_keys(pieces)
    pts_of = {}
    named = []
    for label, pts, lt0, members in chains:
        for k in members:
            pts_of[k] = pts
        raw = _chain_raw_name(members, per_frame_d)
        named.append((label, pts, raw if raw is not None else lt0, members))
    groups = cluster_double_lines(named, per_frame_d)
    groups = stitch_groups(groups, per_frame_d, pts_of)
    groups = upgrade_shared_solid(groups, shared_keys, per_frame_d)
    series = {}
    for label, members, group_lt, is_double in groups:
        seq = []
        for idx in range(len(frames)):
            exc = bool(frames[idx][1])
            best = None
            if not exc:
                cands = [per_frame_d[idx][k] for k in members
                         if k in per_frame_d[idx]]
                if cands:
                    if not is_double:
                        typed = [c for c in cands if _lt_name(c[1]) is not None]
                        cands = typed or cands
                    best = min(cands, key=lambda c: abs(c[0]))
            if best is None:
                seq.append((idx, None, None, exc, False))
            else:
                raw = _lt_name(best[1])
                if group_lt is not None and (is_double or raw is not None):
                    # 组类型覆盖逐帧投票；shared-solid 组仍尊重 type-0 影子帧
                    raw = group_lt
                seq.append((idx, best[0], raw, exc, False))
        series[label] = (_bridge_gaps(seq, half), group_lt)
    return frames, series


def _bridge_gaps(seq, half, max_hole=C.MAX_HOLE_FRAMES):
    """桥接**非排除帧**最多 max_hole 帧的数据空洞：两侧都压线时按 d 线性插值
    （两侧异号记 0，即穿越发生在洞内）。排除帧不桥接。"""
    out = [list(e) for e in seq]
    i = 1
    n = len(out)
    while i < n - 1:
        if out[i][1] is not None or out[i][3]:
            i += 1
            continue
        j = i
        while j < n - 1 and out[j][1] is None and not out[j][3]:
            j += 1
        hole = j - i
        if hole < 1 or hole > max_hole or j >= n:
            i = max(j, i + 1)
            continue
        _p, pd, plt, pexc, _pb = out[i - 1]
        _n, nd, nlt, nexc, _nb = out[j]
        if pexc or nexc or pd is None or nd is None:
            i = j
            continue
        if abs(pd) > half or abs(nd) > half:
            i = j
            continue
        span = j - (i - 1)
        for k in range(i, j):
            if pd * nd < 0:
                d = 0.0
            else:
                t = (k - (i - 1)) / float(span)
                d = pd + (nd - pd) * t
            out[k][1] = d
            out[k][2] = plt if plt is not None else nlt
            out[k][4] = True
        i = j
    return [tuple(e) for e in out]


def _nearest_d(seq, pos, step, max_gap):
    """从 pos 起沿 step 方向在 max_gap 帧内找最近非 None 的 d（容忍数据空洞）。
    遇到排除帧（路口）立即停止——不得跨路口借 d 拼"完整穿越"。"""
    for k in range(max_gap + 1):
        i = pos + step * k
        if i < 0 or i >= len(seq):
            return None
        d, exc = seq[i][1], seq[i][3]
        if exc:
            return None
        if d is not None:
            return d
    return None


def _nearest_outside(seq, pos, step, max_gap, half):
    """同 _nearest_d，但只接受 |d|>half 的读数（车外的带外位置证据；
    带内读数与影子帧都不算"曾在另一侧"）。"""
    for k in range(max_gap + 1):
        i = pos + step * k
        if i < 0 or i >= len(seq):
            return None
        d, exc = seq[i][1], seq[i][3]
        if exc:
            return None
        if d is not None and abs(d) > half:
            return d
    return None


def _event_times(frames, start_idx, end_idx):
    # OpenLane-V2 timestamp 单位为纳秒（相邻帧差 5e8 = 0.5s）
    t0 = int(frames[0][0])
    return (round((int(frames[start_idx][0]) - t0) / 1e9, 1),
            round((int(frames[end_idx][0]) - t0) / 1e9 + FRAME_DT, 1))


def _overlapping_d_diff(series, key_a, key_b, idx0, idx1):
    """两链在重叠帧的 mean |d_a-d_b|（均非 None 且非桥接），无共同帧则 None。"""
    sa, sb = series.get(key_a), series.get(key_b)
    if sa is None or sb is None:
        return None
    da = {e[0]: e for e in sa[0] if idx0 <= e[0] <= idx1}
    db = {e[0]: e for e in sb[0] if idx0 <= e[0] <= idx1}
    diffs = [abs(da[k][1] - db[k][1]) for k in da
             if k in db and da[k][1] is not None and db[k][1] is not None
             and not da[k][4] and not db[k][4]]
    return float(np.mean(diffs)) if diffs else None


def merge_events(events, series, frames):
    """方向相同且帧区间重叠/相接的事件合并为一次时段：
    - 同一物理链直接合并；
    - 不同链需重叠区间内 mean|Δd|<=LINE_DUP_TOL，判为共享边界的同一
      物理线碎片（A.right / B.left）后合并。"""
    merged = []
    for e in sorted(events, key=lambda x: (x["start_idx"], x["end_idx"])):
        target = None
        for m in merged:
            if e["start_idx"] > m["end_idx"] + 1 or e["direction"] != m["direction"]:
                continue
            if e["_key"] == m["_key"]:
                target = m
                break
            lo, hi = max(e["start_idx"], m["start_idx"]), \
                min(e["end_idx"], m["end_idx"])
            if hi >= lo:
                diff = _overlapping_d_diff(series, m["_key"], e["_key"], lo, hi)
                if diff is not None and diff <= LINE_DUP_TOL:
                    target = m
                    break
        if target is not None:
            target["end_idx"] = max(target["end_idx"], e["end_idx"])
            _refresh_event_span(frames, target)
        else:
            merged.append(dict(e))
    return merged


def _direction_from_run(seq, start_idx, run):
    """prompt 第三步：压线开始前该线所在侧（骑线时线已在中轴，不能用当时
    位置）。桥接插值帧不参与计票。

    逐级回退：进入前数帧最近有效符号 -> 时段内多数符号 -> 平票取时段内
    最后有效帧 -> 时段 mean d 符号。"""
    for k in range(1, C.DIRECTION_APPROACH_FRAMES + 2):
        i = start_idx - k
        if i < 0:
            break
        d, exc = seq[i][1], seq[i][3]
        if exc:
            break
        if d is not None and abs(d) > CENTER_EPS:
            return "LEFT" if d > 0 else "RIGHT"
    signs = [d for (_i, d, _lt, bridged) in run
             if not bridged and d is not None and abs(d) > CENTER_EPS]
    if signs:
        left = sum(1 for s in signs if s > 0)
        if left * 2 > len(signs):
            return "LEFT"
        if left * 2 < len(signs):
            return "RIGHT"
        return "LEFT" if signs[-1] > 0 else "RIGHT"
    before = _nearest_d(seq, start_idx - 1, -1, C.DIRECTION_APPROACH_FRAMES)
    if before is not None and abs(before) > CENTER_EPS:
        return "LEFT" if before > 0 else "RIGHT"
    dvals = [d for (_i, d, _lt, _b) in run if d is not None]
    mean_d = float(np.mean(dvals)) if dvals else 0.0
    return "LEFT" if mean_d >= 0 else "RIGHT"


def _mk_event(frames, run, seg_id, side, direction=None, seq=None, key=None):
    """run 条目 = (frame_idx, d, line_type|None, bridged)。"""
    start_idx, end_idx = run[0][0], run[-1][0]
    names = [lt for (_i, _d, lt, _b) in run if lt]
    line_type = Counter(names).most_common(1)[0][0] if names else "SOLID"
    if direction is None:
        direction = _direction_from_run(seq or [], start_idx, run)
    start_time_s, end_time_s = _event_times(frames, start_idx, end_idx)
    return {
        "_key": key if key is not None else (seg_id, side),
        "seg_id": seg_id,
        "side": side,
        "line_type": line_type,
        "direction": direction,
        "start_idx": start_idx,
        "end_idx": end_idx,
        "n_frames": len(run),
        "start_ts": frames[start_idx][0],
        "end_ts": frames[end_idx][0],
        "start_time_s": start_time_s,
        "end_time_s": end_time_s,
    }


def _refresh_event_span(frames, e):
    e["start_ts"] = frames[e["start_idx"]][0]
    e["end_ts"] = frames[e["end_idx"]][0]
    e["n_frames"] = e["end_idx"] - e["start_idx"] + 1
    e["start_time_s"], e["end_time_s"] = _event_times(
        frames, e["start_idx"], e["end_idx"])
    return e


def _stitch_dirs(g, pts_of):
    parts = [pts_of[k] for k in sorted(g[1]) if k in pts_of]
    if not parts:
        return None
    return _chain_dir(np.vstack(parts))


def stitch_groups(groups, per_frame_d, pts_of, tol=LINE_DUP_TOL):
    """d 曲线连续（共同/相邻帧 |Δd|<=tol 且方向一致）的链视为同一物理线，
    合并成员——补 merge_pieces 端点匹配失败（type-0 碎片几何退化等）的接缝。"""
    n = len(groups)
    dmaps = []
    for _lab, members, _gt, _isd in groups:
        dm = {}
        for idx, dmap in enumerate(per_frame_d):
            vals = [dmap[k] for k in members if k in dmap]
            if vals:
                typed = [v for v in vals if _lt_name(v[1]) is not None]
                pool = typed or vals
                dm[idx] = min(pool, key=lambda c: abs(c[0]))[0]
        dmaps.append(dm)
    dirs = [_stitch_dirs(g, pts_of) for g in groups]

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def connected(i, j):
        di, dj = dmaps[i], dmaps[j]
        for idx, d1 in di.items():
            for off in (0, 1, -1):
                d2 = dj.get(idx + off)
                if d2 is not None and abs(d1 - d2) <= tol:
                    return True
        return False

    def dir_ok(i, j):
        a, b = dirs[i], dirs[j]
        if a is None or b is None:
            return True  # 退化/闭合几何：靠 |Δd|<=tol 的强共位约束即可
        return abs(float(np.dot(a, b))) >= DOUBLE_COS

    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                ri, rj = find(i), find(j)
                if ri == rj or not dir_ok(ri, rj) or not connected(ri, rj):
                    continue
                parent[rj] = ri
                dmaps[ri] = {**dmaps[ri], **dmaps[rj]}
                changed = True
    comp = {}
    for i in range(n):
        comp.setdefault(find(i), []).append(i)
    out = []
    for roots in comp.values():
        label = groups[roots[0]][0]
        members = set()
        gtype, is_double = groups[roots[0]][2], False
        for r in roots:
            _l, m, gt, isd = groups[r]
            members |= m
            if isd:
                gtype, is_double = gt, True
        out.append((label, members, gtype, is_double))
    return out


def merge_both_events(frames, events):
    """时间重叠、分居车左右的两条压线合并为 BOTH，线型取左侧。
    多条相互重叠（含合并后扩张区间）的事件一并吸收。"""
    evs = sorted(events, key=lambda x: (x["start_idx"], x["end_idx"]))
    used = [False] * len(evs)
    out = []
    for i, a in enumerate(evs):
        if used[i]:
            continue
        used[i] = True
        group = [a]
        s_idx, e_idx = a["start_idx"], a["end_idx"]
        changed = True
        while changed:
            changed = False
            for j, b in enumerate(evs):
                if used[j] or b["start_idx"] > e_idx or b["end_idx"] < s_idx:
                    continue
                if {g["direction"] for g in group} | {b["direction"]} \
                        != {"LEFT", "RIGHT"}:
                    continue
                used[j] = True
                group.append(b)
                s_idx = min(s_idx, b["start_idx"])
                e_idx = max(e_idx, b["end_idx"])
                changed = True
        if len(group) == 1:
            out.append(a)
            continue
        left_e = min((g for g in group if g["direction"] == "LEFT"),
                     key=lambda g: (g["start_idx"], g["end_idx"]))
        merged = dict(group[0])
        merged["direction"] = "BOTH"
        merged["line_type"] = left_e["line_type"]
        merged["side"] = "both"
        merged["seg_id"] = left_e["seg_id"]
        merged["start_idx"] = s_idx
        merged["end_idx"] = e_idx
        out.append(_refresh_event_span(frames, merged))
    return out


def _label_side(label):
    """series label -> (seg_id, side)；curb 为 ('curb', '<id>.<L/R>')。"""
    return label[0], ".".join(str(x) for x in label[1:])


def extract_online_events(frames, series, half=HALF):
    """连续 |d|<=half 且 >=2 帧 -> 压线时段（prompt: 仅一帧蹭线不算）。
    type-0 影子帧（lt=None）不算骑线，但可被 _nearest_outside 借用。"""
    events = []
    for label, (seq, _gtype) in series.items():
        seg_id, side = _label_side(label)
        run = []
        for idx, d, lt, _exc, bridged in seq:
            online = d is not None and lt is not None and abs(d) <= half
            if online:
                run.append((idx, d, lt, bridged))
            else:
                if len(run) >= C.MIN_ONLINE_FRAMES \
                        and _run_continuous(seq, run[0][0], run[-1][0]):
                    events.append(_mk_event(
                        frames, run, seg_id, side, seq=seq, key=label))
                run = []
        if len(run) >= C.MIN_ONLINE_FRAMES \
                and _run_continuous(seq, run[0][0], run[-1][0]):
            events.append(_mk_event(
                frames, run, seg_id, side, seq=seq, key=label))
    return merge_both_events(frames, merge_events(events, series, frames))


def extract_lanechange_events(frames, series, half=HALF):
    """完整变道（prompt 第三步【占有/越线深度 满足任一】）：
    A. 可见穿越即越线深度成立，无需占有：前 d>+half、后 d<-half（或反向）。
       视频开头即骑线（无带外进入读数）的时段不判变道（00233 守卫）。
    B. 截断穿越：线穿越车轴后不再压线、非视频末尾，且视频结束时占有新车道。
    输出全部完整变道，按时间顺序（prompt"多次变道"）。"""
    events = []
    m_gap = C.CROSSING_GAP_FRAMES
    for label, (seq, _gtype) in series.items():
        seg_id, side = _label_side(label)
        m = len(seq)
        i = 0
        while i < m:
            e_i = seq[i]
            if e_i[1] is None or e_i[2] is None or abs(e_i[1]) > half:
                i += 1
                continue
            j = i
            while (j < m and seq[j][1] is not None and seq[j][2] is not None
                   and abs(seq[j][1]) <= half):
                j += 1
            run = [(e[0], e[1], e[2], e[4]) for e in seq[i:j]]
            if len(run) < C.MIN_ONLINE_FRAMES \
                    or not _run_continuous(seq, i, j - 1):
                i = j
                continue
            before = _nearest_outside(seq, i - 1, -1, m_gap, half)
            after = _nearest_outside(seq, j, +1, m_gap, half)
            direction = None
            if before is not None and after is not None:
                if before > half and after < -half:
                    direction = "LEFT"
                elif before < -half and after > half:
                    direction = "RIGHT"
            elif after is None and j < m and _no_more_online(seq, j, half):
                last_d = run[-1][1]
                if before is not None and before > half and last_d < -CENTER_EPS:
                    if _occupies_new_lane(frames, run[0][0], run[-1][0]):
                        direction = "LEFT"
                elif before is not None and before < -half and last_d > CENTER_EPS:
                    if _occupies_new_lane(frames, run[0][0], run[-1][0]):
                        direction = "RIGHT"
            if direction:
                events.append(_mk_event(
                    frames, run, seg_id, side, direction=direction,
                    seq=seq, key=label))
            i = j
    events = merge_events(events, series, frames)
    events = _dedupe_lc_events(events, frames)
    events.sort(key=lambda e: (e["start_idx"], e["end_idx"]))
    return events


def _dedupe_lc_events(events, frames):
    """prompt"多次变道"下的去重：
    - 区间重叠但方向相反 -> 道路分合流/证据矛盾，两个都剔除；
    - 重叠或相邻且同向 -> 一次变道扫过线对的多条链，保留证据多的一条并吸收区间。"""
    evs = sorted(events, key=lambda e: (e["start_idx"], e["end_idx"]))
    changed = True
    while changed:
        changed = False
        for i in range(len(evs)):
            for j in range(i + 1, len(evs)):
                a, b = evs[i], evs[j]
                if b["start_idx"] > a["end_idx"] + 1:
                    continue
                if a["direction"] != b["direction"]:
                    if b["start_idx"] <= a["end_idx"]:
                        del evs[j]
                        del evs[i]
                        changed = True
                        break
                    continue
                big, small = (a, b) if a["n_frames"] >= b["n_frames"] else (b, a)
                big["start_idx"] = min(a["start_idx"], b["start_idx"])
                big["end_idx"] = max(a["end_idx"], b["end_idx"])
                _refresh_event_span(frames, big)
                evs.remove(small)
                changed = True
                break
            if changed:
                break
    return evs


def _run_continuous(seq, i0, i1):
    """时段物理连续性校验：进入/离开/相邻帧 d 跳变均 <= SERIES_JUMP_MAX x 帧距
    （伪影跳变按单帧算>=2.2m，真实噪声<=1.7m，跨多帧时阈值同步放宽）。
    Y 形链的 min|d| 在分支间切换会产生 >2m 的单帧跳变（00096/00233 假穿越
    根因），真实骑线/穿越的横向移动 <= ~3m/s。"""
    j = C.SERIES_JUMP_MAX
    prev, prev_idx = None, i0
    for k in range(max(0, i0 - 2), i0):
        e = seq[k]
        if e[3]:
            prev = None
            break
        if e[1] is not None:
            prev, prev_idx = e[1], k
    if prev is not None and abs(seq[i0][1] - prev) > j * (i0 - prev_idx):
        return False
    for k in range(i1 + 1, min(len(seq), i1 + 3)):
        e = seq[k]
        if not e[3] and e[1] is not None:
            if abs(e[1] - seq[i1][1]) > j * (k - i1):
                return False
            break
    for k in range(i0 + 1, i1 + 1):
        a, b = seq[k - 1][1], seq[k][1]
        if a is not None and b is not None and abs(b - a) > j:
            return False
    return True


def _no_more_online(seq, j, half):
    """压线时段之后该线在剩余视频中不再处于压线状态（允许远距离重现、
    排除帧与 type-0 影子帧）。"""
    return all(e[1] is None or e[2] is None or abs(e[1]) > half
               for e in seq[j:])


def _occupies_new_lane(frames, start_idx, end_idx,
                       back_cap=C.OCCUPY_BACKCAP_FRAMES):
    """prompt 条件1【车道占有】：视频结束时车体大部分（相交>0.5）进入新段。
    ref0 从时段起点最多回溯 back_cap 帧；ref1 从末帧向前找首个有效非排除帧。
    若拓扑上是纵向后继但中心线横向偏移 >1.5m，仍视为匝道/分流占有。"""
    ref0, pairs0, lane_y0 = None, set(), {}
    for k in range(start_idx, max(start_idx - back_cap, -1), -1):
        if frames[k][1]:
            continue
        if frames[k][2] is not None:
            ref0, pairs0, lane_y0 = frames[k][2], frames[k][3], frames[k][5]
            break
    ref1, overlap1, lane_y1 = None, 0.0, {}
    last = len(frames) - 1
    for k in range(last, min(end_idx, last) - 1, -1):
        if frames[k][1]:
            continue
        if frames[k][2] is not None:
            ref1 = frames[k][2]
            overlap1 = frames[k][4]
            lane_y1 = frames[k][5]
            break
    if ref0 is None or ref1 is None or ref0 == ref1:
        return False
    if overlap1 <= OCCUPY_FRAC:
        return False
    if (ref0, ref1) not in pairs0 and (ref1, ref0) not in pairs0:
        return True
    y0 = lane_y1.get(ref0)
    y1 = lane_y1.get(ref1)
    if y0 is None or y1 is None:
        y0 = lane_y0.get(ref0)
        y1 = lane_y0.get(ref1)
    if y0 is not None and y1 is not None and abs(y1 - y0) > RAMP_LATERAL:
        return True
    return False


def render_flag_frame(root, split, segment, timestamp, out_png):
    frame = load_frame(Path(root) / split / segment / "info", timestamp)
    annotation = assign_attribute(frame["annotation"])
    ls_bev.THICKNESS = C.LINE_WIDTH
    # 验证图开关见 config.FLAG_DRAW（attribute 着色 + area，便于目检路口/灯色）
    image = draw_annotation_bev(annotation, **C.FLAG_DRAW)
    draw_ego_vehicle(image)
    bgr = cv2.cvtColor(np.clip(image, 0, 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_png), bgr)


def write_outputs(out_dir, name, events_by_seg, frames_by_seg, dict_prefix):
    """events csv + data_dict json（有事件的段写入该段全部 timestamp）。"""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / f"{name}_events.csv"
    skip = {"start_idx", "end_idx"}

    def _plain(e):
        return {k: v for k, v in e.items()
                if k not in skip and not k.startswith("_")}
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["split", "segment", "seg_id", "side", "line_type",
                           "direction", "start_ts", "end_ts", "n_frames",
                           "start_time_s", "end_time_s"])
        writer.writeheader()
        for (split, segment), events in events_by_seg.items():
            for e in events:
                row = {"split": split, "segment": segment}
                row.update(_plain(e))
                writer.writerow(row)

    data = {}
    n_event_frames = 0
    for (split, segment), events in events_by_seg.items():
        frames = frames_by_seg[(split, segment)]
        covered = set()
        for e in events:
            for i in range(e["start_idx"], e["end_idx"] + 1):
                covered.add(frames[i][0])
        n_event_frames += len(covered)
        data.setdefault(split, {})[segment] = [fr[0] for fr in frames]
    json_path = out_dir / f"{dict_prefix}_{name}.json"
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    n_events = sum(len(v) for v in events_by_seg.values())
    n_render = sum(len(v) for s in data.values() for v in s.values())
    n_segs = sum(len(v) for v in data.values())
    print(f"[{name}] 事件 {n_events}，事件覆盖帧 {n_event_frames}，"
          f"将渲染整段帧 {n_render}，段数 {n_segs}")
    print(f"  CSV: {csv_path}")
    print(f"  data_dict: {json_path}")
    return json_path, events_by_seg


def _sample_targets(ev_by_seg, priority, n):
    picked = []
    seen = set()
    for want in priority:
        for (split, segment), events in ev_by_seg.items():
            if segment != want or not events:
                continue
            key = (split, segment)
            if key in seen:
                continue
            picked.append((key, events))
            seen.add(key)
            if len(picked) >= n:
                return picked
    for key, events in ev_by_seg.items():
        if key in seen or not events:
            continue
        picked.append((key, events))
        seen.add(key)
        if len(picked) >= n:
            break
    return picked


def main():
    args = parse_args()
    apply_bev_overrides()
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

    dict_prefix = Path(args.data_dict).stem
    write_outputs(out_dir, "online", online_by_seg, frames_by_seg, dict_prefix)
    write_outputs(out_dir, "lanechange", change_by_seg, frames_by_seg, dict_prefix)

    n = args.sample_vis
    for kind, ev_by_seg in (("online", online_by_seg), ("lanechange", change_by_seg)):
        shown = 0
        for (split, segment), events in _sample_targets(
                ev_by_seg, args.sample_segments, n):
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

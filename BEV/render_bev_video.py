import argparse
import shutil
import sys
import tarfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import cv2
import numpy as np

from openlanev2.lanesegment.dataset import Collection
from openlanev2.lanesegment.io import io
from openlanev2.lanesegment.preprocessing import collect
from openlanev2.lanesegment.visualization import (
    assign_attribute,
    draw_annotation_bev,
)
import openlanev2.lanesegment.visualization.bev as ls_bev
import openlanev2.centerline.visualization.bev as cl_bev

import config as C

# 兼容旧引用：自车参数（nuPlan Pacifica，米；原点=后轴中心）与插值点数集中在 config.py
PACIFICA = C.PACIFICA
N_POINTS = C.N_POINTS


def apply_bev_overrides():
    """运行时 patch 官方画布常量（不改官方源码）。BEV_RANGE/BEV_SCALE 在
    ls_bev 与 cl_bev（_draw_vertex）中各有一份，需同步。"""
    for mod in (ls_bev, cl_bev):
        mod.BEV_SCALE = C.BEV_SCALE
        mod.BEV_RANGE = list(C.BEV_RANGE)


def _ego_to_col(y_ego):
    # 与官方 _draw_line 相同：左为正 y，像素列向小
    return int(round(ls_bev.BEV_SCALE * (ls_bev.BEV_RANGE[3] - y_ego)))


def _ego_to_row(x_ego):
    # 前为正 x，像素行向小（车头朝上）
    return int(round(ls_bev.BEV_SCALE * (ls_bev.BEV_RANGE[1] - x_ego)))


def draw_ego_vehicle(image, rear=None, front=None, width=None):
    """在标注 BEV 图上叠加自车矩形。官方 draw_annotation_bev 不画自车，故在此补画。
    尺寸默认 config.PACIFICA，样式默认 config.EGO_STYLE。"""
    if rear is None or front is None or width is None:
        rear, front, width = C.PACIFICA
    s = C.EGO_STYLE
    half = width / 2
    pt1 = (_ego_to_col(half), _ego_to_row(front))
    pt2 = (_ego_to_col(-half), _ego_to_row(-rear))
    cv2.rectangle(image, pt1, pt2, s["fill"], -1)
    cv2.rectangle(image, pt1, pt2, s["outline"], s["outline_width"])
    cv2.arrowedLine(
        image,
        (_ego_to_col(0), _ego_to_row((front - rear) / 2)),
        (_ego_to_col(0), _ego_to_row(front - s["arrow_nose_margin"])),
        s["arrow"],
        s["arrow_width"],
        tipLength=s["arrow_tip_length"],
    )


def _draw_line_fast(image, line, with_attribute, with_linetype):
    """官方 _draw_line 的等价快速实现：一次 cv2.polylines 替代 999 次 cv2.line。

    官方实现（openlanev2/lanesegment/visualization/bev.py:33）把每条折线
    interp_arc 重采样到 1000 点后逐段 cv2.line，每帧约 25 万次调用；
    本函数逐点取整方式与官方一致（int 截断 + 偏移），仅合并绘制调用。
    运行时 patch 到 ls_bev._draw_line，不改官方源码。
    """
    points = np.array(line["points"])
    points = ls_bev.BEV_SCALE * (
        -points[:, :2] + np.array([ls_bev.BEV_RANGE[1], ls_bev.BEV_RANGE[3]]))
    points = ls_bev.interp_arc(points, C.INTERP_POINTS)
    if points is None:
        return

    if with_attribute and len(set(line["attributes"]) - set([0])):
        colors = [ls_bev.COLOR_DICT[a] for a in set(line["attributes"]) - set([0])]
    elif with_linetype and line["linetype"]:
        colors = [ls_bev.COLOR_DICT[line["linetype"]]]
    else:
        colors = [ls_bev.COLOR_DEFAULT]

    thickness = ls_bev.THICKNESS
    for idx, color in enumerate(colors):
        pts = (points + idx * thickness * 1.5).astype(np.int32)
        pts = np.stack([pts[:, 1], pts[:, 0]], axis=1)
        cv2.polylines(image, [pts], False, color=color,
                      thickness=thickness, lineType=cv2.LINE_AA)


def _ls_json_exists(dest_root, split, segment):
    info = Path(dest_root) / split / segment / "info"
    return any(info.glob("*-ls.json"))


def prepare_data(tar_path, dest_root, split=None, segment=None,
                 data_dict=None):
    split = split or C.SPLIT
    segment = segment or C.SEGMENT
    dest = Path(dest_root)
    dest.mkdir(parents=True, exist_ok=True)
    checks = []
    if data_dict and (segment == "all" or split == "all"):
        for sp, segs in data_dict.items():
            if split not in ("all", sp):
                continue
            for sg in segs:
                if segment not in ("all", sg):
                    continue
                checks.append((sp, sg))
    else:
        if split == "all" or segment == "all":
            raise ValueError(
                "--prepare-data 配 all 需要能读到的 --data-dict（当前为空）")
        checks = [(split, segment)]
    if not checks:
        raise ValueError(
            f"data_dict 过滤后没有任何段可校验（split={split} "
            f"segment={segment}），请检查 --split/--segment/--data-dict")
    missing = [(sp, sg) for sp, sg in checks
               if not _ls_json_exists(dest, sp, sg)]
    if not missing:
        print(f"已存在 {len(checks)} 段 *-ls.json，跳过解压")
        return
    print(f"解压 {tar_path} -> {dest}（缺 {len(missing)} 段，约 1GB）")
    with tarfile.open(tar_path, "r") as tf:
        # py3.8 无 filter 参数；升级 Python>=3.12 后应加 filter='data'
        tf.extractall(dest)
    still = [(sp, sg) for sp, sg in missing
             if not _ls_json_exists(dest, sp, sg)]
    if still:
        raise FileNotFoundError(
            f"解压后仍缺 {still[0][0]}/{still[0][1]}/*-ls.json 等 "
            f"{len(still)} 段，检查 tar 是否完整"
        )


def parse_args():
    parser = argparse.ArgumentParser(description="Render OpenLane-V2 BEV video")
    parser.add_argument("--root", default=str(C.DATA_ROOT))
    parser.add_argument("--data-dict", default=C.DATA_DICT)
    parser.add_argument("--collection", default=C.COLLECTION)
    parser.add_argument("--split", default=C.SPLIT)
    parser.add_argument("--segment", default=C.SEGMENT)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--fps", type=int, default=C.FPS,
                        help="视频帧率（数据约 2Hz，默认 2 为实时）")
    parser.add_argument("--no-render", action="store_true",
                        help="只做 --prepare-data / --preprocess，不渲染视频")
    parser.add_argument(
        "--line-width",
        type=int,
        default=C.LINE_WIDTH,
        help="线宽（官方 THICKNESS=4，覆盖为运行时 patch，不改官方源码）",
    )
    parser.add_argument("--preprocess", action="store_true")
    parser.add_argument("--only-segment", action="store_true")
    parser.add_argument("--prepare-data", action="store_true")
    parser.add_argument("--no-png", action="store_true", help="只写视频,不导出逐帧 png")
    parser.add_argument("--per-segment", action="store_true",
                        help="按段拆分输出到 <out-dir>/<split>/<segment>/bev.mp4（配合 --segment all）")
    parser.add_argument("--copy-images", action="store_true",
                        help="把命中帧对应的相机图复制到段文件夹,命名 <segment>_image_<camera>_<timestamp>.jpg")
    parser.add_argument("--image-root", default=str(C.IMAGE_ROOT))
    parser.add_argument(
        "--cameras",
        nargs="*",
        default=list(C.CAMERAS),
        help="要复制的相机目录名;传 all 表示该段全部相机",
    )
    parser.add_argument("--no-fast-lines", dest="fast_lines", action="store_false",
                        help="关闭 cv2.polylines 快速绘制,回退官方逐段 cv2.line")
    parser.add_argument("--with-ego", dest="with_ego", action="store_true", default=True)
    parser.add_argument("--no-ego", dest="with_ego", action="store_false")
    parser.add_argument("--centerline", dest="centerline", action="store_true",
                        default=None,
                        help="渲染车道中心线（默认取 config.RENDER_DRAW）")
    parser.add_argument("--no-centerline", dest="centerline", action="store_false")
    parser.add_argument("--laneline", dest="laneline", action="store_true",
                        default=None, help="渲染左右边线（默认取 config.RENDER_DRAW）")
    parser.add_argument("--no-laneline", dest="laneline", action="store_false")
    parser.add_argument(
        "--ego-size",
        nargs=3,
        type=float,
        metavar=("REAR", "FRONT", "WIDTH"),
        default=list(C.PACIFICA),
        help="自车尺寸（米）：后轴到车尾、后轴到车头、车宽",
    )
    parser.add_argument("--info-ls-tar", default=str(C.INFO_LS_TAR))
    return parser.parse_args()


def run_preprocess(root, data_dict_name, collection, split, segment, only_segment):
    dict_path = Path(root) / data_dict_name  # pathlib 对绝对路径自动覆盖
    if not dict_path.exists():
        dict_path = Path(data_dict_name)  # 尝试按当前工作目录解析
    data_dict = io.json_load(str(dict_path))
    if only_segment:
        if split not in data_dict or segment not in data_dict[split]:
            avail = ", ".join(
                f"{sp}/{sg}" for sp, segs in data_dict.items()
                for sg in list(segs)[:2])
            raise KeyError(
                f"{data_dict_name} 中没有 {split}/{segment}；"
                f"该文件包含的段示例: {avail}（共 "
                f"{sum(len(v) for v in data_dict.values())} 段）")
        data_dict = {split: {segment: data_dict[split][segment]}}
    collect(root, data_dict, collection, with_sd_map=C.WITH_SD_MAP,
            n_points=N_POINTS)
    print(f"已生成 {root}/{collection}.pkl")


def overlay_time(bgr, t_sec):
    """左上角烧 t=X.Xs（相对本段第一帧），外观参数见 config.TIME_OVERLAY。"""
    o = C.TIME_OVERLAY
    text = f"t={t_sec:.1f}s"
    cv2.putText(bgr, text, o["pos"], cv2.FONT_HERSHEY_SIMPLEX,
                o["font_scale"], (0, 0, 0), o["outline_width"], cv2.LINE_AA)
    cv2.putText(bgr, text, o["pos"], cv2.FONT_HERSHEY_SIMPLEX,
                o["font_scale"], (255, 255, 255), o["text_width"], cv2.LINE_AA)
    return bgr


def render_frame_bgr(frame, with_ego, ego_size, with_centerline=None,
                     with_laneline=None):
    draw = dict(C.RENDER_DRAW)
    if with_centerline is not None:
        draw["with_centerline"] = with_centerline
    if with_laneline is not None:
        draw["with_laneline"] = with_laneline
    ann = frame.get_annotations()
    if ann is None:
        return None
    ann = assign_attribute(ann)
    bev = draw_annotation_bev(ann, **draw)
    if with_ego:
        draw_ego_vehicle(bev, *ego_size)
    bev = np.clip(bev, 0, 255).astype(np.uint8)
    return cv2.cvtColor(bev, cv2.COLOR_RGB2BGR)


def copy_segment_images(image_root, split, segment, timestamps, dst_dir, cameras):
    """把命中帧的相机图复制为 <segment>_image_<camera>_<timestamp>.jpg。"""
    src_base = Path(image_root) / split / segment / "image"
    if not src_base.is_dir():
        return 0, 0  # 该 split/段本就没有相机图（val/test），不计缺失
    if cameras == ["all"]:
        cams = sorted(p.name for p in src_base.iterdir() if p.is_dir())
    else:
        cams = list(cameras)
    copied = missing = 0
    for ts in timestamps:
        for cam in cams:
            src = src_base / cam / f"{ts}.jpg"
            if src.is_file():
                shutil.copy2(src, dst_dir / f"{segment}_image_{cam}_{ts}.jpg")
                copied += 1
            else:
                missing += 1
    return copied, missing


def render_segment(root, collection, split, segment, out_dir, fps, with_ego=True,
                   ego_size=C.PACIFICA, no_png=False, per_segment=False,
                   copy_images=False, image_root=None, cameras=tuple(C.CAMERAS),
                   with_centerline=None, with_laneline=None):
    print("官方 collect / draw_annotation_bev，CPU 绘制标注 BEV。")
    dataset = Collection(root, root, collection)
    frames = []
    for i in range(len(dataset.keys)):
        identifier, frame = dataset.get_frame_via_index(i)
        if split not in ("all", identifier[0]):
            continue
        if segment not in ("all", identifier[1]):
            continue
        frames.append((identifier, frame))
    frames.sort(key=lambda item: (item[0][0], item[0][1], int(item[0][2])))
    if not frames:
        raise RuntimeError(
            f"pkl 中没有 {split}/{segment}。先加 --preprocess，或检查 --collection/--segment"
        )

    out_dir = Path(out_dir)
    groups = {}
    for item in frames:
        key = (item[0][0], item[0][1]) if per_segment else None
        groups.setdefault(key, []).append(item)

    total_written = 0
    for key, group in groups.items():
        if per_segment:
            gsplit, gseg = key
            sub_dir = out_dir / gsplit / gseg
        else:
            gsplit = gseg = None
            sub_dir = out_dir
        sub_dir.mkdir(parents=True, exist_ok=True)
        writer = None
        written = 0
        timestamps = []
        t0 = int(group[0][0][2])

        for i, (identifier, frame) in enumerate(group):
            bgr = render_frame_bgr(frame, with_ego, ego_size,
                                   with_centerline, with_laneline)
            if bgr is None:
                print(f"跳过无标注帧 {identifier}")
                continue
            t_sec = (int(identifier[2]) - t0) / 1e9
            overlay_time(bgr, t_sec)
            if not no_png:
                cv2.imwrite(str(sub_dir / f"{i:06d}.png"), bgr)
            if writer is None:
                height, width = bgr.shape[:2]
                writer = cv2.VideoWriter(
                    str(sub_dir / "bev.mp4"),
                    cv2.VideoWriter_fourcc(*C.VIDEO_FOURCC),
                    fps,
                    (width, height),
                )
            writer.write(bgr)
            written += 1
            timestamps.append(identifier[2])
            if not per_segment:
                print(identifier)

        if writer is not None:
            writer.release()
        total_written += written
        if per_segment:
            print(f"{gsplit}/{gseg}: {written} 帧 -> {sub_dir / 'bev.mp4'}", flush=True)
            if copy_images:
                copied, missing = copy_segment_images(
                    image_root, gsplit, gseg, timestamps, sub_dir, list(cameras))
                if copied or missing:
                    print(f"  相机图: 复制 {copied} 张, 缺失 {missing} 张", flush=True)

    if total_written == 0:
        raise RuntimeError("没有写出任何帧（可能全是 test 无标注）")
    if per_segment:
        print(f"完成 {total_written} 帧、{len(groups)} 段 -> {out_dir}")
    else:
        print(f"完成 {total_written} 帧 -> {out_dir / 'bev.mp4'}")


def main():
    args = parse_args()
    if args.copy_images and not args.per_segment:
        raise SystemExit("--copy-images 需与 --per-segment 同用")
    apply_bev_overrides()
    ls_bev.THICKNESS = args.line_width
    cl_bev.THICKNESS = args.line_width
    if args.fast_lines:
        ls_bev._draw_line = _draw_line_fast
    out_dir = args.out_dir or str(C.VIS_DIR / f"bev_{args.segment}")
    if args.prepare_data:
        dict_path = Path(args.root) / args.data_dict
        if not dict_path.exists():
            dict_path = Path(args.data_dict)
        data_dict = io.json_load(str(dict_path)) if dict_path.exists() else None
        prepare_data(
            args.info_ls_tar, args.root, args.split, args.segment,
            data_dict=data_dict,
        )
    if args.preprocess:
        run_preprocess(
            args.root,
            args.data_dict,
            args.collection,
            args.split,
            args.segment,
            args.only_segment,
        )
    if args.no_render:
        return
    render_segment(
        args.root,
        args.collection,
        args.split,
        args.segment,
        out_dir,
        args.fps,
        args.with_ego,
        tuple(args.ego_size),
        args.no_png,
        args.per_segment,
        args.copy_images,
        args.image_root,
        tuple(args.cameras),
        args.centerline,
        args.laneline,
    )


if __name__ == "__main__":
    main()

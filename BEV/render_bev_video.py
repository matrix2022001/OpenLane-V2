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
from openlanev2.lanesegment.visualization.bev import BEV_SCALE, BEV_RANGE
import openlanev2.lanesegment.visualization.bev as ls_bev
import openlanev2.centerline.visualization.bev as cl_bev

N_POINTS = {
    "area": 20,
    "centerline": 10,
    "left_laneline": 20,
    "right_laneline": 20,
}

# nuPlan Pacifica 自车参数（米）：后轴→车尾 / 后轴→车头 / 车宽。
# 标注为 Ego 坐标系、原点=后轴中心（nuPlan 惯例）。
PACIFICA = (1.127, 4.049, 2.297)


def _ego_to_col(y_ego):
    # 与官方 _draw_line 相同：左为正 y，像素列向小
    return int(round(BEV_SCALE * (BEV_RANGE[3] - y_ego)))


def _ego_to_row(x_ego):
    # 前为正 x，像素行向小（车头朝上）
    return int(round(BEV_SCALE * (BEV_RANGE[1] - x_ego)))


def draw_ego_vehicle(image, rear=PACIFICA[0], front=PACIFICA[1], width=PACIFICA[2]):
    """在标注 BEV 图上叠加自车框。官方 draw_annotation_bev 不画自车，故在此补画。"""
    half = width / 2
    pt1 = (_ego_to_col(half), _ego_to_row(front))
    pt2 = (_ego_to_col(-half), _ego_to_row(-rear))
    cv2.rectangle(image, pt1, pt2, (255, 0, 0), -1)
    cv2.rectangle(image, pt1, pt2, (0, 0, 0), 2)
    cv2.arrowedLine(
        image,
        (_ego_to_col(0), _ego_to_row((front - rear) / 2)),
        (_ego_to_col(0), _ego_to_row(front - 0.1)),
        (255, 255, 255),
        2,
        tipLength=0.3,
    )


def _draw_line_fast(image, line, with_attribute, with_linetype):
    """官方 _draw_line 的等价快速实现：一次 cv2.polylines 替代 999 次 cv2.line。

    官方实现（openlanev2/lanesegment/visualization/bev.py:33）把每条折线
    interp_arc 重采样到 1000 点后逐段 cv2.line，每帧约 25 万次调用；
    本函数逐点取整方式与官方一致（int 截断 + 偏移），仅合并绘制调用。
    运行时 patch 到 ls_bev._draw_line，不改官方源码。
    """
    points = np.array(line["points"])
    points = BEV_SCALE * (-points[:, :2] + np.array([BEV_RANGE[1], BEV_RANGE[3]]))
    points = ls_bev.interp_arc(points)
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


def prepare_data(tar_path, dest_root, split="train", segment="00000"):
    dest = Path(dest_root)
    dest.mkdir(parents=True, exist_ok=True)
    marker = dest / split / segment / "info"
    if any(marker.glob("*-ls.json")):
        print(f"已存在 {marker}/*-ls.json，跳过解压")
        return
    print(f"解压 {tar_path} -> {dest}（约 1GB，需数分钟）")
    with tarfile.open(tar_path, "r") as tf:
        tf.extractall(dest)
    if not any(marker.glob("*-ls.json")):
        raise FileNotFoundError(
            f"解压后仍无 {marker}/*-ls.json，检查 tar 是否完整"
        )


def parse_args():
    parser = argparse.ArgumentParser(description="Render OpenLane-V2 BEV video")
    parser.add_argument("--root", default=str(REPO_ROOT / "data/OpenLane-V2"))
    parser.add_argument("--data-dict", default="data_dict_subset_A.json")
    parser.add_argument("--collection", default="data_dict_subset_A_ls")
    parser.add_argument("--split", default="train")
    parser.add_argument("--segment", default="00000")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--fps", type=int, default=10)
    parser.add_argument(
        "--line-width",
        type=int,
        default=2,
        help="线宽（官方 THICKNESS=4，覆盖为运行时 patch，不改官方源码）",
    )
    parser.add_argument("--preprocess", action="store_true")
    parser.add_argument("--only-segment", action="store_true")
    parser.add_argument("--prepare-data", action="store_true")
    parser.add_argument("--no-png", action="store_true", help="只写视频,不导出逐帧 png")
    parser.add_argument("--per-segment", action="store_true",
                        help="按 segment 拆分输出到 <out-dir>/<segment>/bev.mp4(配合 --segment all)")
    parser.add_argument("--copy-images", action="store_true",
                        help="把命中帧对应的相机图复制到段文件夹,命名 <segment>_image_<camera>_<timestamp>.jpg")
    parser.add_argument(
        "--image-root",
        default=str(
            REPO_ROOT
            / "download_dataset/OpenDriveLab___OpenLane-V2/raw/"
            / "OpenLane-V2_subset_A_image_0"
        ),
    )
    parser.add_argument(
        "--cameras",
        nargs="*",
        default=["ring_front_center"],
        help="要复制的相机目录名;传 all 表示该段全部相机",
    )
    parser.add_argument("--no-fast-lines", dest="fast_lines", action="store_false",
                        help="关闭 cv2.polylines 快速绘制,回退官方逐段 cv2.line")
    parser.add_argument("--with-ego", dest="with_ego", action="store_true", default=True)
    parser.add_argument("--no-ego", dest="with_ego", action="store_false")
    parser.add_argument(
        "--ego-size",
        nargs=3,
        type=float,
        metavar=("REAR", "FRONT", "WIDTH"),
        default=list(PACIFICA),
        help="自车尺寸（米）：后轴到车尾、后轴到车头、车宽",
    )
    parser.add_argument(
        "--info-ls-tar",
        default=str(
            REPO_ROOT
            / "download_dataset/OpenDriveLab___OpenLane-V2/raw/"
            / "OpenLane-V2_subset_A_info-ls/OpenLane-V2_subset_A_info-ls"
        ),
    )
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
    collect(root, data_dict, collection, n_points=N_POINTS)
    print(f"已生成 {root}/{collection}.pkl")


def render_frame_bgr(frame, with_ego, ego_size):
    ann = frame.get_annotations()
    if ann is None:
        return None
    ann = assign_attribute(ann)
    bev = draw_annotation_bev(
        ann,
        with_attribute=False,
        with_linetype=True,
        with_centerline=True,
        with_laneline=True,
        with_area=False,
    )
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
                   ego_size=PACIFICA, no_png=False, per_segment=False,
                   copy_images=False, image_root=None, cameras=("ring_front_center",)):
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
            sub_dir = out_dir / gseg
        else:
            gsplit = gseg = None
            sub_dir = out_dir
        sub_dir.mkdir(parents=True, exist_ok=True)
        writer = None
        written = 0
        timestamps = []

        for i, (identifier, frame) in enumerate(group):
            bgr = render_frame_bgr(frame, with_ego, ego_size)
            if bgr is None:
                print(f"跳过无标注帧 {identifier}")
                continue
            if not no_png:
                cv2.imwrite(str(sub_dir / f"{i:06d}.png"), bgr)
            if writer is None:
                height, width = bgr.shape[:2]
                writer = cv2.VideoWriter(
                    str(sub_dir / "bev.mp4"),
                    cv2.VideoWriter_fourcc(*"mp4v"),
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
    ls_bev.THICKNESS = args.line_width
    cl_bev.THICKNESS = args.line_width
    if args.fast_lines:
        ls_bev._draw_line = _draw_line_fast
    out_dir = args.out_dir or str(
        Path(__file__).resolve().parent / "vis" / f"bev_{args.segment}"
    )
    if args.prepare_data:
        prepare_data(args.info_ls_tar, args.root, args.split, args.segment)
    if args.preprocess:
        run_preprocess(
            args.root,
            args.data_dict,
            args.collection,
            args.split,
            args.segment,
            args.only_segment,
        )
    if args.copy_images and not args.per_segment:
        parser_error = "--copy-images 需与 --per-segment 同用"
        raise SystemExit(parser_error)
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
    )


if __name__ == "__main__":
    main()

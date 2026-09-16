# -*- coding: utf-8 -*-
"""一键重新判定压线/变道并渲染对应 BEV 视频。

串联三步（与 BEV.md 附录 A4 手动链路等价）：
  1) filter_driving_behavior.py  全量重判定 -> out/*.csv + 行为 data_dict json
  2) render_bev_video.py         online 行为视频 -> vis/bev_behavior/online/<split>/<seg>/bev.mp4
  3) render_bev_video.py         lanechange 行为视频 -> vis/bev_behavior/lanechange/...

用法示例（在 BEV/ 下）：
  uv run python main.py                     # 重判定 + 重渲染两组视频
  uv run python main.py --skip-filter       # 只重渲染（pkl/判定结果不变）
  uv run python main.py --skip-render        # 只重判定
  uv run python main.py --dry-run           # 只打印将执行的命令
"""
import argparse
import csv
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import config as C

BEV_DIR = Path(__file__).resolve().parent
KINDS = ("online", "lanechange")


def parse_args():
    prefix = Path(C.DATA_DICT).stem
    ap = argparse.ArgumentParser(description="重新判定压线/变道并渲染 BEV 视频")
    ap.add_argument("--skip-filter", action="store_true",
                    help="跳过判定，仅渲染（沿用现有 out/ 结果）")
    ap.add_argument("--skip-render", action="store_true",
                    help="跳过渲染，仅判定")
    ap.add_argument("--kinds", nargs="*", default=list(KINDS),
                    choices=list(KINDS), help="要渲染的行为类别")
    ap.add_argument("--sample-vis", type=int, default=C.SAMPLE_VIS)
    ap.add_argument("--sample-segments", nargs="*",
                    default=list(C.SAMPLE_SEGMENTS))
    ap.add_argument("--limit-segments", type=int, default=0,
                    help="调试用：透传给 filter，每 split 只处理前 N 段")
    ap.add_argument("--filter-out-dir", default=str(C.OUT_DIR),
                    help="filter 产出目录（渲染也从此目录读 json）")
    ap.add_argument("--out-root", default=str(C.VIS_DIR / "bev_behavior"),
                    help="行为视频输出根目录")
    ap.add_argument("--fps", type=int, default=C.FPS)
    ap.add_argument("--copy-images", dest="copy_images", action="store_true",
                    default=True)
    ap.add_argument("--no-copy-images", dest="copy_images", action="store_false")
    ap.add_argument("--collection-prefix", default=None,
                    help="pkl 名前缀，默认同 data_dict 文件名 stem（调试时隔离生产 pkl）")
    ap.add_argument("--result", default=str(C.RESULT_MD),
                    help="渲染完成后写出的 result.md 路径")
    ap.add_argument("--keep-old-videos", action="store_true",
                    help="不清理旧的 <out-root>/<kind>/ 目录（默认渲染前清理，"
                         "防止 result.md/浏览时混入上一轮段）")
    ap.add_argument("--preprocess", dest="preprocess", action="store_true",
                    default=None,
                    help="collect 重建 pkl；默认跑过 filter 则开、--skip-filter 则关")
    ap.add_argument("--no-preprocess", dest="preprocess", action="store_false")
    ap.add_argument("--dry-run", action="store_true", help="只打印命令不执行")
    args = ap.parse_args()
    args.dict_prefix = prefix
    return args


def run(cmd, dry_run):
    print('+ ' + ' '.join(str(c) for c in cmd), flush=True)
    if dry_run:
        return 0
    t0 = time.time()
    rc = subprocess.call([sys.executable] + [str(c) for c in cmd], cwd=BEV_DIR)
    print('  -> exit=%d 用时 %.1f min' % (rc, (time.time() - t0) / 60),
          flush=True)
    return rc


def _rendered_segments(kind_root):
    """枚举 <out-root>/<kind>/<split>/<segment>/ 下含 bev.mp4 的 (split, segment)。"""
    segs = set()
    kind_root = Path(kind_root)
    if not kind_root.exists():
        return segs
    for split_dir in kind_root.iterdir():
        if not split_dir.is_dir():
            continue
        for seg_dir in split_dir.iterdir():
            if seg_dir.is_dir() and (seg_dir / "bev.mp4").exists():
                segs.add((split_dir.name, seg_dir.name))
    return segs


def _events_by_segment(csv_path):
    by_seg = {}
    csv_path = Path(csv_path)
    if not csv_path.exists():
        return by_seg
    with open(csv_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            by_seg.setdefault((r["split"], r["segment"]), []).append(r)
    for lst in by_seg.values():
        lst.sort(key=lambda r: float(r["start_time_s"]))
    return by_seg


def write_result_md(result_path, filter_out, kinds, out_root):
    """把已渲染段文件夹 + 事件明细写成 Markdown 表格（一段多事件 -> 多行）。"""
    lines = ["# BEV 行为视频结果", "",
             "生成时间: %s" % datetime.now().strftime("%Y-%m-%d %H:%M"), ""]
    for kind in kinds:
        segs = _rendered_segments(Path(out_root) / kind)
        evs = _events_by_segment(Path(filter_out) / f"{kind}_events.csv")
        rows, n_ev = [], 0
        for split, seg in sorted(segs):
            lst = evs.get((split, seg), [])
            if lst:
                n_ev += len(lst)
                for e in lst:
                    rows.append((split, seg, e["line_type"], e["direction"],
                                 e["start_time_s"], e["end_time_s"]))
            else:
                rows.append((split, seg, "", "", "", ""))
        lines.append("## %s（%d 段 / %d 事件）" % (kind, len(segs), n_ev))
        lines.append("")
        if not rows:
            lines.append("（无事件段）")
            lines.append("")
            continue
        lines.append("| split | segment_id | line_type | direction | start_time | end_time |")
        lines.append("|---|---|---|---|---|---|")
        for r in rows:
            lines.append("| " + " | ".join(r) + " |")
        lines.append("")
    Path(result_path).write_text("\n".join(lines), encoding="utf-8")
    print("result.md ->", result_path)


def main():
    args = parse_args()
    filter_out = Path(args.filter_out_dir)
    preprocess = args.preprocess if args.preprocess is not None \
        else not args.skip_filter

    if not args.skip_filter:
        cmd = ["filter_driving_behavior.py",
               "--sample-vis", args.sample_vis,
               "--sample-segments", *args.sample_segments,
               "--out-dir", filter_out]
        if args.limit_segments:
            cmd += ["--limit-segments", args.limit_segments]
        if run(cmd, args.dry_run) != 0:
            sys.exit('filter 失败，终止')

    if args.skip_render:
        return

    for kind in args.kinds:
        dict_path = filter_out / f"{args.dict_prefix}_{kind}.json"
        coll_prefix = args.collection_prefix or args.dict_prefix
        collection = f"{coll_prefix}_{kind}_ls"
        if not args.dry_run:
            if not dict_path.exists():
                sys.exit(f'缺少 {dict_path}，请先跑判定（去掉 --skip-filter）')
            if not json.loads(dict_path.read_text(encoding='utf-8')):
                print(f'[{kind}] 无事件段（{dict_path.name} 为空），跳过渲染')
                kind_root = Path(args.out_root) / kind
                if not args.keep_old_videos and not args.dry_run \
                        and kind_root.exists():
                    shutil.rmtree(kind_root)
                    print(f'[{kind}] 已清理旧视频目录 {kind_root}')
                continue
        kind_root = Path(args.out_root) / kind
        if not args.keep_old_videos and not args.dry_run and kind_root.exists():
            shutil.rmtree(kind_root)
            print(f'[{kind}] 清理旧视频目录 {kind_root}')
        cmd = ["render_bev_video.py",
               "--data-dict", dict_path,
               "--collection", collection,
               "--split", "all", "--segment", "all",
               "--out-dir", Path(args.out_root) / kind,
               "--no-png", "--per-segment", "--fps", args.fps]
        if preprocess:
            cmd.append("--preprocess")
        if args.copy_images:
            cmd.append("--copy-images")
        if run(cmd, args.dry_run) != 0:
            sys.exit(f'{kind} 渲染失败，终止')

    if not args.dry_run:
        write_result_md(args.result, filter_out, args.kinds, args.out_root)
    print('完成。视频根目录:', args.out_root)


if __name__ == "__main__":
    main()

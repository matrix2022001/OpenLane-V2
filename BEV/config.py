# -*- coding: utf-8 -*-
"""BEV 脚本（render_bev_video.py / filter_driving_behavior.py）的全部可配置参数。

约定：脚本只从本文件取默认值与阈值，CLI 参数可覆盖默认值；
调参/回归实验改这里即可，两个脚本行为保持一致。
"""
from pathlib import Path

BEV_DIR = Path(__file__).resolve().parent
REPO_ROOT = BEV_DIR.parent

# ---------------- 数据路径 ----------------
DATA_ROOT = REPO_ROOT / "data" / "OpenLane-V2"
DATA_DICT = "data_dict_subset_A.json"          # 相对 DATA_ROOT
COLLECTION = "data_dict_subset_A_ls"           # collect 生成的 pkl 名（不含 .pkl）
IMAGE_ROOT = (REPO_ROOT / "download_dataset" / "OpenDriveLab___OpenLane-V2"
              / "raw" / "OpenLane-V2_subset_A_image_0")
INFO_LS_TAR = (REPO_ROOT / "download_dataset" / "OpenDriveLab___OpenLane-V2"
               / "raw" / "OpenLane-V2_subset_A_info-ls"
               / "OpenLane-V2_subset_A_info-ls")
OUT_DIR = BEV_DIR / "out"                      # 筛选产出目录
VIS_DIR = BEV_DIR / "vis"                      # 渲染输出根目录
RESULT_MD = BEV_DIR / "result.md"              # main.py 渲染完成后写出的结果清单

# ---------------- 自车（2017 Ford Fusion Hybrid，米；原点=后轴中心） ----------------
# 数据源（Car and Driver 2017 Fusion Hybrid 规格页，与 carfolio / automobile-catalog
# 的 mm 值一致）：https://www.caranddriver.com/ford/fusion/specs/2017/ford_fusion_ford-fusion-hybrid_2017
#   Length 191.8 in = 4.872 m；Wheelbase 112.2 in = 2.850 m
#   Width w/o mirrors 72.9 in = 1.852 m；Width w/ mirrors 83.5 in = 2.121 m
# 官方只公布总长与轴距 -> 前后悬合计 2.022 m，各家目录的 overhang 字段均为 “-”；
# 按三厢前驱车比例取前悬 0.940 m、后悬 1.082 m（同平台 2850 轴距的 Ford Everest
# 实测前悬 905 / 后悬 1137 同向）。原点=后轴中心与 AV2 vehicle frame 一致
# （arXiv:2301.00493 Fig.8：x 前、y 左、原点在后轴中心）。
EGO_LENGTH = 4.872
EGO_WHEELBASE = 2.850
EGO_FRONT_OVERHANG = 0.940                     # 前保->前轴（推算值，见上）
EGO_REAR = round(EGO_LENGTH - EGO_WHEELBASE - EGO_FRONT_OVERHANG, 3)   # 后轴->车尾 1.082
EGO_FRONT = round(EGO_WHEELBASE + EGO_FRONT_OVERHANG, 3)               # 后轴->车头 3.790
EGO_WIDTH = 1.852                              # 车身宽，不含后视镜（72.9 in）
EGO_MIRROR_WIDTH = 2.121                       # 含后视镜宽（83.5 in），仅备查
EGO_SIZE = (EGO_REAR, EGO_FRONT, EGO_WIDTH)    # 画框/判定共用的单一来源
# 车体包络半宽：footprint（参考段/路口排除/车道占有）与变道“线已到车外”判据
# 都用车身宽（不含后视镜）；含镜包络半宽 1.0605 仅备查。
# 已知代价（2026-09-22 A/B 实测）：00094 的变道带内 typed 帧只剩 1 帧
# （< MIN_ONLINE_FRAMES=2）而丢失；改用含镜 1.0605 可保住（4.5-5.5s，2 帧）。
EGO_HALF = EGO_WIDTH / 2                       # 0.926
EGO_CENTER_X = (EGO_FRONT - EGO_REAR) / 2      # 1.354；几何中心在 ego 系的 x
# 画框与判定同口径（均不含后视镜），旧口径曾把含镜宽 2.297 用于画框。
EGO_BODY_WIDTH = EGO_WIDTH
# 压线只看车头 x=EGO_FRONT，车身中部仅擦到外缘不算（00001 弯道误报）。
# 车身半宽 0.926m 仍会把贴着外缘的线算进去：前视里这条线在引擎盖外侧。
# 阈值不按车身半宽等比缩放，而是换几何后在 12 个回归段上实测重标定
# （2026-09-22，scan_segment 的 min|d_nose|）：
#   必须检出：00528=0.858、00094=0.828、00171=0.591、00051=0.248、00012=0.077
#   必须不报：00013=0.950、00001=1.061
# -> 可行窗 [0.858, 0.950)，取最大余量解 0.90（与旧 Pacifica 口径同值；
#    等比缩放值 0.82 落在窗外，会丢掉 00528 与 00094 的压线）。
PRESS_HALF = 0.90
# 车头距短暂超出车身、但仍不超过此值时，视为同一次压线，避免穿越中途被拆开
# （不受上述可行窗约束；PRESS_HALF 未变故沿用旧值 1.25）
PRESS_LINK_HALF = 1.25

# ---------------- 渲染 ----------------
SPLIT = "train"
SEGMENT = "00000"
FPS = 2                                        # 数据约 2Hz，默认实时
LINE_WIDTH = 2                                 # 运行时 patch 官方 THICKNESS=4
CAMERAS = ["ring_front_center"]                # --copy-images 默认相机
N_POINTS = {                                   # collect 插值点数
    "area": 20,
    "centerline": 10,
    "left_laneline": 20,
    "right_laneline": 20,
}
WITH_SD_MAP = False                            # collect 是否读 sdmap.json（subset_A 无）
BEV_SCALE = 10                                 # 官方默认；运行时 patch ls_bev/cl_bev
BEV_RANGE = [-50, 50, -25, 25]                # 官方默认；画布 = 高 scale*(r1-r0) x 宽 scale*(r3-r2)
INTERP_POINTS = 1000                           # interp_arc 重采样点数（仅 _draw_line_fast 路径生效）
VIDEO_FOURCC = "mp4v"                          # cv2.VideoWriter 编码
# 自车叠加样式（draw_ego_vehicle，RGB 画布上绘制）
EGO_STYLE = {
    "fill": (255, 0, 0),                       # 车体填充（红）
    "outline": (0, 0, 0),                      # 车体描边（黑）
    "outline_width": 2,
    "arrow": (255, 255, 255),                  # 前向箭头（白）
    "arrow_width": 2,
    "arrow_tip_length": 0.3,
    "arrow_nose_margin": 0.1,                  # 箭头尖端距车头（米）
}
# 画面左上角时间戳烧字 t=X.Xs
TIME_OVERLAY = {
    "pos": (12, 32),
    "font_scale": 0.9,
    "outline_width": 4,                        # 黑色描边
    "text_width": 2,                           # 白色正文
}
# draw_annotation_bev 绘制开关（render_bev_video.py 视频渲染默认）
RENDER_DRAW = {
    "with_attribute": False,
    "with_linetype": True,
    "with_centerline": False,
    "with_laneline": True,
    "with_area": False,
}
# filter_driving_behavior.py 诊断图（render_flag_frame）绘制开关
FLAG_DRAW = {
    "with_attribute": True,
    "with_linetype": True,
    "with_centerline": True,
    "with_laneline": True,
    "with_area": True,
}

# ---------------- 行为检测（filter_driving_behavior.py） ----------------
FRAME_DT = 0.5                                 # 标称帧间隔（时段末尾 +0.5s 结束偏移）
SHORT_WINDOW_X = (-0.5, 2.0)                   # d 回退短窗口 x∈[x0,x1]；固定值，
                                               # 非车身派生量（换车型不调）
MERGE_ENDPOINT_TOL = 0.3                       # 物理线端点匹配容差（米）
SEAM_COS = 0.5                                 # 接缝方向一致阈值（cos>0.5 即夹角<60°）
DOUBLE_SEP = 0.5                               # 双线组平行间距（米）
DOUBLE_MIN_SEP = 0.03                          # 间距小于此 = 同一物理线的重合观测（共享边界），不是双线
DOUBLE_COS = 0.8                               # 双线组平行方向阈值
OCCUPY_FRAC = 0.5                              # 车道占有：新段与车体相交面积占比
RAMP_LATERAL = 1.5                             # 纵向后继但中心线横移>此值仍算占有（匝道）
LINE_DUP_TOL = 0.25                            # 双链判为同一物理线的 mean|Δd| 容差
BOUNDARY_OVERLAP_MIN = 1.0                     # left/right 跨侧拼接所需的最小重叠弧长（米），
                                               # 防导流鼻处不同物理线在节点收敛被误并
CENTER_EPS = 0.05                              # d 侧向符号有效证据容差（米）
SERIES_JUMP_MAX = 1.8                          # 时段相邻帧 d 最大跳变（米/帧；实测伪影跳变≥2.2，真实噪声≤1.7）
MIN_ONLINE_FRAMES = 2                          # 压线时段最少帧数（一蹭即离不算）
MAX_HOLE_FRAMES = 2                            # 非排除帧数据空洞桥接上限
DIRECTION_APPROACH_FRAMES = 2                  # 方向回退：进入前搜索 approach 符号的帧数
CROSSING_GAP_FRAMES = 4                        # 穿越前/后带外证据搜索帧数上限
OCCUPY_BACKCAP_FRAMES = 10                     # ref0 从时段起点回溯帧数上限
LANE_POLY_SAMPLES = 20                         # 车道多边形重采样点数
SPLITS = ["train", "val"]                      # 默认扫描 split（test 无标注）
SAMPLE_VIS = 4                                 # 每类行为抽样渲染帧数
SAMPLE_SEGMENTS = ["00012", "00040", "00051", "00094"]  # 抽样优先段

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

# ---------------- 自车（nuPlan Pacifica，米；原点=后轴中心） ----------------
EGO_REAR, EGO_FRONT, EGO_WIDTH = 1.127, 4.049, 2.297
PACIFICA = (EGO_REAR, EGO_FRONT, EGO_WIDTH)
EGO_HALF = EGO_WIDTH / 2                       # 车体半宽（压线判定阈值）
EGO_CENTER_X = (EGO_FRONT - EGO_REAR) / 2      # 几何中心在 ego 系的 x

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
SHORT_WINDOW_X = (-0.5, 2.0)                   # d 回退短窗口 x∈[x0,x1]
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

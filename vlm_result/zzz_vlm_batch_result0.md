# 蓝区压线变道VLM判定结果

样本：`00012`、`00030`、`00051`、`00094`  
模型：`qwen3.8-max`、`qwen3.7-plus`  
提示词：变道、压线  
轮数：3  

## 组合对比图

柱状图只展示本批次 48 组的实际耗时和推理 token。

![实际耗时总览](zzz_vlm_batch_charts/elapsed_overview.png)

![耗时对比](zzz_vlm_batch_charts/elapsed_grid.png)

![推理 token 对比](zzz_vlm_batch_charts/reasoning_grid.png)

## 48 组合对照表

| 模型 | 提示 | ID | 轮次 | 判定 | 事件 | 耗时 | 推理 token |
|---|---|---|---|---|---|---|---|
| qwen3.8-max | 变道 | 00012 | 1 | 是 | DASH / LEFT / 1.5–2.5s | 154.0s | 8465 |
| qwen3.8-max | 变道 | 00012 | 2 | 是 | DASH / LEFT / 1.0–3.0s | 101.9s | 5231 |
| qwen3.8-max | 变道 | 00012 | 3 | 是 | DASH / LEFT / 2.5–3.5s | 101.9s | 4956 |
| qwen3.8-max | 变道 | 00030 | 1 | 是 | DASH / RIGHT / 5.5–6.5s | 191.0s | 7936 |
| qwen3.8-max | 变道 | 00030 | 2 | 是 | DASH / RIGHT / 5.0–7.5s | 119.8s | 5560 |
| qwen3.8-max | 变道 | 00030 | 3 | 是 | DASH / RIGHT / 5.5–7.5s | 120.2s | 5577 |
| qwen3.8-max | 变道 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 10.5–12.0s | 120.4s | 5573 |
| qwen3.8-max | 变道 | 00051 | 2 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 133.2s | 6809 |
| qwen3.8-max | 变道 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 11.0–12.5s | 116.6s | 5382 |
| qwen3.8-max | 变道 | 00094 | 1 | 是 | DASH / RIGHT / 4.0–6.0s | 200.6s | 8360 |
| qwen3.8-max | 变道 | 00094 | 2 | 否 | — | 50.0s | 2190 |
| qwen3.8-max | 变道 | 00094 | 3 | 否 | — | 61.6s | 2532 |
| qwen3.8-max | 压线 | 00012 | 1 | 是 | DASH / LEFT / 1.5–2.5s | 208.9s | 9721 |
| qwen3.8-max | 压线 | 00012 | 2 | 是 | DASH / LEFT / 1.5–2.5s | 232.7s | 10943 |
| qwen3.8-max | 压线 | 00012 | 3 | 是 | DASH / LEFT / 2.0–3.0s | 78.5s | 3961 |
| qwen3.8-max | 压线 | 00030 | 1 | 是 | DASH / RIGHT / 5.0–6.0s | 248.9s | 10965 |
| qwen3.8-max | 压线 | 00030 | 2 | 是 | DASH / RIGHT / 5.5–6.5s | 220.0s | 9862 |
| qwen3.8-max | 压线 | 00030 | 3 | 是 | DASH / RIGHT / 5.5–6.0s | 229.4s | 7687 |
| qwen3.8-max | 压线 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 150.9s | 6533 |
| qwen3.8-max | 压线 | 00051 | 2 | 是 | DOUBLE_SOLID / LEFT / 11.0–12.5s | 121.0s | 5748 |
| qwen3.8-max | 压线 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 80.3s | 3424 |
| qwen3.8-max | 压线 | 00094 | 1 | 是 | SOLID / RIGHT / 5.0–6.0s；SOLID / LEFT / 7.5–9.0s | 225.5s | 10264 |
| qwen3.8-max | 压线 | 00094 | 2 | 是 | DASH / RIGHT / 4.5–6.5s | 128.7s | 6143 |
| qwen3.8-max | 压线 | 00094 | 3 | 是 | DASH / RIGHT / 4.0–7.0s | 205.9s | 9254 |
| qwen3.7-plus | 变道 | 00012 | 1 | 否 | — | 8.8s | 308 |
| qwen3.7-plus | 变道 | 00012 | 2 | 否 | — | 23.4s | 1177 |
| qwen3.7-plus | 变道 | 00012 | 3 | 否 | — | 9.0s | 309 |
| qwen3.7-plus | 变道 | 00030 | 1 | 否 | — | 12.2s | 500 |
| qwen3.7-plus | 变道 | 00030 | 2 | 否 | — | 14.7s | 705 |
| qwen3.7-plus | 变道 | 00030 | 3 | 是 | DASH / RIGHT / 5.0–7.5s | 79.5s | 4453 |
| qwen3.7-plus | 变道 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 10.0–12.5s | 15.2s | 634 |
| qwen3.7-plus | 变道 | 00051 | 2 | 否 | — | 8.4s | 342 |
| qwen3.7-plus | 变道 | 00051 | 3 | 否 | — | 7.2s | 280 |
| qwen3.7-plus | 变道 | 00094 | 1 | 否 | — | 24.2s | 1196 |
| qwen3.7-plus | 变道 | 00094 | 2 | 否 | — | 19.2s | 972 |
| qwen3.7-plus | 变道 | 00094 | 3 | 否 | — | 35.7s | 1949 |
| qwen3.7-plus | 压线 | 00012 | 1 | 否 | — | 42.9s | 2290 |
| qwen3.7-plus | 压线 | 00012 | 2 | 是 | DASH / LEFT / 2.0–4.0s | 60.7s | 3308 |
| qwen3.7-plus | 压线 | 00012 | 3 | 是 | DASH / LEFT / 0.0–4.0s | 84.2s | 4772 |
| qwen3.7-plus | 压线 | 00030 | 1 | 是 | DASH / RIGHT / 3.0–6.0s | 105.9s | 5937 |
| qwen3.7-plus | 压线 | 00030 | 2 | 是 | DOUBLE_SOLID / LEFT / 13.0–15.0s | 54.6s | 2764 |
| qwen3.7-plus | 压线 | 00030 | 3 | 是 | DASH / RIGHT / 5.5–7.0s | 94.1s | 5193 |
| qwen3.7-plus | 压线 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 11.0–13.0s | 68.7s | 3754 |
| qwen3.7-plus | 压线 | 00051 | 2 | 否 | — | 76.9s | 4389 |
| qwen3.7-plus | 压线 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 12.0–13.5s | 43.3s | 2318 |
| qwen3.7-plus | 压线 | 00094 | 1 | 否 | — | 137.3s | 7856 |
| qwen3.7-plus | 压线 | 00094 | 2 | 是 | SOLID / LEFT / 5.0–8.0s；SOLID / LEFT / 12.0–15.0s | 94.3s | 5299 |
| qwen3.7-plus | 压线 | 00094 | 3 | 是 | CURB / RIGHT / 8.0–10.0s；DOUBLE_SOLID / LEFT / 10.0–15.0s | 121.8s | 6927 |

## 总览

| 模型 | 轮次 | ID | 压线 | 压线事件 | 变道 | 变道事件 | 结论是否一致 |
|---|---|---|---|---|---|---|---|
| qwen3.7-plus | 1 | 00012 | 否 | — | 否 | — | 一致 |
| qwen3.7-plus | 1 | 00030 | 是 | DASH / RIGHT / 3.0–6.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 1 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.0–13.0s | 是 | DOUBLE_SOLID / LEFT / 10.0–12.5s | 一致（时段略有差异） |
| qwen3.7-plus | 1 | 00094 | 否 | — | 否 | — | 一致 |
| qwen3.7-plus | 2 | 00012 | 是 | DASH / LEFT / 2.0–4.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 2 | 00030 | 是 | DOUBLE_SOLID / LEFT / 13.0–15.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 2 | 00051 | 否 | — | 否 | — | 一致 |
| qwen3.7-plus | 2 | 00094 | 是 | SOLID / LEFT / 5.0–8.0s；SOLID / LEFT / 12.0–15.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 3 | 00012 | 是 | DASH / LEFT / 0.0–4.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 3 | 00030 | 是 | DASH / RIGHT / 5.5–7.0s | 是 | DASH / RIGHT / 5.0–7.5s | 一致（时段略有差异） |
| qwen3.7-plus | 3 | 00051 | 是 | DOUBLE_SOLID / LEFT / 12.0–13.5s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 3 | 00094 | 是 | CURB / RIGHT / 8.0–10.0s；DOUBLE_SOLID / LEFT / 10.0–15.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.8-max | 1 | 00012 | 是 | DASH / LEFT / 1.5–2.5s | 是 | DASH / LEFT / 1.5–2.5s | 一致 |
| qwen3.8-max | 1 | 00030 | 是 | DASH / RIGHT / 5.0–6.0s | 是 | DASH / RIGHT / 5.5–6.5s | 一致（时段略有差异） |
| qwen3.8-max | 1 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 是 | DOUBLE_SOLID / LEFT / 10.5–12.0s | 一致（时段略有差异） |
| qwen3.8-max | 1 | 00094 | 是 | SOLID / RIGHT / 5.0–6.0s；SOLID / LEFT / 7.5–9.0s | 是 | DASH / RIGHT / 4.0–6.0s | 部分一致（线型或方向不同） |
| qwen3.8-max | 2 | 00012 | 是 | DASH / LEFT / 1.5–2.5s | 是 | DASH / LEFT / 1.0–3.0s | 一致（时段略有差异） |
| qwen3.8-max | 2 | 00030 | 是 | DASH / RIGHT / 5.5–6.5s | 是 | DASH / RIGHT / 5.0–7.5s | 一致（时段略有差异） |
| qwen3.8-max | 2 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.0–12.5s | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 一致 |
| qwen3.8-max | 2 | 00094 | 是 | DASH / RIGHT / 4.5–6.5s | 否 | — | 一致（仅压线未变道） |
| qwen3.8-max | 3 | 00012 | 是 | DASH / LEFT / 2.0–3.0s | 是 | DASH / LEFT / 2.5–3.5s | 一致（时段略有差异） |
| qwen3.8-max | 3 | 00030 | 是 | DASH / RIGHT / 5.5–6.0s | 是 | DASH / RIGHT / 5.5–7.5s | 一致（时段略有差异） |
| qwen3.8-max | 3 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 是 | DOUBLE_SOLID / LEFT / 11.0–12.5s | 一致 |
| qwen3.8-max | 3 | 00094 | 是 | DASH / RIGHT / 4.0–7.0s | 否 | — | 一致（仅压线未变道） |

## 压线明细

| 模型 | 轮次 | ID | is_online | 事件 | 耗时 | 推理 token | 输出文本 token |
|---|---|---|---|---|---|---|---|
| qwen3.8-max | 1 | 00012 | True | DASH / LEFT / 1.5–2.5s | 208.9s | 9721 | 58 |
| qwen3.8-max | 2 | 00012 | True | DASH / LEFT / 1.5–2.5s | 232.7s | 10943 | 57 |
| qwen3.8-max | 3 | 00012 | True | DASH / LEFT / 2.0–3.0s | 78.5s | 3961 | 58 |
| qwen3.8-max | 1 | 00030 | True | DASH / RIGHT / 5.0–6.0s | 248.9s | 10965 | 58 |
| qwen3.8-max | 2 | 00030 | True | DASH / RIGHT / 5.5–6.5s | 220.0s | 9862 | 57 |
| qwen3.8-max | 3 | 00030 | True | DASH / RIGHT / 5.5–6.0s | 229.4s | 7687 | 57 |
| qwen3.8-max | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–12.5s | 150.9s | 6533 | 60 |
| qwen3.8-max | 2 | 00051 | True | DOUBLE_SOLID / LEFT / 11.0–12.5s | 121.0s | 5748 | 60 |
| qwen3.8-max | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–12.5s | 80.3s | 3424 | 60 |
| qwen3.8-max | 1 | 00094 | True | SOLID / RIGHT / 5.0–6.0s；SOLID / LEFT / 7.5–9.0s | 225.5s | 10264 | 92 |
| qwen3.8-max | 2 | 00094 | True | DASH / RIGHT / 4.5–6.5s | 128.7s | 6143 | 57 |
| qwen3.8-max | 3 | 00094 | True | DASH / RIGHT / 4.0–7.0s | 205.9s | 9254 | 57 |
| qwen3.7-plus | 1 | 00012 | False | — | 42.9s | 2290 | 26 |
| qwen3.7-plus | 2 | 00012 | True | DASH / LEFT / 2.0–4.0s | 60.7s | 3308 | 74 |
| qwen3.7-plus | 3 | 00012 | True | DASH / LEFT / 0.0–4.0s | 84.2s | 4772 | 74 |
| qwen3.7-plus | 1 | 00030 | True | DASH / RIGHT / 3.0–6.0s | 105.9s | 5937 | 74 |
| qwen3.7-plus | 2 | 00030 | True | DOUBLE_SOLID / LEFT / 13.0–15.0s | 54.6s | 2764 | 77 |
| qwen3.7-plus | 3 | 00030 | True | DASH / RIGHT / 5.5–7.0s | 94.1s | 5193 | 74 |
| qwen3.7-plus | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 11.0–13.0s | 68.7s | 3754 | 77 |
| qwen3.7-plus | 2 | 00051 | False | — | 76.9s | 4389 | 26 |
| qwen3.7-plus | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 12.0–13.5s | 43.3s | 2318 | 77 |
| qwen3.7-plus | 1 | 00094 | False | — | 137.3s | 7856 | 26 |
| qwen3.7-plus | 2 | 00094 | True | SOLID / LEFT / 5.0–8.0s；SOLID / LEFT / 12.0–15.0s | 94.3s | 5299 | 121 |
| qwen3.7-plus | 3 | 00094 | True | CURB / RIGHT / 8.0–10.0s；DOUBLE_SOLID / LEFT / 10.0–15.0s | 121.8s | 6927 | 123 |

## 变道明细

| 模型 | 轮次 | ID | is_lanechange | 事件 | 耗时 | 推理 token | 输出文本 token |
|---|---|---|---|---|---|---|---|
| qwen3.8-max | 1 | 00012 | True | DASH / LEFT / 1.5–2.5s | 154.0s | 8465 | 59 |
| qwen3.8-max | 2 | 00012 | True | DASH / LEFT / 1.0–3.0s | 101.9s | 5231 | 59 |
| qwen3.8-max | 3 | 00012 | True | DASH / LEFT / 2.5–3.5s | 101.9s | 4956 | 59 |
| qwen3.8-max | 1 | 00030 | True | DASH / RIGHT / 5.5–6.5s | 191.0s | 7936 | 58 |
| qwen3.8-max | 2 | 00030 | True | DASH / RIGHT / 5.0–7.5s | 119.8s | 5560 | 59 |
| qwen3.8-max | 3 | 00030 | True | DASH / RIGHT / 5.5–7.5s | 120.2s | 5577 | 59 |
| qwen3.8-max | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 10.5–12.0s | 120.4s | 5573 | 62 |
| qwen3.8-max | 2 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–12.5s | 133.2s | 6809 | 62 |
| qwen3.8-max | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 11.0–12.5s | 116.6s | 5382 | 61 |
| qwen3.8-max | 1 | 00094 | True | DASH / RIGHT / 4.0–6.0s | 200.6s | 8360 | 59 |
| qwen3.8-max | 2 | 00094 | False | — | 50.0s | 2190 | 22 |
| qwen3.8-max | 3 | 00094 | False | — | 61.6s | 2532 | 22 |
| qwen3.7-plus | 1 | 00012 | False | — | 8.8s | 308 | 27 |
| qwen3.7-plus | 2 | 00012 | False | — | 23.4s | 1177 | 27 |
| qwen3.7-plus | 3 | 00012 | False | — | 9.0s | 309 | 27 |
| qwen3.7-plus | 1 | 00030 | False | — | 12.2s | 500 | 26 |
| qwen3.7-plus | 2 | 00030 | False | — | 14.7s | 705 | 27 |
| qwen3.7-plus | 3 | 00030 | True | DASH / RIGHT / 5.0–7.5s | 79.5s | 4453 | 75 |
| qwen3.7-plus | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 10.0–12.5s | 15.2s | 634 | 78 |
| qwen3.7-plus | 2 | 00051 | False | — | 8.4s | 342 | 27 |
| qwen3.7-plus | 3 | 00051 | False | — | 7.2s | 280 | 27 |
| qwen3.7-plus | 1 | 00094 | False | — | 24.2s | 1196 | 26 |
| qwen3.7-plus | 2 | 00094 | False | — | 19.2s | 972 | 27 |
| qwen3.7-plus | 3 | 00094 | False | — | 35.7s | 1949 | 27 |

## 耗时与 token

| 模型 | 轮次 | ID | 压线耗时 | 变道耗时 | 压线 total | 变道 total | 压线 cached | 变道 cached |
|---|---|---|---|---|---|---|---|---|
| qwen3.7-plus | 1 | 00012 | 42.9s | 8.8s | 14218 | 12453 | 0 | 0 |
| qwen3.7-plus | 1 | 00030 | 105.9s | 12.2s | 17913 | 12644 | 0 | 0 |
| qwen3.7-plus | 1 | 00051 | 68.7s | 15.2s | 15733 | 12830 | 0 | 0 |
| qwen3.7-plus | 1 | 00094 | 137.3s | 24.2s | 19784 | 13340 | 0 | 0 |
| qwen3.7-plus | 2 | 00012 | 60.7s | 23.4s | 15284 | 13322 | 11520 | 11520 |
| qwen3.7-plus | 2 | 00030 | 54.6s | 14.7s | 14743 | 12850 | 0 | 11520 |
| qwen3.7-plus | 2 | 00051 | 76.9s | 8.4s | 16317 | 12487 | 11520 | 11520 |
| qwen3.7-plus | 2 | 00094 | 94.3s | 19.2s | 17322 | 13117 | 0 | 11520 |
| qwen3.7-plus | 3 | 00012 | 84.2s | 9.0s | 16748 | 12454 | 11520 | 11520 |
| qwen3.7-plus | 3 | 00030 | 94.1s | 79.5s | 17169 | 16646 | 0 | 11520 |
| qwen3.7-plus | 3 | 00051 | 43.3s | 7.2s | 14297 | 12425 | 11520 | 11520 |
| qwen3.7-plus | 3 | 00094 | 121.8s | 35.7s | 18952 | 14094 | 11520 | 11520 |
| qwen3.8-max | 1 | 00012 | 208.9s | 154.0s | 21826 | 20787 | 10240 | 10240 |
| qwen3.8-max | 1 | 00030 | 248.9s | 191.0s | 23070 | 20257 | 10240 | 10240 |
| qwen3.8-max | 1 | 00051 | 150.9s | 120.4s | 18640 | 17898 | 10240 | 0 |
| qwen3.8-max | 1 | 00094 | 225.5s | 200.6s | 22403 | 20682 | 10240 | 0 |
| qwen3.8-max | 2 | 00012 | 232.7s | 101.9s | 23047 | 17553 | 11520 | 11520 |
| qwen3.8-max | 2 | 00030 | 220.0s | 119.8s | 21966 | 17882 | 11520 | 11520 |
| qwen3.8-max | 2 | 00051 | 121.0s | 133.2s | 17855 | 19134 | 11520 | 11520 |
| qwen3.8-max | 2 | 00094 | 128.7s | 50.0s | 18247 | 14475 | 11520 | 11520 |
| qwen3.8-max | 3 | 00012 | 78.5s | 101.9s | 16066 | 17278 | 11520 | 11520 |
| qwen3.8-max | 3 | 00030 | 229.4s | 120.2s | 19791 | 17899 | 11520 | 11520 |
| qwen3.8-max | 3 | 00051 | 80.3s | 116.6s | 15531 | 17706 | 11520 | 11520 |
| qwen3.8-max | 3 | 00094 | 205.9s | 61.6s | 21358 | 14817 | 11520 | 11520 |
| **合计** | — | — | **3115.5s** | **1728.8s** | — | — | — | — |
| **平均** | — | — | **129.8s** | **72.0s** | — | — | — | — |

## 对照备注

1. **qwen3.7-plus / r1 / 00012**：压线 —；变道 —；一致。
2. **qwen3.7-plus / r1 / 00030**：压线 DASH / RIGHT / 3.0–6.0s；变道 —；一致（仅压线未变道）。
3. **qwen3.7-plus / r1 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.0–13.0s；变道 DOUBLE_SOLID / LEFT / 10.0–12.5s；一致（时段略有差异）。
4. **qwen3.7-plus / r1 / 00094**：压线 —；变道 —；一致。
5. **qwen3.7-plus / r2 / 00012**：压线 DASH / LEFT / 2.0–4.0s；变道 —；一致（仅压线未变道）。
6. **qwen3.7-plus / r2 / 00030**：压线 DOUBLE_SOLID / LEFT / 13.0–15.0s；变道 —；一致（仅压线未变道）。
7. **qwen3.7-plus / r2 / 00051**：压线 —；变道 —；一致。
8. **qwen3.7-plus / r2 / 00094**：压线 SOLID / LEFT / 5.0–8.0s；SOLID / LEFT / 12.0–15.0s；变道 —；一致（仅压线未变道）。
9. **qwen3.7-plus / r3 / 00012**：压线 DASH / LEFT / 0.0–4.0s；变道 —；一致（仅压线未变道）。
10. **qwen3.7-plus / r3 / 00030**：压线 DASH / RIGHT / 5.5–7.0s；变道 DASH / RIGHT / 5.0–7.5s；一致（时段略有差异）。
11. **qwen3.7-plus / r3 / 00051**：压线 DOUBLE_SOLID / LEFT / 12.0–13.5s；变道 —；一致（仅压线未变道）。
12. **qwen3.7-plus / r3 / 00094**：压线 CURB / RIGHT / 8.0–10.0s；DOUBLE_SOLID / LEFT / 10.0–15.0s；变道 —；一致（仅压线未变道）。
13. **qwen3.8-max / r1 / 00012**：压线 DASH / LEFT / 1.5–2.5s；变道 DASH / LEFT / 1.5–2.5s；一致。
14. **qwen3.8-max / r1 / 00030**：压线 DASH / RIGHT / 5.0–6.0s；变道 DASH / RIGHT / 5.5–6.5s；一致（时段略有差异）。
15. **qwen3.8-max / r1 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.5–12.5s；变道 DOUBLE_SOLID / LEFT / 10.5–12.0s；一致（时段略有差异）。
16. **qwen3.8-max / r1 / 00094**：压线 SOLID / RIGHT / 5.0–6.0s；SOLID / LEFT / 7.5–9.0s；变道 DASH / RIGHT / 4.0–6.0s；部分一致（线型或方向不同）。
17. **qwen3.8-max / r2 / 00012**：压线 DASH / LEFT / 1.5–2.5s；变道 DASH / LEFT / 1.0–3.0s；一致（时段略有差异）。
18. **qwen3.8-max / r2 / 00030**：压线 DASH / RIGHT / 5.5–6.5s；变道 DASH / RIGHT / 5.0–7.5s；一致（时段略有差异）。
19. **qwen3.8-max / r2 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.0–12.5s；变道 DOUBLE_SOLID / LEFT / 11.5–12.5s；一致。
20. **qwen3.8-max / r2 / 00094**：压线 DASH / RIGHT / 4.5–6.5s；变道 —；一致（仅压线未变道）。
21. **qwen3.8-max / r3 / 00012**：压线 DASH / LEFT / 2.0–3.0s；变道 DASH / LEFT / 2.5–3.5s；一致（时段略有差异）。
22. **qwen3.8-max / r3 / 00030**：压线 DASH / RIGHT / 5.5–6.0s；变道 DASH / RIGHT / 5.5–7.5s；一致（时段略有差异）。
23. **qwen3.8-max / r3 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.5–12.5s；变道 DOUBLE_SOLID / LEFT / 11.0–12.5s；一致。
24. **qwen3.8-max / r3 / 00094**：压线 DASH / RIGHT / 4.0–7.0s；变道 —；一致（仅压线未变道）。

# 详细结果

# 变道_00012_qwen3.8-max_r1

## 耗时
154.0s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 8525, 'prompt_tokens': 12262, 'total_tokens': 20787, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 8465, 'rejected_prediction_tokens': None, 'text_tokens': 59}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 10240, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-833a783b-427a-997a-bd6e-00d67e5a9b0d', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "LEFT", "start_time": 1.5, "end_time": 2.5}
  ]
}

# 变道_00012_qwen3.8-max_r2

## 耗时
101.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5291, 'prompt_tokens': 12262, 'total_tokens': 17553, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5231, 'rejected_prediction_tokens': None, 'text_tokens': 59}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-600b5f85-8435-9171-972d-d5ae1a77a1af', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "LEFT", "start_time": 1.0, "end_time": 3.0}
  ]
}

# 变道_00012_qwen3.8-max_r3

## 耗时
101.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5016, 'prompt_tokens': 12262, 'total_tokens': 17278, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 4956, 'rejected_prediction_tokens': None, 'text_tokens': 59}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-a18604f1-bf8e-92f5-b125-1719ca851ee6', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "LEFT", "start_time": 2.5, "end_time": 3.5}
  ]
}

# 变道_00030_qwen3.8-max_r1

## 耗时
191.0s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 7995, 'prompt_tokens': 12262, 'total_tokens': 20257, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 7936, 'rejected_prediction_tokens': None, 'text_tokens': 58}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 10240, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-50c944b6-df0b-9844-baea-57c3c7f6d932', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 5.5, "end_time": 6.5}
  ]
}

# 变道_00030_qwen3.8-max_r2

## 耗时
119.8s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5620, 'prompt_tokens': 12262, 'total_tokens': 17882, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5560, 'rejected_prediction_tokens': None, 'text_tokens': 59}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-e175295c-5bbe-96e2-9b05-42c7038a1172', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 5.0, "end_time": 7.5}
  ]
}

# 变道_00030_qwen3.8-max_r3

## 耗时
120.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5637, 'prompt_tokens': 12262, 'total_tokens': 17899, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5577, 'rejected_prediction_tokens': None, 'text_tokens': 59}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-c06587b1-7618-9a44-9323-e3ca0ed14f9f', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 5.5, "end_time": 7.5}
  ]
}

# 变道_00051_qwen3.8-max_r1

## 耗时
120.4s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5636, 'prompt_tokens': 12262, 'total_tokens': 17898, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5573, 'rejected_prediction_tokens': None, 'text_tokens': 62}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-8d63cca1-09b7-9fd3-9edf-54ec362a7d04', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 10.5, "end_time": 12.0}
  ]
}

# 变道_00051_qwen3.8-max_r2

## 耗时
133.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 6872, 'prompt_tokens': 12262, 'total_tokens': 19134, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 6809, 'rejected_prediction_tokens': None, 'text_tokens': 62}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-5c9775b7-38c8-9733-b0e7-b98213ed5e1c', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 11.5, "end_time": 12.5}
  ]
}

# 变道_00051_qwen3.8-max_r3

## 耗时
116.6s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5444, 'prompt_tokens': 12262, 'total_tokens': 17706, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5382, 'rejected_prediction_tokens': None, 'text_tokens': 61}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-fc6a2d78-d41f-9b02-a5fc-13220a5a45bb', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 11.0, "end_time": 12.5}
  ]
}

# 变道_00094_qwen3.8-max_r1

## 耗时
200.6s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 8420, 'prompt_tokens': 12262, 'total_tokens': 20682, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 8360, 'rejected_prediction_tokens': None, 'text_tokens': 59}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-5c7cff5b-8dc5-983d-9f4d-fdef05dbd68e', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 4.0, "end_time": 6.0}
  ]
}

# 变道_00094_qwen3.8-max_r2

## 耗时
50.0s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 2213, 'prompt_tokens': 12262, 'total_tokens': 14475, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 2190, 'rejected_prediction_tokens': None, 'text_tokens': 22}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-de1fdcae-32e4-9b25-9e0e-5c5fe3ce6d5f', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": false,
  "line_events": []
}

# 变道_00094_qwen3.8-max_r3

## 耗时
61.6s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 2555, 'prompt_tokens': 12262, 'total_tokens': 14817, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 2532, 'rejected_prediction_tokens': None, 'text_tokens': 22}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1920, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-6982fda1-c01c-9635-b028-7d203ede47b7', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_lanechange": false,
  "line_events": []
}

# 压线_00012_qwen3.8-max_r1

## 耗时
208.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 9780, 'prompt_tokens': 12046, 'total_tokens': 21826, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 9721, 'rejected_prediction_tokens': None, 'text_tokens': 58}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 10240, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-faa3b587-50ea-9cc0-a924-cdcb52972572', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "LEFT", "start_time": 1.5, "end_time": 2.5}
  ]
}

# 压线_00012_qwen3.8-max_r2

## 耗时
232.7s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 11001, 'prompt_tokens': 12046, 'total_tokens': 23047, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 10943, 'rejected_prediction_tokens': None, 'text_tokens': 57}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-83c9d181-66eb-9df0-809a-9dd8dc89e323', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "LEFT", "start_time": 1.5, "end_time": 2.5}
  ]
}

# 压线_00012_qwen3.8-max_r3

## 耗时
78.5s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 4020, 'prompt_tokens': 12046, 'total_tokens': 16066, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 3961, 'rejected_prediction_tokens': None, 'text_tokens': 58}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-f407bec0-8b15-9dbd-82e4-a6dc7ea8eb50', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "LEFT", "start_time": 2.0, "end_time": 3.0}
  ]
}

# 压线_00030_qwen3.8-max_r1

## 耗时
248.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 11024, 'prompt_tokens': 12046, 'total_tokens': 23070, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 10965, 'rejected_prediction_tokens': None, 'text_tokens': 58}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 10240, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-354ff787-209a-9250-9164-c93b288dbaac', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 5.0, "end_time": 6.0}
  ]
}

# 压线_00030_qwen3.8-max_r2

## 耗时
220.0s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 9920, 'prompt_tokens': 12046, 'total_tokens': 21966, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 9862, 'rejected_prediction_tokens': None, 'text_tokens': 57}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-7db139fe-eabf-95a7-b6da-b71fdc6a3d5a', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 5.5, "end_time": 6.5}
  ]
}

# 压线_00030_qwen3.8-max_r3

## 耗时
229.4s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 7745, 'prompt_tokens': 12046, 'total_tokens': 19791, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 7687, 'rejected_prediction_tokens': None, 'text_tokens': 57}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-9fa4803f-3674-9fef-8b8e-69b8f9786c28', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 5.5, "end_time": 6.0}
  ]
}

# 压线_00051_qwen3.8-max_r1

## 耗时
150.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 6594, 'prompt_tokens': 12046, 'total_tokens': 18640, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 6533, 'rejected_prediction_tokens': None, 'text_tokens': 60}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 10240, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-58eb5efc-c4cc-96c7-a510-c814e27a7294', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 11.5, "end_time": 12.5}
  ]
}

# 压线_00051_qwen3.8-max_r2

## 耗时
121.0s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5809, 'prompt_tokens': 12046, 'total_tokens': 17855, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5748, 'rejected_prediction_tokens': None, 'text_tokens': 60}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-9547ff82-a0d8-9fc5-bdd9-44b252a04220', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 11.0, "end_time": 12.5}
  ]
}

# 压线_00051_qwen3.8-max_r3

## 耗时
80.3s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 3485, 'prompt_tokens': 12046, 'total_tokens': 15531, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 3424, 'rejected_prediction_tokens': None, 'text_tokens': 60}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-4ea07b89-a84d-9de5-a021-fdd993d7908e', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 11.5, "end_time": 12.5}
  ]
}

# 压线_00094_qwen3.8-max_r1

## 耗时
225.5s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 10357, 'prompt_tokens': 12046, 'total_tokens': 22403, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 10264, 'rejected_prediction_tokens': None, 'text_tokens': 92}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 10240, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-6cb41da1-a44c-960a-9b7f-84d9a1611c62', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "SOLID", "direction": "RIGHT", "start_time": 5.0, "end_time": 6.0},
    {"line_type": "SOLID", "direction": "LEFT", "start_time": 7.5, "end_time": 9.0}
  ]
}

# 压线_00094_qwen3.8-max_r2

## 耗时
128.7s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 6201, 'prompt_tokens': 12046, 'total_tokens': 18247, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 6143, 'rejected_prediction_tokens': None, 'text_tokens': 57}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-fb7563a9-fd89-9bcc-9315-df1029a21b7a', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 4.5, "end_time": 6.5}
  ]
}

# 压线_00094_qwen3.8-max_r3

## 耗时
205.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 9312, 'prompt_tokens': 12046, 'total_tokens': 21358, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 9254, 'rejected_prediction_tokens': None, 'text_tokens': 57}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'text_tokens': 1704, 'video_tokens': 10342}}, 'model_provider': 'openai', 'model_name': 'qwen3.8-max', 'system_fingerprint': None, 'id': 'chatcmpl-efcb7f27-501c-931a-854e-f7c364738430', 'finish_reason': 'stop', 'logprobs': None}
## 结果
{
  "is_online": true,
  "line_events": [
    {"line_type": "DASH", "direction": "RIGHT", "start_time": 4.0, "end_time": 7.0}
  ]
}

# 变道_00012_qwen3.7-plus_r1

## 耗时
8.8s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 336, 'prompt_tokens': 12117, 'total_tokens': 12453, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 308, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-4fc2f872-bea2-9339-9fed-72ae93a1db4a', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00012_qwen3.7-plus_r2

## 耗时
23.4s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 1205, 'prompt_tokens': 12117, 'total_tokens': 13322, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 1177, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-cf3228a8-18c5-941f-b344-324d1cac9ee5', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00012_qwen3.7-plus_r3

## 耗时
9.0s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 337, 'prompt_tokens': 12117, 'total_tokens': 12454, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 309, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-a2ef0734-20c8-90c7-b608-d4f01efcf27d', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00030_qwen3.7-plus_r1

## 耗时
12.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 527, 'prompt_tokens': 12117, 'total_tokens': 12644, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 500, 'rejected_prediction_tokens': None, 'text_tokens': 26}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-488eb831-915f-92eb-aa2d-f68c100c555d', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00030_qwen3.7-plus_r2

## 耗时
14.7s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 733, 'prompt_tokens': 12117, 'total_tokens': 12850, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 705, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-b247eae4-6528-943b-87f6-7354e3b12d2c', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00030_qwen3.7-plus_r3

## 耗时
79.5s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 4529, 'prompt_tokens': 12117, 'total_tokens': 16646, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 4453, 'rejected_prediction_tokens': None, 'text_tokens': 75}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-72d7821a-32ea-9094-9427-2a67726d6459', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.0,
      "end_time": 7.5
    }
  ]
}
```

# 变道_00051_qwen3.7-plus_r1

## 耗时
15.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 713, 'prompt_tokens': 12117, 'total_tokens': 12830, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 634, 'rejected_prediction_tokens': None, 'text_tokens': 78}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-86320827-7c76-9029-aa67-efed9e87f45d', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 10.0,
      "end_time": 12.5
    }
  ]
}
```

# 变道_00051_qwen3.7-plus_r2

## 耗时
8.4s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 370, 'prompt_tokens': 12117, 'total_tokens': 12487, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 342, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-34827587-9b6e-9bae-b7af-c926e9c81f88', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00051_qwen3.7-plus_r3

## 耗时
7.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 308, 'prompt_tokens': 12117, 'total_tokens': 12425, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 280, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-78e488c1-e593-9064-8973-1112582ded84', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00094_qwen3.7-plus_r1

## 耗时
24.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 1223, 'prompt_tokens': 12117, 'total_tokens': 13340, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 1196, 'rejected_prediction_tokens': None, 'text_tokens': 26}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-fcd44966-5d92-994b-a287-235c9b0e1ec5', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00094_qwen3.7-plus_r2

## 耗时
19.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 1000, 'prompt_tokens': 12117, 'total_tokens': 13117, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 972, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-5214412a-702a-9821-a19e-4d48e0f37913', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00094_qwen3.7-plus_r3

## 耗时
35.7s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 1977, 'prompt_tokens': 12117, 'total_tokens': 14094, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 1949, 'rejected_prediction_tokens': None, 'text_tokens': 27}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1907}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-9757450e-40db-92e2-8030-4fe4fedd0315', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 压线_00012_qwen3.7-plus_r1

## 耗时
42.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 2317, 'prompt_tokens': 11901, 'total_tokens': 14218, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 2290, 'rejected_prediction_tokens': None, 'text_tokens': 26}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-af09d791-c673-95fe-a883-3dc59273f4df', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": false,
  "line_events": []
}
```

# 压线_00012_qwen3.7-plus_r2

## 耗时
60.7s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 3383, 'prompt_tokens': 11901, 'total_tokens': 15284, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 3308, 'rejected_prediction_tokens': None, 'text_tokens': 74}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-2c8e3c56-a48c-92dd-b108-c8e307d81f06', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 2.0,
      "end_time": 4.0
    }
  ]
}
```

# 压线_00012_qwen3.7-plus_r3

## 耗时
84.2s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 4847, 'prompt_tokens': 11901, 'total_tokens': 16748, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 4772, 'rejected_prediction_tokens': None, 'text_tokens': 74}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-9a4ab895-65ff-979d-a4f4-2e5907eb26aa', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 0.0,
      "end_time": 4.0
    }
  ]
}
```

# 压线_00030_qwen3.7-plus_r1

## 耗时
105.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 6012, 'prompt_tokens': 11901, 'total_tokens': 17913, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5937, 'rejected_prediction_tokens': None, 'text_tokens': 74}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-ae5d43bd-5b55-9166-bc07-89c1a7db4cca', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 3.0,
      "end_time": 6.0
    }
  ]
}
```

# 压线_00030_qwen3.7-plus_r2

## 耗时
54.6s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 2842, 'prompt_tokens': 11901, 'total_tokens': 14743, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 2764, 'rejected_prediction_tokens': None, 'text_tokens': 77}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-240a9621-ee31-9ba5-a7c6-6dc84549ed8f', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 13.0,
      "end_time": 15.0
    }
  ]
}
```

# 压线_00030_qwen3.7-plus_r3

## 耗时
94.1s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5268, 'prompt_tokens': 11901, 'total_tokens': 17169, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5193, 'rejected_prediction_tokens': None, 'text_tokens': 74}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-6930d7fe-2ba4-9fa4-bfe5-f02fb9991af9', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.5,
      "end_time": 7.0
    }
  ]
}
```

# 压线_00051_qwen3.7-plus_r1

## 耗时
68.7s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 3832, 'prompt_tokens': 11901, 'total_tokens': 15733, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 3754, 'rejected_prediction_tokens': None, 'text_tokens': 77}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-862e87c5-fda1-902e-8533-cce297a4e0b3', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 11.0,
      "end_time": 13.0
    }
  ]
}
```

# 压线_00051_qwen3.7-plus_r2

## 耗时
76.9s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 4416, 'prompt_tokens': 11901, 'total_tokens': 16317, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 4389, 'rejected_prediction_tokens': None, 'text_tokens': 26}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-95de0c76-7abe-9a19-a6e5-49ea8269a54d', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": false,
  "line_events": []
}
```

# 压线_00051_qwen3.7-plus_r3

## 耗时
43.3s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 2396, 'prompt_tokens': 11901, 'total_tokens': 14297, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 2318, 'rejected_prediction_tokens': None, 'text_tokens': 77}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-20fdef53-1f44-9e5a-a5f7-0600ccf1d899', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 12.0,
      "end_time": 13.5
    }
  ]
}
```

# 压线_00094_qwen3.7-plus_r1

## 耗时
137.3s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 7883, 'prompt_tokens': 11901, 'total_tokens': 19784, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 7856, 'rejected_prediction_tokens': None, 'text_tokens': 26}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-b2c764a1-4383-95ed-bce9-005c0c542966', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": false,
  "line_events": []
}
```

# 压线_00094_qwen3.7-plus_r2

## 耗时
94.3s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 5421, 'prompt_tokens': 11901, 'total_tokens': 17322, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 5299, 'rejected_prediction_tokens': None, 'text_tokens': 121}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-b3f4be12-f891-96e8-abab-cae92928498d', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "SOLID",
      "direction": "LEFT",
      "start_time": 5.0,
      "end_time": 8.0
    },
    {
      "line_type": "SOLID",
      "direction": "LEFT",
      "start_time": 12.0,
      "end_time": 15.0
    }
  ]
}
```

# 压线_00094_qwen3.7-plus_r3

## 耗时
121.8s
## 响应
response_metadata：{'token_usage': {'completion_tokens': 7051, 'prompt_tokens': 11901, 'total_tokens': 18952, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 6927, 'rejected_prediction_tokens': None, 'text_tokens': 123}, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 11520, 'video_tokens': 10210, 'text_tokens': 1691}}, 'model_provider': 'openai', 'model_name': 'qwen3.7-plus', 'system_fingerprint': None, 'id': 'chatcmpl-512fbae2-ac69-93fc-820f-f0328f3eb703', 'finish_reason': 'stop', 'logprobs': None}
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "CURB",
      "direction": "RIGHT",
      "start_time": 8.0,
      "end_time": 10.0
    },
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 10.0,
      "end_time": 15.0
    }
  ]
}
```

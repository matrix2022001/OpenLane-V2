# 蓝区压线变道VLM判定结果

样本：`00012`、`00030`、`00051`、`00094`  
模型：`qwen3.8-max`、`qwen3.7-plus`  
提示词：变道、压线  
轮数：3  
进度：48/48

## 组合对比图

柱状图只展示本批次 48 组的实际耗时和推理 token。

![实际耗时总览](zzz_vlm_batch_charts/elapsed_overview.png)

![耗时对比](zzz_vlm_batch_charts/elapsed_grid.png)

![推理 token 对比](zzz_vlm_batch_charts/reasoning_grid.png)

## 48 组合对照表

| 模型 | 提示 | ID | 轮次 | 判定 | 事件 | 耗时 | 推理 token |
|---|---|---|---|---|---|---|---|
| qwen3.8-max | 变道 | 00012 | 1 | 是 | DASH / LEFT / 1.5–2.5s | 159.0s | 7827 |
| qwen3.8-max | 变道 | 00012 | 2 | 是 | DASH / LEFT / 2.0–3.0s | 137.8s | 6439 |
| qwen3.8-max | 变道 | 00012 | 3 | 是 | DASH / LEFT / 2.0–3.0s | 100.3s | 5570 |
| qwen3.8-max | 变道 | 00030 | 1 | 是 | DASH / RIGHT / 5.5–6.5s | 195.2s | 9530 |
| qwen3.8-max | 变道 | 00030 | 2 | 是 | DASH / RIGHT / 6.0–8.0s | 120.1s | 6481 |
| qwen3.8-max | 变道 | 00030 | 3 | 是 | DASH / RIGHT / 6.0–8.0s | 134.4s | 7144 |
| qwen3.8-max | 变道 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.0s | 195.5s | 7268 |
| qwen3.8-max | 变道 | 00051 | 2 | — | — | 124.7s | 5897 |
| qwen3.8-max | 变道 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 10.5–12.0s | 93.4s | 4650 |
| qwen3.8-max | 变道 | 00094 | 1 | 是 | DASH / RIGHT / 5.0–7.0s | 195.9s | 8204 |
| qwen3.8-max | 变道 | 00094 | 2 | 否 | — | 152.5s | 7383 |
| qwen3.8-max | 变道 | 00094 | 3 | 否 | — | 56.6s | 2602 |
| qwen3.8-max | 压线 | 00012 | 1 | 是 | DASH / LEFT / 2.0–3.0s | 138.0s | 7507 |
| qwen3.8-max | 压线 | 00012 | 2 | 是 | DASH / LEFT / 2.0–3.5s | 249.3s | 12237 |
| qwen3.8-max | 压线 | 00012 | 3 | 是 | DASH / LEFT / 1.5–2.5s | 126.0s | 6959 |
| qwen3.8-max | 压线 | 00030 | 1 | 是 | DASH / RIGHT / 5.5–8.0s | 99.5s | 5310 |
| qwen3.8-max | 压线 | 00030 | 2 | 是 | DASH / RIGHT / 5.5–6.0s | 223.6s | 10791 |
| qwen3.8-max | 压线 | 00030 | 3 | 是 | DASH / RIGHT / 5.5–6.0s | 189.4s | 10063 |
| qwen3.8-max | 压线 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.0s | 85.7s | 4475 |
| qwen3.8-max | 压线 | 00051 | 2 | 是 | DOUBLE_SOLID / LEFT / 10.5–11.5s | 130.8s | 7197 |
| qwen3.8-max | 压线 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 155.5s | 8045 |
| qwen3.8-max | 压线 | 00094 | 1 | 否 | — | 97.4s | 4882 |
| qwen3.8-max | 压线 | 00094 | 2 | 是 | SOLID / LEFT / 7.0–8.5s | 266.6s | 12521 |
| qwen3.8-max | 压线 | 00094 | 3 | 是 | DASH / RIGHT / 4.5–8.0s | 172.5s | 8354 |
| qwen3.7-plus | 变道 | 00012 | 1 | 否 | — | 27.0s | 1340 |
| qwen3.7-plus | 变道 | 00012 | 2 | 是 | DASH / LEFT / 4.0–6.0s | 45.5s | 2483 |
| qwen3.7-plus | 变道 | 00012 | 3 | 是 | DASH / LEFT / 1.5–3.0s | 46.2s | 2524 |
| qwen3.7-plus | 变道 | 00030 | 1 | 否 | — | 18.7s | 862 |
| qwen3.7-plus | 变道 | 00030 | 2 | 否 | — | 17.6s | 859 |
| qwen3.7-plus | 变道 | 00030 | 3 | 否 | — | 22.1s | 968 |
| qwen3.7-plus | 变道 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 11.0–13.0s | 21.2s | 558 |
| qwen3.7-plus | 变道 | 00051 | 2 | 否 | — | 21.8s | 1120 |
| qwen3.7-plus | 变道 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 12.0–14.5s | 27.5s | 1428 |
| qwen3.7-plus | 变道 | 00094 | 1 | 否 | — | 47.3s | 2401 |
| qwen3.7-plus | 变道 | 00094 | 2 | 否 | — | 17.8s | 868 |
| qwen3.7-plus | 变道 | 00094 | 3 | 否 | — | 23.0s | 1137 |
| qwen3.7-plus | 压线 | 00012 | 1 | 是 | DASH / LEFT / 2.0–3.0s；DASH / RIGHT / 6.0–8.0s | 77.4s | 4207 |
| qwen3.7-plus | 压线 | 00012 | 2 | 是 | DASH / LEFT / 6.0–8.5s | 114.8s | 6546 |
| qwen3.7-plus | 压线 | 00012 | 3 | 是 | DASH / LEFT / 5.5–8.0s | 46.3s | 2464 |
| qwen3.7-plus | 压线 | 00030 | 1 | 是 | DASH / RIGHT / 3.0–5.0s | 82.7s | 4547 |
| qwen3.7-plus | 压线 | 00030 | 2 | 否 | — | 76.2s | 4307 |
| qwen3.7-plus | 压线 | 00030 | 3 | 是 | DASH / RIGHT / 4.0–6.0s | 79.4s | 4461 |
| qwen3.7-plus | 压线 | 00051 | 1 | 是 | DOUBLE_SOLID / LEFT / 11.5–13.0s | 46.6s | 2465 |
| qwen3.7-plus | 压线 | 00051 | 2 | 是 | DOUBLE_SOLID / LEFT / 12.0–13.0s | 43.0s | 2324 |
| qwen3.7-plus | 压线 | 00051 | 3 | 是 | DOUBLE_SOLID / LEFT / 11.0–13.0s | 32.3s | 1714 |
| qwen3.7-plus | 压线 | 00094 | 1 | 是 | CURB / RIGHT / 8.0–10.0s | 101.5s | 5648 |
| qwen3.7-plus | 压线 | 00094 | 2 | 是 | DASH / RIGHT / 5.0–8.0s；SOLID / LEFT / 12.0–15.5s | 130.5s | 7393 |
| qwen3.7-plus | 压线 | 00094 | 3 | 是 | SOLID / LEFT / 12.0–15.0s | 124.9s | 7148 |

## 总览

| 模型 | 轮次 | ID | 压线 | 压线事件 | 变道 | 变道事件 | 结论是否一致 |
|---|---|---|---|---|---|---|---|
| qwen3.7-plus | 1 | 00012 | 是 | DASH / LEFT / 2.0–3.0s；DASH / RIGHT / 6.0–8.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 1 | 00030 | 是 | DASH / RIGHT / 3.0–5.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 1 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.5–13.0s | 是 | DOUBLE_SOLID / LEFT / 11.0–13.0s | 一致 |
| qwen3.7-plus | 1 | 00094 | 是 | CURB / RIGHT / 8.0–10.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 2 | 00012 | 是 | DASH / LEFT / 6.0–8.5s | 是 | DASH / LEFT / 4.0–6.0s | 一致（时段略有差异） |
| qwen3.7-plus | 2 | 00030 | 否 | — | 否 | — | 一致 |
| qwen3.7-plus | 2 | 00051 | 是 | DOUBLE_SOLID / LEFT / 12.0–13.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 2 | 00094 | 是 | DASH / RIGHT / 5.0–8.0s；SOLID / LEFT / 12.0–15.5s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 3 | 00012 | 是 | DASH / LEFT / 5.5–8.0s | 是 | DASH / LEFT / 1.5–3.0s | 一致（时段略有差异） |
| qwen3.7-plus | 3 | 00030 | 是 | DASH / RIGHT / 4.0–6.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.7-plus | 3 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.0–13.0s | 是 | DOUBLE_SOLID / LEFT / 12.0–14.5s | 一致（时段略有差异） |
| qwen3.7-plus | 3 | 00094 | 是 | SOLID / LEFT / 12.0–15.0s | 否 | — | 一致（仅压线未变道） |
| qwen3.8-max | 1 | 00012 | 是 | DASH / LEFT / 2.0–3.0s | 是 | DASH / LEFT / 1.5–2.5s | 一致（时段略有差异） |
| qwen3.8-max | 1 | 00030 | 是 | DASH / RIGHT / 5.5–8.0s | 是 | DASH / RIGHT / 5.5–6.5s | 一致（时段略有差异） |
| qwen3.8-max | 1 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.0s | 是 | DOUBLE_SOLID / LEFT / 11.5–12.0s | 一致 |
| qwen3.8-max | 1 | 00094 | 否 | — | 是 | DASH / RIGHT / 5.0–7.0s | **冲突**：变道成立但压线为空 |
| qwen3.8-max | 2 | 00012 | 是 | DASH / LEFT / 2.0–3.5s | 是 | DASH / LEFT / 2.0–3.0s | 一致（时段略有差异） |
| qwen3.8-max | 2 | 00030 | 是 | DASH / RIGHT / 5.5–6.0s | 是 | DASH / RIGHT / 6.0–8.0s | 一致（时段略有差异） |
| qwen3.8-max | 2 | 00051 | 是 | DOUBLE_SOLID / LEFT / 10.5–11.5s | — | — | — |
| qwen3.8-max | 2 | 00094 | 是 | SOLID / LEFT / 7.0–8.5s | 否 | — | 一致（仅压线未变道） |
| qwen3.8-max | 3 | 00012 | 是 | DASH / LEFT / 1.5–2.5s | 是 | DASH / LEFT / 2.0–3.0s | 一致（时段略有差异） |
| qwen3.8-max | 3 | 00030 | 是 | DASH / RIGHT / 5.5–6.0s | 是 | DASH / RIGHT / 6.0–8.0s | 一致（时段略有差异） |
| qwen3.8-max | 3 | 00051 | 是 | DOUBLE_SOLID / LEFT / 11.5–12.5s | 是 | DOUBLE_SOLID / LEFT / 10.5–12.0s | 一致（时段略有差异） |
| qwen3.8-max | 3 | 00094 | 是 | DASH / RIGHT / 4.5–8.0s | 否 | — | 一致（仅压线未变道） |

## 压线明细

| 模型 | 轮次 | ID | is_online | 事件 | 耗时 | 推理 token | 输出文本 token |
|---|---|---|---|---|---|---|---|
| qwen3.8-max | 1 | 00012 | True | DASH / LEFT / 2.0–3.0s | 138.0s | 7507 | 58 |
| qwen3.8-max | 2 | 00012 | True | DASH / LEFT / 2.0–3.5s | 249.3s | 12237 | 58 |
| qwen3.8-max | 3 | 00012 | True | DASH / LEFT / 1.5–2.5s | 126.0s | 6959 | 58 |
| qwen3.8-max | 1 | 00030 | True | DASH / RIGHT / 5.5–8.0s | 99.5s | 5310 | 58 |
| qwen3.8-max | 2 | 00030 | True | DASH / RIGHT / 5.5–6.0s | 223.6s | 10791 | 57 |
| qwen3.8-max | 3 | 00030 | True | DASH / RIGHT / 5.5–6.0s | 189.4s | 10063 | 58 |
| qwen3.8-max | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–12.0s | 85.7s | 4475 | 61 |
| qwen3.8-max | 2 | 00051 | True | DOUBLE_SOLID / LEFT / 10.5–11.5s | 130.8s | 7197 | 60 |
| qwen3.8-max | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–12.5s | 155.5s | 8045 | 61 |
| qwen3.8-max | 1 | 00094 | False | — | 97.4s | 4882 | 21 |
| qwen3.8-max | 2 | 00094 | True | SOLID / LEFT / 7.0–8.5s | 266.6s | 12521 | 58 |
| qwen3.8-max | 3 | 00094 | True | DASH / RIGHT / 4.5–8.0s | 172.5s | 8354 | 57 |
| qwen3.7-plus | 1 | 00012 | True | DASH / LEFT / 2.0–3.0s；DASH / RIGHT / 6.0–8.0s | 77.4s | 4207 | 119 |
| qwen3.7-plus | 2 | 00012 | True | DASH / LEFT / 6.0–8.5s | 114.8s | 6546 | 74 |
| qwen3.7-plus | 3 | 00012 | True | DASH / LEFT / 5.5–8.0s | 46.3s | 2464 | 74 |
| qwen3.7-plus | 1 | 00030 | True | DASH / RIGHT / 3.0–5.0s | 82.7s | 4547 | 74 |
| qwen3.7-plus | 2 | 00030 | False | — | 76.2s | 4307 | 26 |
| qwen3.7-plus | 3 | 00030 | True | DASH / RIGHT / 4.0–6.0s | 79.4s | 4461 | 74 |
| qwen3.7-plus | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–13.0s | 46.6s | 2465 | 77 |
| qwen3.7-plus | 2 | 00051 | True | DOUBLE_SOLID / LEFT / 12.0–13.0s | 43.0s | 2324 | 77 |
| qwen3.7-plus | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 11.0–13.0s | 32.3s | 1714 | 77 |
| qwen3.7-plus | 1 | 00094 | True | CURB / RIGHT / 8.0–10.0s | 101.5s | 5648 | 75 |
| qwen3.7-plus | 2 | 00094 | True | DASH / RIGHT / 5.0–8.0s；SOLID / LEFT / 12.0–15.5s | 130.5s | 7393 | 121 |
| qwen3.7-plus | 3 | 00094 | True | SOLID / LEFT / 12.0–15.0s | 124.9s | 7148 | 76 |

## 变道明细

| 模型 | 轮次 | ID | is_lanechange | 事件 | 耗时 | 推理 token | 输出文本 token |
|---|---|---|---|---|---|---|---|
| qwen3.8-max | 1 | 00012 | True | DASH / LEFT / 1.5–2.5s | 159.0s | 7827 | 59 |
| qwen3.8-max | 2 | 00012 | True | DASH / LEFT / 2.0–3.0s | 137.8s | 6439 | 59 |
| qwen3.8-max | 3 | 00012 | True | DASH / LEFT / 2.0–3.0s | 100.3s | 5570 | 59 |
| qwen3.8-max | 1 | 00030 | True | DASH / RIGHT / 5.5–6.5s | 195.2s | 9530 | 59 |
| qwen3.8-max | 2 | 00030 | True | DASH / RIGHT / 6.0–8.0s | 120.1s | 6481 | 59 |
| qwen3.8-max | 3 | 00030 | True | DASH / RIGHT / 6.0–8.0s | 134.4s | 7144 | 58 |
| qwen3.8-max | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 11.5–12.0s | 195.5s | 7268 | 62 |
| qwen3.8-max | 2 | 00051 | — | — | 124.7s | 5897 | 64 |
| qwen3.8-max | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 10.5–12.0s | 93.4s | 4650 | 61 |
| qwen3.8-max | 1 | 00094 | True | DASH / RIGHT / 5.0–7.0s | 195.9s | 8204 | 58 |
| qwen3.8-max | 2 | 00094 | False | — | 152.5s | 7383 | 22 |
| qwen3.8-max | 3 | 00094 | False | — | 56.6s | 2602 | 22 |
| qwen3.7-plus | 1 | 00012 | False | — | 27.0s | 1340 | 27 |
| qwen3.7-plus | 2 | 00012 | True | DASH / LEFT / 4.0–6.0s | 45.5s | 2483 | 75 |
| qwen3.7-plus | 3 | 00012 | True | DASH / LEFT / 1.5–3.0s | 46.2s | 2524 | 75 |
| qwen3.7-plus | 1 | 00030 | False | — | 18.7s | 862 | 26 |
| qwen3.7-plus | 2 | 00030 | False | — | 17.6s | 859 | 26 |
| qwen3.7-plus | 3 | 00030 | False | — | 22.1s | 968 | 27 |
| qwen3.7-plus | 1 | 00051 | True | DOUBLE_SOLID / LEFT / 11.0–13.0s | 21.2s | 558 | 78 |
| qwen3.7-plus | 2 | 00051 | False | — | 21.8s | 1120 | 27 |
| qwen3.7-plus | 3 | 00051 | True | DOUBLE_SOLID / LEFT / 12.0–14.5s | 27.5s | 1428 | 78 |
| qwen3.7-plus | 1 | 00094 | False | — | 47.3s | 2401 | 27 |
| qwen3.7-plus | 2 | 00094 | False | — | 17.8s | 868 | 27 |
| qwen3.7-plus | 3 | 00094 | False | — | 23.0s | 1137 | 27 |

## 耗时与 token

| 模型 | 轮次 | ID | 压线耗时 | 变道耗时 | 压线 total | 变道 total | 压线 cached | 变道 cached |
|---|---|---|---|---|---|---|---|---|
| qwen3.7-plus | 1 | 00012 | 77.4s | 27.0s | 16228 | 13485 | 0 | 0 |
| qwen3.7-plus | 1 | 00030 | 82.7s | 18.7s | 16523 | 13006 | 0 | 0 |
| qwen3.7-plus | 1 | 00051 | 46.6s | 21.2s | 14444 | 12754 | 0 | 0 |
| qwen3.7-plus | 1 | 00094 | 101.5s | 47.3s | 17625 | 14546 | 0 | 0 |
| qwen3.7-plus | 2 | 00012 | 114.8s | 45.5s | 18522 | 14676 | 11520 | 11520 |
| qwen3.7-plus | 2 | 00030 | 76.2s | 17.6s | 16235 | 13003 | 11520 | 11520 |
| qwen3.7-plus | 2 | 00051 | 43.0s | 21.8s | 14303 | 13265 | 11520 | 11520 |
| qwen3.7-plus | 2 | 00094 | 130.5s | 17.8s | 19416 | 13013 | 11520 | 11520 |
| qwen3.7-plus | 3 | 00012 | 46.3s | 46.2s | 14440 | 14717 | 11520 | 11520 |
| qwen3.7-plus | 3 | 00030 | 79.4s | 22.1s | 16437 | 13113 | 11520 | 11520 |
| qwen3.7-plus | 3 | 00051 | 32.3s | 27.5s | 13693 | 13624 | 11520 | 11520 |
| qwen3.7-plus | 3 | 00094 | 124.9s | 23.0s | 19126 | 13282 | 0 | 11520 |
| qwen3.8-max | 1 | 00012 | 138.0s | 159.0s | 19612 | 20149 | 10240 | 0 |
| qwen3.8-max | 1 | 00030 | 99.5s | 195.2s | 17415 | 21852 | 10240 | 0 |
| qwen3.8-max | 1 | 00051 | 85.7s | 195.5s | 16583 | 19593 | 10240 | 0 |
| qwen3.8-max | 1 | 00094 | 97.4s | 195.9s | 16950 | 20525 | 10240 | 0 |
| qwen3.8-max | 2 | 00012 | 249.3s | 137.8s | 24342 | 18761 | 11520 | 11520 |
| qwen3.8-max | 2 | 00030 | 223.6s | 120.1s | 22895 | 18803 | 11520 | 11264 |
| qwen3.8-max | 2 | 00051 | 130.8s | 124.7s | 19304 | 18224 | 11520 | 11520 |
| qwen3.8-max | 2 | 00094 | 266.6s | 152.5s | 24626 | 19668 | 11520 | 11520 |
| qwen3.8-max | 3 | 00012 | 126.0s | 100.3s | 19064 | 17892 | 11520 | 11520 |
| qwen3.8-max | 3 | 00030 | 189.4s | 134.4s | 22168 | 19465 | 11520 | 11520 |
| qwen3.8-max | 3 | 00051 | 155.5s | 93.4s | 20153 | 16974 | 11520 | 11520 |
| qwen3.8-max | 3 | 00094 | 172.5s | 56.6s | 20458 | 14887 | 11520 | 11264 |
| **合计** | — | — | **2890.0s** | **2001.1s** | — | — | — | — |
| **平均** | — | — | **120.4s** | **83.4s** | — | — | — | — |

## 对照备注

1. **qwen3.7-plus / r1 / 00012**：压线 DASH / LEFT / 2.0–3.0s；DASH / RIGHT / 6.0–8.0s；变道 —；一致（仅压线未变道）。
2. **qwen3.7-plus / r1 / 00030**：压线 DASH / RIGHT / 3.0–5.0s；变道 —；一致（仅压线未变道）。
3. **qwen3.7-plus / r1 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.5–13.0s；变道 DOUBLE_SOLID / LEFT / 11.0–13.0s；一致。
4. **qwen3.7-plus / r1 / 00094**：压线 CURB / RIGHT / 8.0–10.0s；变道 —；一致（仅压线未变道）。
5. **qwen3.7-plus / r2 / 00012**：压线 DASH / LEFT / 6.0–8.5s；变道 DASH / LEFT / 4.0–6.0s；一致（时段略有差异）。
6. **qwen3.7-plus / r2 / 00030**：压线 —；变道 —；一致。
7. **qwen3.7-plus / r2 / 00051**：压线 DOUBLE_SOLID / LEFT / 12.0–13.0s；变道 —；一致（仅压线未变道）。
8. **qwen3.7-plus / r2 / 00094**：压线 DASH / RIGHT / 5.0–8.0s；SOLID / LEFT / 12.0–15.5s；变道 —；一致（仅压线未变道）。
9. **qwen3.7-plus / r3 / 00012**：压线 DASH / LEFT / 5.5–8.0s；变道 DASH / LEFT / 1.5–3.0s；一致（时段略有差异）。
10. **qwen3.7-plus / r3 / 00030**：压线 DASH / RIGHT / 4.0–6.0s；变道 —；一致（仅压线未变道）。
11. **qwen3.7-plus / r3 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.0–13.0s；变道 DOUBLE_SOLID / LEFT / 12.0–14.5s；一致（时段略有差异）。
12. **qwen3.7-plus / r3 / 00094**：压线 SOLID / LEFT / 12.0–15.0s；变道 —；一致（仅压线未变道）。
13. **qwen3.8-max / r1 / 00012**：压线 DASH / LEFT / 2.0–3.0s；变道 DASH / LEFT / 1.5–2.5s；一致（时段略有差异）。
14. **qwen3.8-max / r1 / 00030**：压线 DASH / RIGHT / 5.5–8.0s；变道 DASH / RIGHT / 5.5–6.5s；一致（时段略有差异）。
15. **qwen3.8-max / r1 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.5–12.0s；变道 DOUBLE_SOLID / LEFT / 11.5–12.0s；一致。
16. **qwen3.8-max / r1 / 00094**：压线 —；变道 DASH / RIGHT / 5.0–7.0s；**冲突**：变道成立但压线为空。
17. **qwen3.8-max / r2 / 00012**：压线 DASH / LEFT / 2.0–3.5s；变道 DASH / LEFT / 2.0–3.0s；一致（时段略有差异）。
18. **qwen3.8-max / r2 / 00030**：压线 DASH / RIGHT / 5.5–6.0s；变道 DASH / RIGHT / 6.0–8.0s；一致（时段略有差异）。
19. **qwen3.8-max / r2 / 00051**：压线 DOUBLE_SOLID / LEFT / 10.5–11.5s；变道 —；—。
20. **qwen3.8-max / r2 / 00094**：压线 SOLID / LEFT / 7.0–8.5s；变道 —；一致（仅压线未变道）。
21. **qwen3.8-max / r3 / 00012**：压线 DASH / LEFT / 1.5–2.5s；变道 DASH / LEFT / 2.0–3.0s；一致（时段略有差异）。
22. **qwen3.8-max / r3 / 00030**：压线 DASH / RIGHT / 5.5–6.0s；变道 DASH / RIGHT / 6.0–8.0s；一致（时段略有差异）。
23. **qwen3.8-max / r3 / 00051**：压线 DOUBLE_SOLID / LEFT / 11.5–12.5s；变道 DOUBLE_SOLID / LEFT / 10.5–12.0s；一致（时段略有差异）。
24. **qwen3.8-max / r3 / 00094**：压线 DASH / RIGHT / 4.5–8.0s；变道 —；一致（仅压线未变道）。

# 详细结果

# 变道_00012_qwen3.8-max_r1

## 耗时
159.0s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7887,
    "prompt_tokens": 12262,
    "total_tokens": 20149,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7827,
      "rejected_prediction_tokens": null,
      "text_tokens": 59
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-243ab39e-042c-986b-8fb0-d538c47509a2",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 1.5,
      "end_time": 2.5
    }
  ]
}
```

# 变道_00012_qwen3.8-max_r2

## 耗时
137.8s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 6499,
    "prompt_tokens": 12262,
    "total_tokens": 18761,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 6439,
      "rejected_prediction_tokens": null,
      "text_tokens": 59
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-a28761b0-2766-9f9c-9de0-30c6bd082ef1",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 2.0,
      "end_time": 3.0
    }
  ]
}
```

# 变道_00012_qwen3.8-max_r3

## 耗时
100.3s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 5630,
    "prompt_tokens": 12262,
    "total_tokens": 17892,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 5570,
      "rejected_prediction_tokens": null,
      "text_tokens": 59
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-b9ca70f6-19af-999b-ab67-d93f6679504c",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 2.0,
      "end_time": 3.0
    }
  ]
}
```

# 变道_00030_qwen3.8-max_r1

## 耗时
195.2s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 9590,
    "prompt_tokens": 12262,
    "total_tokens": 21852,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 9530,
      "rejected_prediction_tokens": null,
      "text_tokens": 59
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-db1600e2-b4d7-9b0f-818d-6b4c81dd2a91",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.5,
      "end_time": 6.5
    }
  ]
}
```

# 变道_00030_qwen3.8-max_r2

## 耗时
120.1s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 6541,
    "prompt_tokens": 12262,
    "total_tokens": 18803,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 6481,
      "rejected_prediction_tokens": null,
      "text_tokens": 59
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11264,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-99f9a8c1-280a-906f-91ba-a70f2fb18550",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 6.0,
      "end_time": 8.0
    }
  ]
}
```

# 变道_00030_qwen3.8-max_r3

## 耗时
134.4s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7203,
    "prompt_tokens": 12262,
    "total_tokens": 19465,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7144,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-7591167d-be5b-9656-ba75-7066fd5b5d1d",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 6.0,
      "end_time": 8.0
    }
  ]
}
```

# 变道_00051_qwen3.8-max_r1

## 耗时
195.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7331,
    "prompt_tokens": 12262,
    "total_tokens": 19593,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7268,
      "rejected_prediction_tokens": null,
      "text_tokens": 62
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-a4e2481c-84e6-9976-96f2-e99e64e16d50",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 11.5,
      "end_time": 12.0
    }
  ]
}
```

# 变道_00051_qwen3.8-max_r2

## 耗时
124.7s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 5962,
    "prompt_tokens": 12262,
    "total_tokens": 18224,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 5897,
      "rejected_prediction_tokens": null,
      "text_tokens": 64
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-93031c71-d502-9d6c-a6b0-bb3e2c4c8619",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {"line_type": "DOUBLE_SOLID", "direction": "LEFT", "start_time": 11.0, "end_time": 12.5}
  ]
}
}
```

# 变道_00051_qwen3.8-max_r3

## 耗时
93.4s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4712,
    "prompt_tokens": 12262,
    "total_tokens": 16974,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4650,
      "rejected_prediction_tokens": null,
      "text_tokens": 61
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-ba7c0952-cb93-90c3-8744-678fdf2add67",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 10.5,
      "end_time": 12.0
    }
  ]
}
```

# 变道_00094_qwen3.8-max_r1

## 耗时
195.9s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 8263,
    "prompt_tokens": 12262,
    "total_tokens": 20525,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 8204,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-34aaf875-0551-9b8f-82c7-f4b9c5085b37",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.0,
      "end_time": 7.0
    }
  ]
}
```

# 变道_00094_qwen3.8-max_r2

## 耗时
152.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7406,
    "prompt_tokens": 12262,
    "total_tokens": 19668,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7383,
      "rejected_prediction_tokens": null,
      "text_tokens": 22
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-0663e483-fe4c-9ecf-af2c-b203b8886e5d",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00094_qwen3.8-max_r3

## 耗时
56.6s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2625,
    "prompt_tokens": 12262,
    "total_tokens": 14887,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2602,
      "rejected_prediction_tokens": null,
      "text_tokens": 22
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11264,
      "text_tokens": 1920,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-4f1fbb71-ea5d-9917-8873-b07b2d497d7f",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 压线_00012_qwen3.8-max_r1

## 耗时
138.0s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7566,
    "prompt_tokens": 12046,
    "total_tokens": 19612,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7507,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 10240,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-a728a7e4-2c3e-9420-9493-ae552b5f18c9",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 2.0,
      "end_time": 3.0
    }
  ]
}
```

# 压线_00012_qwen3.8-max_r2

## 耗时
249.3s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 12296,
    "prompt_tokens": 12046,
    "total_tokens": 24342,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 12237,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-7b5e681c-cf7d-918a-aa87-85601de75107",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 2.0,
      "end_time": 3.5
    }
  ]
}
```

# 压线_00012_qwen3.8-max_r3

## 耗时
126.0s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7018,
    "prompt_tokens": 12046,
    "total_tokens": 19064,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 6959,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-9c5924f6-683e-9dca-86ae-47a902c2fec3",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 1.5,
      "end_time": 2.5
    }
  ]
}
```

# 压线_00030_qwen3.8-max_r1

## 耗时
99.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 5369,
    "prompt_tokens": 12046,
    "total_tokens": 17415,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 5310,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 10240,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-1ccd82e7-6145-90e5-8060-f2cb02b50a6d",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.5,
      "end_time": 8.0
    }
  ]
}
```

# 压线_00030_qwen3.8-max_r2

## 耗时
223.6s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 10849,
    "prompt_tokens": 12046,
    "total_tokens": 22895,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 10791,
      "rejected_prediction_tokens": null,
      "text_tokens": 57
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-b177c17b-4d48-9347-8f53-332344baba4f",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.5,
      "end_time": 6.0
    }
  ]
}
```

# 压线_00030_qwen3.8-max_r3

## 耗时
189.4s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 10122,
    "prompt_tokens": 12046,
    "total_tokens": 22168,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 10063,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-b66ef91d-b739-97d7-9e96-487fb1dd9100",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.5,
      "end_time": 6.0
    }
  ]
}
```

# 压线_00051_qwen3.8-max_r1

## 耗时
85.7s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4537,
    "prompt_tokens": 12046,
    "total_tokens": 16583,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4475,
      "rejected_prediction_tokens": null,
      "text_tokens": 61
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 10240,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-b3dc2a0a-6063-9a57-9abe-0528d3e59c57",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 11.5,
      "end_time": 12.0
    }
  ]
}
```

# 压线_00051_qwen3.8-max_r2

## 耗时
130.8s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7258,
    "prompt_tokens": 12046,
    "total_tokens": 19304,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7197,
      "rejected_prediction_tokens": null,
      "text_tokens": 60
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-ab4a6420-7b45-9f94-bff5-2d5b134a3471",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 10.5,
      "end_time": 11.5
    }
  ]
}
```

# 压线_00051_qwen3.8-max_r3

## 耗时
155.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 8107,
    "prompt_tokens": 12046,
    "total_tokens": 20153,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 8045,
      "rejected_prediction_tokens": null,
      "text_tokens": 61
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-92afcbb8-2a3d-97ac-b4c2-3d5c8009a4ce",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 11.5,
      "end_time": 12.5
    }
  ]
}
```

# 压线_00094_qwen3.8-max_r1

## 耗时
97.4s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4904,
    "prompt_tokens": 12046,
    "total_tokens": 16950,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4882,
      "rejected_prediction_tokens": null,
      "text_tokens": 21
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 10240,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-79b68f59-1f86-9a2a-bf84-b914b87594ec",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": false,
  "line_events": []
}
```

# 压线_00094_qwen3.8-max_r2

## 耗时
266.6s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 12580,
    "prompt_tokens": 12046,
    "total_tokens": 24626,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 12521,
      "rejected_prediction_tokens": null,
      "text_tokens": 58
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-c41ae1fd-8e28-91d3-b557-75e525bc9ca7",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "SOLID",
      "direction": "LEFT",
      "start_time": 7.0,
      "end_time": 8.5
    }
  ]
}
```

# 压线_00094_qwen3.8-max_r3

## 耗时
172.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 8412,
    "prompt_tokens": 12046,
    "total_tokens": 20458,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 8354,
      "rejected_prediction_tokens": null,
      "text_tokens": 57
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "text_tokens": 1704,
      "video_tokens": 10342
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.8-max",
  "system_fingerprint": null,
  "id": "chatcmpl-7fad4a87-3c45-97b8-90ef-839494f8ad8e",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 4.5,
      "end_time": 8.0
    }
  ]
}
```

# 变道_00012_qwen3.7-plus_r1

## 耗时
27.0s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 1368,
    "prompt_tokens": 12117,
    "total_tokens": 13485,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 1340,
      "rejected_prediction_tokens": null,
      "text_tokens": 27
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-b25ee01c-b34b-93ec-b9e2-06d2b6b14899",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00012_qwen3.7-plus_r2

## 耗时
45.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2559,
    "prompt_tokens": 12117,
    "total_tokens": 14676,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2483,
      "rejected_prediction_tokens": null,
      "text_tokens": 75
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-3eedb104-620b-9895-835c-9a1cea7a96a4",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 4.0,
      "end_time": 6.0
    }
  ]
}
```

# 变道_00012_qwen3.7-plus_r3

## 耗时
46.2s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2600,
    "prompt_tokens": 12117,
    "total_tokens": 14717,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2524,
      "rejected_prediction_tokens": null,
      "text_tokens": 75
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-d3df05b0-e839-913c-a404-7d92619e89ee",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 1.5,
      "end_time": 3.0
    }
  ]
}
```

# 变道_00030_qwen3.7-plus_r1

## 耗时
18.7s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 889,
    "prompt_tokens": 12117,
    "total_tokens": 13006,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 862,
      "rejected_prediction_tokens": null,
      "text_tokens": 26
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-c10080a3-d29b-932f-9413-b28ae96d7986",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00030_qwen3.7-plus_r2

## 耗时
17.6s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 886,
    "prompt_tokens": 12117,
    "total_tokens": 13003,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 859,
      "rejected_prediction_tokens": null,
      "text_tokens": 26
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-66a7eff4-44e4-9700-b828-fa7b83aa01df",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00030_qwen3.7-plus_r3

## 耗时
22.1s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 996,
    "prompt_tokens": 12117,
    "total_tokens": 13113,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 968,
      "rejected_prediction_tokens": null,
      "text_tokens": 27
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-63f94be7-37d4-9c18-a227-0e9ff8ee10bd",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00051_qwen3.7-plus_r1

## 耗时
21.2s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 637,
    "prompt_tokens": 12117,
    "total_tokens": 12754,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 558,
      "rejected_prediction_tokens": null,
      "text_tokens": 78
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-88320849-ed9e-9777-9c3e-4780484f1b08",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
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

# 变道_00051_qwen3.7-plus_r2

## 耗时
21.8s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 1148,
    "prompt_tokens": 12117,
    "total_tokens": 13265,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 1120,
      "rejected_prediction_tokens": null,
      "text_tokens": 27
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-1307ecd6-f365-913f-a868-ae3edbba0ab5",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00051_qwen3.7-plus_r3

## 耗时
27.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 1507,
    "prompt_tokens": 12117,
    "total_tokens": 13624,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 1428,
      "rejected_prediction_tokens": null,
      "text_tokens": 78
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-2a96de64-ccdd-9faf-b581-f61a2ea56174",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 12.0,
      "end_time": 14.5
    }
  ]
}
```

# 变道_00094_qwen3.7-plus_r1

## 耗时
47.3s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2429,
    "prompt_tokens": 12117,
    "total_tokens": 14546,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2401,
      "rejected_prediction_tokens": null,
      "text_tokens": 27
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-6e256e62-f94c-9621-9b0a-ddb392448c4c",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00094_qwen3.7-plus_r2

## 耗时
17.8s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 896,
    "prompt_tokens": 12117,
    "total_tokens": 13013,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 868,
      "rejected_prediction_tokens": null,
      "text_tokens": 27
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-536d372f-5571-9b6e-ac37-36199809ea6d",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 变道_00094_qwen3.7-plus_r3

## 耗时
23.0s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 1165,
    "prompt_tokens": 12117,
    "total_tokens": 13282,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 1137,
      "rejected_prediction_tokens": null,
      "text_tokens": 27
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1907
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-8a709f3e-4b82-90e4-8406-a7444b5b0575",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_lanechange": false,
  "line_events": []
}
```

# 压线_00012_qwen3.7-plus_r1

## 耗时
77.4s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4327,
    "prompt_tokens": 11901,
    "total_tokens": 16228,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4207,
      "rejected_prediction_tokens": null,
      "text_tokens": 119
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-a0617355-dff4-9a19-a00b-ea1d263c5139",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 2.0,
      "end_time": 3.0
    },
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 6.0,
      "end_time": 8.0
    }
  ]
}
```

# 压线_00012_qwen3.7-plus_r2

## 耗时
114.8s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 6621,
    "prompt_tokens": 11901,
    "total_tokens": 18522,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 6546,
      "rejected_prediction_tokens": null,
      "text_tokens": 74
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-7319a8af-026f-9f3f-9d35-94b6fbd8d24d",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 6.0,
      "end_time": 8.5
    }
  ]
}
```

# 压线_00012_qwen3.7-plus_r3

## 耗时
46.3s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2539,
    "prompt_tokens": 11901,
    "total_tokens": 14440,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2464,
      "rejected_prediction_tokens": null,
      "text_tokens": 74
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-f5a46e08-10ba-9a3a-abf7-c7cf114f06fa",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "LEFT",
      "start_time": 5.5,
      "end_time": 8.0
    }
  ]
}
```

# 压线_00030_qwen3.7-plus_r1

## 耗时
82.7s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4622,
    "prompt_tokens": 11901,
    "total_tokens": 16523,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4547,
      "rejected_prediction_tokens": null,
      "text_tokens": 74
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-146f5aa8-bc7e-9816-8dbe-fb272a4f4cba",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 3.0,
      "end_time": 5.0
    }
  ]
}
```

# 压线_00030_qwen3.7-plus_r2

## 耗时
76.2s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4334,
    "prompt_tokens": 11901,
    "total_tokens": 16235,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4307,
      "rejected_prediction_tokens": null,
      "text_tokens": 26
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-e904e8f8-6a39-9487-85ef-13307b14a8b7",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": false,
  "line_events": []
}
```

# 压线_00030_qwen3.7-plus_r3

## 耗时
79.4s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 4536,
    "prompt_tokens": 11901,
    "total_tokens": 16437,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 4461,
      "rejected_prediction_tokens": null,
      "text_tokens": 74
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-15df146a-84a0-9bb0-b71f-c1d90df94033",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 4.0,
      "end_time": 6.0
    }
  ]
}
```

# 压线_00051_qwen3.7-plus_r1

## 耗时
46.6s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2543,
    "prompt_tokens": 11901,
    "total_tokens": 14444,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2465,
      "rejected_prediction_tokens": null,
      "text_tokens": 77
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-c2e5c097-1a02-9e83-9e7a-a206d1ac0a6a",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 11.5,
      "end_time": 13.0
    }
  ]
}
```

# 压线_00051_qwen3.7-plus_r2

## 耗时
43.0s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 2402,
    "prompt_tokens": 11901,
    "total_tokens": 14303,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 2324,
      "rejected_prediction_tokens": null,
      "text_tokens": 77
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-ffaa8e6e-e5de-977a-8369-8d65a516f328",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DOUBLE_SOLID",
      "direction": "LEFT",
      "start_time": 12.0,
      "end_time": 13.0
    }
  ]
}
```

# 压线_00051_qwen3.7-plus_r3

## 耗时
32.3s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 1792,
    "prompt_tokens": 11901,
    "total_tokens": 13693,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 1714,
      "rejected_prediction_tokens": null,
      "text_tokens": 77
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-d71c7d06-06c9-9329-b4b5-4094a1d96a4a",
  "finish_reason": "stop",
  "logprobs": null
}
```
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

# 压线_00094_qwen3.7-plus_r1

## 耗时
101.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 5724,
    "prompt_tokens": 11901,
    "total_tokens": 17625,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 5648,
      "rejected_prediction_tokens": null,
      "text_tokens": 75
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-702ddd53-76b2-969e-9c7b-b8f753669a8e",
  "finish_reason": "stop",
  "logprobs": null
}
```
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
    }
  ]
}
```

# 压线_00094_qwen3.7-plus_r2

## 耗时
130.5s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7515,
    "prompt_tokens": 11901,
    "total_tokens": 19416,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7393,
      "rejected_prediction_tokens": null,
      "text_tokens": 121
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 11520,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-3cd445f9-ae93-9440-ad86-efc610e9dfac",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "DASH",
      "direction": "RIGHT",
      "start_time": 5.0,
      "end_time": 8.0
    },
    {
      "line_type": "SOLID",
      "direction": "LEFT",
      "start_time": 12.0,
      "end_time": 15.5
    }
  ]
}
```

# 压线_00094_qwen3.7-plus_r3

## 耗时
124.9s
## 响应
```json
{
  "token_usage": {
    "completion_tokens": 7225,
    "prompt_tokens": 11901,
    "total_tokens": 19126,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 7148,
      "rejected_prediction_tokens": null,
      "text_tokens": 76
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cache_write_tokens": null,
      "cached_tokens": 0,
      "video_tokens": 10210,
      "text_tokens": 1691
    }
  },
  "model_provider": "openai",
  "model_name": "qwen3.7-plus",
  "system_fingerprint": null,
  "id": "chatcmpl-4b6ffa41-0610-9ec7-8e5d-f419ac3ed72a",
  "finish_reason": "stop",
  "logprobs": null
}
```
## 结果
```json
{
  "is_online": true,
  "line_events": [
    {
      "line_type": "SOLID",
      "direction": "LEFT",
      "start_time": 12.0,
      "end_time": 15.0
    }
  ]
}
```

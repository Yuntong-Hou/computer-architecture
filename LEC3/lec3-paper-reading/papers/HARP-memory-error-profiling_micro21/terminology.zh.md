# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| On-die ECC | 芯片内 ECC | Page 1 | 内存芯片内部执行的纠错码，控制器通常不可见其 metadata 和 correction 行为。 | 是 |
| Direct error | 直接错误 | Page 1-2 | ECC word 数据部分 raw bit error 直接导致的 post-correction error。 | 是 |
| Indirect error | 间接错误 | Page 1-2 | on-die ECC 在不可纠正错误上发生 miscorrection 后引入的错误。 | 是 |
| Hybrid Active-Reactive Profiling (HARP) | 混合主动-反应式错误画像 | Page 1-2 | 先主动识别 direct errors，再运行时安全发现 indirect errors 的 profiling 算法。 | 是 |
| Parity-check matrix | 校验矩阵 | Page 2 and Section 3 | 描述 ECC code 的矩阵；HARP-A 可用它预计算 indirect at-risk bits。 | 是 |

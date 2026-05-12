# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| MIMD | 多指令多数据 | Page 1-3 | 不同 mats 可执行不同 PUD operations，而非全 subarray 同步执行同一操作 | 是 |
| PUD | Processing-using-DRAM | Page 1 | 利用 DRAM 模拟操作属性执行计算 | 是 |
| DRAM mat | DRAM 阵列小块 | Page 2-3 | subarray 内较小二维阵列，是 MIMDRAM 的细粒度资源单位 | 是 |
| SIMD utilization | SIMD 利用率 | Page 12 | 实际有用 lane 占可用 lane 的比例 | 是 |
| Vector reduction | 向量归约 | Page 6-7 | 把向量多元素聚合成标量，如 sum reduction | 是 |
| SALP/BLP | subarray/bank-level parallelism | Page 13-14 | 利用多个 subarray/bank 并发执行，提高 PUD 吞吐 | 是 |

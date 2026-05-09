# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Staged Memory Scheduler (SMS) | 分阶段内存调度器 | Page 1-2 | 三阶段、低复杂度、应用感知 memory scheduler。 | 是 |
| Batch formation | 批形成 | Page 4-5 | 按 source 和 row locality 把 requests 组成 batch。 | 是 |
| SJF probability | 最短作业优先概率 | Page 5 and Page 8-9 | 调节 batch scheduler 偏向短 batch/CPU 或 GPU 的参数 p。 | 是 |
| CGWS | CPU-GPU Weighted Speedup | Page 8 | 综合 CPU/GPU 性能并用 GPUweight 加权的指标。 | 是 |
| DCS FIFO | DRAM command scheduler FIFO | Page 4-5 | 最后阶段 per-bank FIFO，只处理低层 DRAM timing。 | 是 |

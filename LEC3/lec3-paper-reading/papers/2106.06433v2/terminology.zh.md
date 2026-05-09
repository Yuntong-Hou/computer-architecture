# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| near-memory computing | 近内存计算 | Page 1 Abstract; Page 2 | 把计算逻辑放到接近内存的位置，减少远距离数据搬移 | 是 |
| HBM | 高带宽内存（High Bandwidth Memory） | Page 1-3 | 与 FPGA 同封装的高带宽内存，提供多个 pseudo channels | 是 |
| FPGA | 现场可编程门阵列（Field-Programmable Gate Array） | Page 1 | 可重构硬件，用于实现应用专用加速器 | 是 |
| pre-alignment filtering | 预比对过滤 | Page 2-4 | 在完整 sequence alignment 前快速过滤不相似序列 | 是 |
| SneakySnake | SneakySnake 过滤算法 | Page 1-4 | 将 approximate string matching 转换为 single net routing 的高并行过滤器 | 是 |
| COSMO | COSMO 天气预测模型 | Page 1, Page 5 | Consortium for Small-Scale Modeling，本文用其中 kernels 做案例 | 是 |
| stencil kernel | stencil 计算核 | Page 5 | 在网格上访问邻域数据的数值计算模式 | 是 |
| PE | 处理单元（Processing Element） | Page 3, Page 6-8 | FPGA 中并行执行 kernel 部分工作的计算单元 | 是 |
| OCAPI | Open Coherent Accelerator Processor Interface | Page 3, Page 7 | POWER9 与 FPGA 的 cache-coherent interconnect | 是 |
| CAPI2 | Coherent Accelerator Processor Interface 2 | Page 7-8 | 另一种 POWER-FPGA coherent interconnect | 中 |
| BRAM / URAM | 块 RAM / UltraRAM | Page 2-3, Page 7 | FPGA 上的片上存储资源，用于缓存和构建数据流 | 是 |
| arithmetic intensity | 算术强度 | Page 2, Figure 1 | 每 byte 数据对应的计算量；低值通常意味着 memory-bound | 是 |
| energy efficiency | 能效 | Page 7-9 | 每瓦性能，本文以 Mseq/s/Watt 或 GFLOPS/Watt 表示 | 是 |

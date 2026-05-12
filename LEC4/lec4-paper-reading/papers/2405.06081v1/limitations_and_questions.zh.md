# Limitations and Questions

## 1. 作者明确承认的局限
- 部分 Samsung 芯片未观察到同一 subarray 中多于一行的同时激活，因此不支持测试的 PUD operations，见 Page 12, Section 9。
- 当前只能控制 consecutive two-row activation 或 simultaneous 2/4/8/16/32-row activation，无法任意选择激活行数，可能受 1.5ns timing granularity 限制，见 Page 12。

## 2. 论文中隐含的局限
- PUD operations 对 transient errors 的潜在影响没有完全探索，见 Page 12。
- MAJ9 在某些厂商上因 success rate 差可能导致性能退化，见 Page 11。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 能否设计标准化 DRAM 接口，让行数和 row group 更可控地执行 SiMRA？
- MAJ9 等低 success rate 操作是否能通过 input replication、ECC 或重试策略变得实用？
- simultaneous many-row activation 是否会加剧 read disturbance，这与 PuDHammer 论文直接相关。

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。

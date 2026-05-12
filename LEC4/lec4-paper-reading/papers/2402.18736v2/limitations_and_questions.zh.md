# Limitations and Questions

## 1. 作者明确承认的局限
- 并非所有厂商芯片都支持所有操作：SK Hynix 支持最完整，Samsung 主要观察到 NOT，Micron 未观察到这些 bitwise operations，见 Page 14, Section 7。
- 测试芯片最多支持到 16-input Boolean operations；是否能更多输入取决于未公开 row decoder 设计，见 Page 15, Section 7。

## 2. 论文中隐含的局限
- 这些操作依赖违反厂商推荐 timing parameters 和未文档化内部行为，现阶段不等价于标准、可靠的商用功能，见 Page 14-15。
- 论文主要是芯片能力表征，没有完整系统/应用级加速评估。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 为什么 Micron/Samsung 芯片不完整支持这些操作，是否由命令过滤或 row decoder 设计造成？
- 如果把这些行为正式做进 DRAM 标准，需要增加哪些接口和校验机制？
- 在包含 ECC、refresh、温度变化和真实工作负载的系统里，success rate 能否满足应用要求？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。

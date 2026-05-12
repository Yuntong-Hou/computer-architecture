# Limitations and Questions

## 1. 作者明确承认的局限
- 论文没有实现和定量 benchmark，除引用 IBM 360/85 cache 结果外，多数性能主张是概念性推断，见 Page 3-6。
- 可行性强依赖当时对 microelectronic packaging/pin/gate cost 的预测，见 Page 1 和 Page 4。

## 2. 论文中隐含的局限
- 作者明确指出 instruction repertoire 的实际 utility 难以衡量，是 future research，见 Page 4。
- 高层语言与 unconventional instruction repertoire 不匹配，若编译器目标语言只用普通指令，强大 memory-side instructions 难以带来实际收益，见 Page 6。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- Stone 的 sector operation 抽象和现代 SIMDRAM/PEI 的 ISA abstraction 有哪些共同点和差异？
- 如果把 logic-enhanced cache 换成现代 HBM logic layer 或 near-cache accelerator，哪些设计仍成立？
- 高层语言如何自然表达 memory-side sector/bit-slice operations，这个问题在现代 PIM 编译器中如何解决？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。

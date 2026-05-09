# Limitations and Questions

## 1. 作者明确承认的局限
- PIM adoption 仍受 programming model、runtime scheduling、data mapping、coherence、virtual memory 等系统问题限制。（Page 24-31, Section 8）
- 不同 PIM substrates 的可编程性、成本和可维护性差异很大，不能用单一方案覆盖所有 workload。（Page 13-24, Sections 5-7）

## 2. 论文中隐含的局限
- 综述覆盖面大但不是统一实验平台，跨案例的数字不能直接横向比较。（推断，基于 survey nature）
- 截至本文时间点，commercial PIM adoption 仍处早期，后续标准和产品进展需要另查。（推断，基于 Section 8-9）

## 3. 实验设计可能存在的问题
- 结论与本文所选平台、benchmark、模型或综述范围相关；迁移到新系统时需要重新验证。（推断）

## 4. 方法可能不适用的场景
- 当 workload 行为、硬件接口、内存技术或系统软件支持与论文假设差异明显时，本文方法或结论可能不直接适用。（推断）

## 5. 我阅读时应该追问的问题
- 为什么 data movement 已经成为性能、能耗和可扩展性瓶颈？
- PUM 与 PNM 的技术基础、收益和限制分别是什么？
- RowClone、Ambit、Tesseract、移动端 PNM、GPU PNM、GenASM/NATSA 等案例之间如何归类？
- PIM 真正进入实际系统还缺哪些编程模型、runtime、coherence、virtual memory 和 benchmark 支持？

## 6. 后续可以继续阅读的方向
- 在 LEC3 论文中继续比较 PIM/NDP、RowHammer/reliability、DRAM simulator 三条主线的共同假设和评估方法。

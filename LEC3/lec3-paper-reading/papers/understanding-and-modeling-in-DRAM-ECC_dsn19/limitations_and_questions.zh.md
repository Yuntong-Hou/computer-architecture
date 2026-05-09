# Limitations and Questions

## 1. 作者明确承认的局限
- MAP estimation 只能在候选模型中选择最可能模型，不能证明未纳入模型的真实 ECC scheme 不存在。（Page 7-8, Section 5.5/5.8）
- EIN 需要已知并可控的 error mechanism 和可诱发 uncorrectable errors；不能识别 bit-exact pre-correction error locations。（Page 8, Section 5.8）

## 2. 论文中隐含的局限
- 真实厂商 ECC 可能随产品/世代变化，候选 code set 与实验条件需随设备重新校准。（推断，基于 Sections 4-7）
- EIN 推断的是 error rate/distribution 而非完整厂商 ECC implementation 细节，安全/专利分析需谨慎使用。（推断，基于 Section 5.8）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、workload、模拟器、芯片样本或工艺节点；迁移到现代 DDR5/HBM/CXL/GPU/PIM 系统时需复核。（推断）

## 4. 方法可能不适用的场景
- 当系统接口、软件栈、workload locality、错误模型、QoS 目标或硬件组织与论文假设明显不同时，方法收益可能变化。（推断）

## 5. 我阅读时应该追问的问题
- on-die ECC 为什么会破坏传统 DRAM error characterization？
- 只看 post-correction errors，如何反推出 ECC code 和 pre-correction BER？
- MAP estimation 如何利用 pre-correction errors 的统计性质区分 ECC schemes？
- EINSim 如何模拟 arbitrary ECC scheme 的 correction/miscorrection？
- 真实 LPDDR4 devices 使用的 on-die ECC 是什么？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：heterogeneous memory scheduling、PIM graph processing、on-die ECC-aware DRAM characterization、HBM/PIM productization。

# Limitations and Questions

## 1. 作者明确承认的局限
- 真实芯片无法获得 ground truth ECC functions；位置：Page 2-3。
- 由于保密关系，不能公开恢复出的最终 ECC functions；位置：Page 2-3。
- BEEP 主要展示 data-retention errors，其他错误机制留待未来；位置：Page 12。

## 2. 论文中隐含的局限
- BEER 需要能诱导足够多、可控的 uncorrectable retention errors。
- SAT solving 对更复杂 ECC 可能成本更高。

## 3. 实验设计可能存在的问题
- 真实芯片结果无法直接验证完全正确性，只能靠仿真证明方法正确。
- 厂商可能使用非线性或组合型 ECC/repair 机制，超出本文假设。

## 4. 方法可能不适用的场景
- 如果 ECC 不属于可用线性 block code 建模，BEER 需要扩展。
- 如果芯片隐藏/扰动 post-correction error visibility，BEER 观测信息不足。

## 5. 我阅读时应该追问的问题
- DDR5 on-die ECC 是否仍可用 BEER 类方法恢复？
- BEER 与 HARP 如何互补？
- 恢复 ECC function 是否可能带来攻击风险？
- 如何优化 SAT formulation 降低 runtime？

## 6. 后续可以继续阅读的方向
- HARP-memory-error-profiling_micro21。
- understanding-and-modeling-in-DRAM-ECC_dsn19。
- REAPER/retention profiling 相关工作。

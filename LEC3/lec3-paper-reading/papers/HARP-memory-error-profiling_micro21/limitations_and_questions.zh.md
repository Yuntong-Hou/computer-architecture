# Limitations and Questions

## 1. 作者明确承认的局限
- HARP 假设 on-die ECC 使用 systematic encoding，并需要修改 read operation 以读取 raw data values。（Page 2, Introduction; Section 5-6）
- secondary ECC 的 correction capability 需要不低于 on-die ECC，增加控制器侧开销。（Page 1-2, HARP overview）

## 2. 论文中隐含的局限
- 评估主要是仿真与模型化 case study，真实商用 DRAM 中 ECC 细节和接口可获得性可能受厂商限制。（推断，基于 Page 1-2 evaluation description）
- 若未来 on-die ECC 更复杂或非 systematic，HARP 假设需要重新审视。（推断，基于 Section 3-6 assumptions）

## 3. 实验设计可能存在的问题
- 实验结论与特定模型、平台、benchmark 或 workload 选择有关；迁移到新硬件/新应用时需要复核。（推断，基于实验设置章节）

## 4. 方法可能不适用的场景
- 当系统假设无法满足、输入行为与评估 workload 差异明显，或硬件/软件接口无法提供所需支持时，该方法收益可能下降。（推断）

## 5. 我阅读时应该追问的问题
- on-die ECC 会怎样改变内存控制器看到的错误分布？
- 为什么传统 active/reactive profiling 在 on-die ECC 存在时难以覆盖所有 at-risk bits？
- 能否在不暴露 ECC metadata 的情况下，实用地识别 direct 和 indirect errors？
- HARP 相比 Naive/BEEP 类 baseline 在 profiling rounds 与 repair 效果上提升多少？

## 6. 后续可以继续阅读的方向
- 阅读同一主题下的相邻论文，并重点比较：问题定义是否相同、硬件假设是否一致、评价指标是否可比、是否有真实系统或芯片数据。

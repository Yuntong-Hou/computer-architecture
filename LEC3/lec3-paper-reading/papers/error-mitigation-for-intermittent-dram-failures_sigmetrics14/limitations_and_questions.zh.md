# Limitations and Questions

## 1. 作者明确承认的局限
- testing-only bit repair 即使测试数月也无法提供强可靠性保证。（Page 11, Figure 18a）
- 在线 profiling 需要在不干扰系统运行的情况下持续执行，这是实用化关键。（Page 12, Section 8）

## 2. 论文中隐含的局限
- 实验基于 DDR3-era modules，未来 DDR4/DDR5/LPDDR/HBM 的 VRT 分布需重新测量。（推断，基于 tested modules scope）
- ECC 组合收益依赖错误独立性、granularity 和实际错误相关性；真实系统需考虑 correlated failures。（推断，基于 ECC model）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 少量 testing 能发现多少 intermittent failures？
- refresh interval guardband 对 VRT cells 是否足够？
- ECC 与 testing/guardbanding 组合能把 failure probability 降到什么程度？
- 已有 bit repair、VS-ECC、Hi-ECC 在真实 intermittent failure 数据下是否仍成立？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DRAM retention/VRT profiling、数据中心应用容错、PIM pointer chasing、system-DRAM co-design、shared-memory slowdown/QoS。

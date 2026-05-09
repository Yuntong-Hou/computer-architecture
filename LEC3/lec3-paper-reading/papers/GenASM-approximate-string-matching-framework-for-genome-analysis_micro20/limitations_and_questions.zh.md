# Limitations and Questions

## 1. 作者明确承认的局限
- pre-alignment filtering for long reads 未评估，留给未来；位置：Page 8。
- 一些 use cases 只讨论未量化，包括 de novo overlap、indexing、WGA、generic text search；位置：Page 13。
- GenASM-TB 对更多 scoring order/configurability 的支持留给未来；位置：Page 11 footnote。

## 2. 论文中隐含的局限
- 多数系统结果基于综合和模拟，不是完整芯片实测。
- 部分 baseline 结果来自原论文，比较公平性依赖参数假设。
- PIM 部署需要 3D-stacked memory logic layer 和软件集成。

## 3. 实验设计可能存在的问题
- 端到端 pipeline speedup 只替换 alignment step，真实系统还需考虑 I/O、format conversion、scheduling。
- accuracy comparison 与 scoring function/window overlap 参数有关。

## 4. 方法可能不适用的场景
- 需要复杂 affine gap scoring 或非标准 alignment semantics 的工具可能需要扩展 TB。
- 非 DNA 大 alphabet text search 会增加 pattern bitmask/storage 成本。

## 5. 我阅读时应该追问的问题
- GenASM 如何集成到真实 Minimap2/BWA-MEM pipeline？
- candidate location 由软件 filtering 提供时，host-accelerator data movement 多大？
- 对 ultra-long reads 和高 error ONT reads，window/overlap 如何调？
- GenASM 与 newer GPU/FPGA aligners 比较是否仍领先？

## 6. 后续可以继续阅读的方向
- Accelerating Genome Analysis primer。
- Darwin、GenAx/SillaX、Shouji、SneakySnake。
- PIM/3D-stacked memory accelerators for genome analysis。

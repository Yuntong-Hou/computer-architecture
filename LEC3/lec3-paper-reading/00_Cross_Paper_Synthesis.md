# Cross-Paper Synthesis

## 1. 这些文献共同关注的问题

这组 LEC3 文献整体围绕“memory system scaling 后，性能、能耗、可靠性和安全性如何继续维持”展开。核心矛盾是：DRAM/NVM/PIM 技术提供更高容量和潜在带宽，但传统抽象把 memory 当作可靠、均匀、被动的黑盒，这在 RowHammer、retention failures、on-die ECC、data movement 和 heterogeneous workloads 面前越来越不成立。

## 2. 方法之间的关系

- RowHammer/retention/reliability 论文从 failure mechanisms 出发，逐步走向 profiling、mitigation 和 field modeling。
- Scheduling/QoS 论文从 shared memory interference 出发，用模型、学习或 staged organization 控制不同应用之间的带宽竞争。
- PIM/NDP 论文从 data movement bottleneck 出发，把计算移动到 memory 附近，尤其适合 graph、genomics、stencil、sparse matrix、time-series 等 memory-bound workloads。
- Cross-layer interface 论文则试图让 hardware、OS、runtime 和 application 共享元数据，使 memory system 能暴露更多可控语义。

## 3. 技术路线对比

- 可靠性路线：RAIDR/AVATAR/Reaper/HARP/MEMCON/DRAM-ECC 关注如何发现、建模和缓解弱 cells 或错误机制；RowHammer 系列关注 disturbance errors 如何变成安全风险。
- 性能路线：RLMC/MISE/ASM/SMS/DASH 关注 memory scheduling、slowdown model 和 heterogeneous QoS。
- 近数据计算路线：Tesseract/SISA/IMPICA/SMASH/GenASM/NERO/NATSA/Google PIM 通过 PIM/NDP 降低数据移动或利用内部带宽。
- 基础设施路线：Ramulator2/SoftMC 提供模拟和真实芯片实验能力，是把其他论文结果复现、扩展和验证的工具基础。

## 4. 结论是否一致

多数论文的结论高度一致：memory bottleneck 不能只靠更大的 cache、更高频率或单层优化解决。可靠性问题需要 profiling 和 cross-layer mitigation；性能问题需要 application-aware scheduling 或把计算移动到数据附近；安全问题需要 memory controller、DRAM vendor、OS 和软件栈协同。

## 5. 争议点或不确定点

- 一些早期 PCM/PIM 参数来自当时 prototype 或 HMC-era 假设，迁移到现代 HBM、DDR5、CXL 和 commercial PIM 时需要重新验证。
- RowHammer 防御方案在状态开销、误报、可部署性和对未知攻击模式的覆盖之间存在长期折中。
- on-die ECC 让真实错误率更难观察，未来 characterization 需要同时推断 ECC 与 error mechanism。
- PIM/NDP 的软件栈、编程模型和数据布局仍是落地关键，不只是硬件结构问题。

## 6. 哪些论文适合先读

优先读 `memory-scaling_imw13`、`dram-row-hammer_isca14`、`raidr-dram-refresh_isca12`、`Ramulator2_arxiv23`、`softMC_hpca17`。这几篇分别提供全局视角、经典 failure、refresh optimization、仿真工具和真实芯片实验基础。

## 7. 哪些论文适合深入读

深入方向可以按兴趣选择：RowHammer 安全读 `RowPress_isca23`、`panopticon` 和前 11 篇新近 arXiv；可靠性 profiling 读 `reaper-dram-retention-profiling-lpddr4_isca17`、`HARP-memory-error-profiling_micro21`、`understanding-and-modeling-in-DRAM-ECC_dsn19`；PIM/NDP 读 `tesseract-pim-architecture-for-graph-processing_isca15`、`SISA-GraphMining-on-PIM_micro21`、`GenASM-approximate-string-matching-framework-for-genome-analysis_micro20`；调度读 `rlmc_isca08`、`mise-predictable_memory_performance-hpca13`、`staged-memory-scheduling_isca12`。

## 8. 我的学习路线建议

1. 先用 `00_All_Papers_Summary_Table.md` 建立全局地图。
2. 每条主线挑 2-3 篇代表作精读，先看 `reading_summary.zh.md` 和 `key_points_with_locations.zh.md`。
3. 回到 PDF 查看核心图表：RowHammer vulnerability 图、RAIDR retention distribution、REAPER Figures 9-13、Tesseract Figures 3/6/10/14、EIN Figures 1/8/11。
4. 最后再读 `00_Glossary.md` 和 `00_Open_Questions.md`，把术语和研究问题串起来。

## 9. 后续值得补充阅读的方向

- DDR5/HBM3/HBM4 中 RowHammer、RowPress、TRR/RFM/PRAC 的最新公开评估。
- CXL memory pooling、memory tiering 与 cross-layer memory metadata。
- Commercial PIM/NDP 产品和软件栈。
- on-die ECC、in-DRAM ECC 与 system-level ECC 的组合可靠性模型。
- LLM/推荐系统/图学习 workloads 在 modern memory hierarchy 上的数据移动瓶颈。

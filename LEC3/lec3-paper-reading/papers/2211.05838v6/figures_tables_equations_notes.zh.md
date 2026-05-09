# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM organization | CPU、memory controller、DRAM module/rank/chip/bank/row 的层级 | 背景图 | 结合 DRAM command 读 |
| Figure 2 | Page 4 | DRAM Bender block diagram | 展示 host API、frontend/backend、DFI/PHY 等模块 | 设计核心图 | 重点看在哪里生成 commands |
| Figure 3 | Page 5 | Instruction encodings | DRAM Bender ISA 如何编码 commands | 说明 no restriction 的实现基础 | 细节可略读 |
| Figure 4 | Page 7 | Hardware infrastructure | FPGA boards、DIMM/SODIMM、温控等实验设置 | 说明真实实验环境 | 做实验复现时重点看 |
| Figure 5 | Page 7 | Temperature measurements | 温控稳定性 | RowHammer/retention 对温度敏感 | 检查实验可信度 |
| Figure 6 | Page 8 | Experiment workflow | 创建平台、program、执行、取回数据 | 说明易用性 | 可作为使用流程记忆 |
| Figure 7 | Page 9 | Double-sided RowHammer attack | V1/A1/V2/A2/V3 rows 和 T 参数 | 理解 case study #1 | 必读 |
| Figure 8-9 | Page 10 | Interleaving pattern vs bit-flip rate | T 越小，交替越频繁，bit-flips 越多 | RowHammer pattern 重要证据 | 看 T=1 与 T=64K |
| Figure 10-11 | Page 10-11 | Interleaving pattern vs HCfirst | T 改变 first bit-flip 所需 ACT 数 | 防护阈值设计证据 | 结合 Figure 8-9 |
| Figure 12 | Page 12 | DDR4 AND/OR BER distribution | 部分 segments 支持 AND/OR，但 BER 非零且 heterogenous | PIM primitive 真实可行性证据 | 重点看 <5% 与 <10% BER |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 2 | SoftMC/LRT/DRAM Bender 对比 | DRAM Bender 同时无接口限制、易用、可扩展 | 全文最重要表 | 先读 |
| Table 2 | Page 5 | ISA description | 指令支持 command、data、control flow | 解释平台能力 | 读设计时参考 |
| Table 3 | Page 7 | FPGA prototypes | 支持多个 DDR4/DDR3 FPGA boards | 证明可扩展性 | 看 board 和 protocol |
| Table 4 | Page 7 | FPGA resource utilization | 平台资源开销 | 实用性证据 | 复现时看 |
| Table 5 | Page 7 | Temperature measurements | 温度控制稳定 | RowHammer 实验可信度 | 快速浏览 |
| Table 6 | Page 10 | Tested DRAM modules | 三个制造商 DDR4 modules | case studies 的样本范围 | 注意样本数量限制 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| HCfirst metric | Page 9-11 | 衡量出现 first RowHammer bit-flip 前每个 aggressor 的 ACT 数 | HCfirst 越低越脆弱 | 比总 bit-flips 更接近防护阈值 | 是 |
| BER metric | Page 11-12 | 衡量 in-DRAM bitwise operation 的错误率 | Bit Error Rate | 真实 DRAM primitive 不是理想门电路 | 中 |

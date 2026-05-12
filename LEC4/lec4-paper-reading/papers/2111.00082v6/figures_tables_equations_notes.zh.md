# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM organization and timing | 给出 PiDRAM 需要控制的 DRAM 层次与时序参数 | 背景图 |
| Figure 2 | Page 5 | PiDRAM overview | 展示硬件/软件组件及其边界 | 核心架构图 |
| Figure 8 | Page 11 | Physical address to DRAM address mapping | 说明 RowClone 对地址映射与对齐的依赖 | 关键定位图 |
| Figure 9-11 | Page 12 | RowClone throughput improvement | 比较 bare-metal、No Flush 与 CLFLUSH 情形 | 核心结果图 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 2 | Page 7 | PiDRAM 可研究的 PuM 技术 | 说明框架扩展范围不止 RowClone/D-RaNGe | 扩展性证据 |
| Table 4 | Page 16 | 与相关平台比较 | 突出 PiDRAM 同时支持真实 DRAM、flexible MC、system software 和 open-source | 定位必读 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文重点是系统框架与实验 | 公式不是理解重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。

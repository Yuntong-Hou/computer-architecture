# Limitations and Questions

## 1. 作者明确承认的局限
- 论文篇幅短，重点展示框架与案例，未覆盖所有可能 DRAM/SoC 集成场景。（Page 1-4）
- cycle-accurate DRAM simulator 仍依赖模型准确性和配置正确性。（Page 3 validation section）

## 2. 论文中隐含的局限
- C++20 和插件架构提高扩展性，但用户仍需理解 DRAM timing/state machine 才能安全修改。（推断，基于 Section 2）
- RowHammer case study 是展示模块化能力，不等同于完整防御方案排名。（推断，基于 Section 3.3）

## 3. 实验设计可能存在的问题
- 结论与本文所选平台、benchmark、模型或综述范围相关；迁移到新系统时需要重新验证。（推断）

## 4. 方法可能不适用的场景
- 当 workload 行为、硬件接口、内存技术或系统软件支持与论文假设差异明显时，本文方法或结论可能不直接适用。（推断）

## 5. 我阅读时应该追问的问题
- 如何把 DRAM memory system 的关键组件抽象为可替换 interface/implementation？
- 如何用简洁可读的 syntax 描述 DDR5/LPDDR5/HBM3/GDDR6 等标准？
- RowHammer mitigation 能否作为 plugin 接入不修改 baseline controller？
- 模块化是否牺牲验证准确性和 simulation speed？

## 6. 后续可以继续阅读的方向
- 在 LEC3 论文中继续比较 PIM/NDP、RowHammer/reliability、DRAM simulator 三条主线的共同假设和评估方法。

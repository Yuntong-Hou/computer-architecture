# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Processing using Memory | 利用内存进行处理 | Page 2 | 复用内存器件固有结构/行为完成计算，而不是单纯靠外加逻辑 | 是 |
| Triple-Row Activation (TRA) | 三行同时激活 | Page 14-16 | 同时激活三条 DRAM wordline，使 sense amplifier 得到 majority 结果 | 是 |
| Ambit-AND-OR | Ambit 的 AND/OR 机制 | Page 14-16 | 通过 TRA 和控制行实现 bulk AND/OR | 是 |
| Dual-contact cell (DCC) | 双接触 DRAM 单元 | Page 17 | 用两个访问晶体管支持读取反相值，实现 NOT | 是 |
| AAP primitive | ACTIVATE-ACTIVATE-PRECHARGE 原语 | Page 20-21 | Ambit 控制器执行 bulk bitwise operation 的基本命令序列 | 是 |
| RowClone | DRAM 内行复制机制 | Page 12, Page 16 | 在 DRAM 内完成行复制/初始化，Ambit 用它移动操作数和结果 | 是 |

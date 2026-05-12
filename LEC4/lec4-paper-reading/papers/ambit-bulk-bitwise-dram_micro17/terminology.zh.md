# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Ambit | 内存内批量按位加速器 | Page 1 | 利用 DRAM analog operation 执行 bitwise operations | 是 |
| Triple-Row Activation (TRA) | 三行同时激活 | Page 4-5 | 同时激活三行得到 majority function | 是 |
| Dual-contact cell (DCC) | 双接触单元 | Page 6 | 支持读取反相值以实现 NOT | 是 |
| AAP | ACTIVATE-ACTIVATE-PRECHARGE | Page 8 | Ambit 执行 bulk bitwise operation 的基础命令序列 | 是 |
| RowClone | DRAM 内行复制 | Page 5 | 用于把源/目标行搬到 designated rows | 是 |
| BitWeaving | 数据库位编织扫描技术 | Page 11-12 | 把列值按 bit plane 存放以用 bitwise operations 加速 predicate | 中 |

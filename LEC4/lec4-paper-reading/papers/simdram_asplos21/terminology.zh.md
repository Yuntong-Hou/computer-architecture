# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| SIMDRAM | DRAM 内 bit-serial SIMD 框架 | Page 1 | 用 MAJ/NOT 和 vertical layout 支持通用 PuM operations | 是 |
| Majority operation (MAJ) | 多数逻辑 | Page 3 | 三个输入中多数为 1 则输出 1，是 TRA 的逻辑模型 | 是 |
| Vertical data layout | 垂直数据布局 | Page 2 | 一个元素的 bits 沿同一 bitline 分布，使 bitline 成为 SIMD lane | 是 |
| Majority-Inverter Graph (MIG) | 多数-反相图 | Page 19 | 用 MAJ/NOT 表示和优化逻辑的图结构 | 是 |
| bbop instruction | bulk bitwise operation 指令 | Page 9-10 | 程序员/编译器调用 SIMDRAM operation 的 ISA 接口 | 是 |
| µProgram | 微程序 | Page 5 | SIMDRAM control unit 执行的 DRAM command sequence | 是 |
| Transposition unit | 转置单元 | Page 15 | 负责 horizontal/vertical layout 转换的 memory-controller 结构 | 是 |

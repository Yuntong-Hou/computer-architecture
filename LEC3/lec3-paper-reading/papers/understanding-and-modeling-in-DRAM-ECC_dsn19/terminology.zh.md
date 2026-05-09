# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| On-die ECC | 片上错误纠正 | Page 1 | DRAM device 内部不可见 ECC，用于提高 yield 和可靠性。 | 是 |
| EIN | Error-correction INference | Page 1-2 | 从 post-correction errors 推断 ECC scheme 和 pre-correction rates 的方法。 | 是 |
| EINSim | EIN 仿真器 | Page 2 and Page 7 | 开源 C++ simulator，用于模拟 ECC 变换和求 likelihood。 | 是 |
| Pre-correction error | 纠错前错误 | Page 1 | 物理机制直接产生、被 ECC 纠正/遮蔽前的错误。 | 是 |
| Post-correction error | 纠错后错误 | Page 1 | 研究者在 device 输出端可观察到的错误。 | 是 |
| MAP estimation | 最大后验估计 | Page 2 and Page 6 | 选择给定观测下最可能模型参数的统计方法。 | 是 |

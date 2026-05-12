# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Fractional value | 分数电压值 | Page 1 | 介于传统 0/Vdd 与 1/ground 之间的 DRAM cell 电压状态 | 是 |
| Frac operation | Frac 操作 | Page 3 | 用 ACTIVATE 后立即 PRECHARGE 中断放大以生成 fractional value | 是 |
| Half-m operation | 掩码 Half 操作 | Page 3-4 | 在 masked bits 中混合写入 normal values 与 Half values | 是 |
| F-MAJ | Fractional majority operation | Page 8-10 | 用 fractional value 改善四行激活下 majority operation 的覆盖和稳定性 | 是 |
| Physical Unclonable Function (PUF) | 物理不可克隆函数 | Page 10 | 利用制造差异生成设备唯一响应的安全 primitive | 是 |
| Intra-HD / Inter-HD | 模块内/模块间汉明距离 | Page 11 | 衡量 PUF reliability 与 uniqueness 的指标 | 是 |

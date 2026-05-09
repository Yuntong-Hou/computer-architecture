# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RowHammer | 行锤击 | Page 1 | 反复激活 aggressor rows，导致相邻 victim rows 中 bit flips 的 DRAM disturbance 现象。 | 是 |
| Aggressor row | 攻击行/aggressor 行 | Page 2-4 | 被反复打开关闭以诱发扰动的 DRAM row。 | 是 |
| Victim row | 受害行 | Page 4-8 | 未被直接访问却出现 bit flip 的邻近 row。 | 是 |
| PARA | 概率相邻行激活/刷新 | Page 9-10 | 每次关闭 row 时以小概率刷新邻近 rows 的 mitigation。 | 是 |
| SECDED ECC | 单错纠正双错检测 ECC | Page 8 | 常见 ECC，但可能无法修复 RowHammer 多 bit errors。 | 是 |

# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| High Bandwidth Memory (HBM2) | 高带宽内存 HBM2 | Page 1-3 | 3D-stacked DRAM，提供高带宽接口 | 是 |
| Read Disturbance | 读扰动 | Page 1 | 读取/激活某些 row 对邻近 row 造成电气干扰 | 是 |
| RowHammer | 行锤击 | Page 1 | 反复激活 aggressor row 诱发 victim row bitflip | 是 |
| RowPress | 行压迫 | Page 1, Page 9 | 延长 aggressor row open 时间造成更强扰动 | 是 |
| HCfirst | 首个 bitflip 的 hammer count | Page 4-8 | 触发第一个错误所需 activation 数 | 是 |
| Bit Error Rate (BER) | 位错误率 | Page 4 | bitflip 数相对测试位数的比例 | 是 |
| tAggON | aggressor row 开启时间 | Page 9 | RowPress 中 aggressor row 保持 open 的时间 | 是 |
| TRR-like Defense | 类 TRR 防护 | Page 10-11 | 片内跟踪高 activation row 并刷新 victim 的机制 | 是 |
| Dummy Row | 干扰/填充 row | Page 11 | 用于影响内部 tracking 的额外访问 row | 是 |
| ECC Word | ECC 码字 | Page 12 | ECC 进行错误检测/纠正的粒度 | 中 |

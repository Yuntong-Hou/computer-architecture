# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RowPress | 行按压 | Page 1 | 长时间保持 DRAM row open 导致附近 row bitflips 的 read-disturb 现象。 | 是 |
| tAggON | aggressor row on time | Page 1-2 | aggressor row 保持打开的时间。 | 是 |
| ACmin | 最小触发 activation 数 | Page 2 | 诱发至少一个 bitflip 所需最小 aggressor activations。 | 是 |
| Graphene-RP / PARA-RP | 适配 RowPress 的 Graphene/PARA | Page 15-16 | 同时考虑 row-open time 和 RowHammer threshold 的防御版本。 | 是 |

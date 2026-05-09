# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RAIDR | Retention-Aware Intelligent DRAM Refresh | Page 1 | 根据 row retention time 差异化刷新。 | 是 |
| Retention time bin | 保持时间分箱 | Page 4 | 按需要 refresh interval 将 rows 分组。 | 是 |
| Bloom filter | 布隆过滤器 | Page 5 | 低开销近似集合，用于存储短 retention rows。 | 是 |
| RAS-only refresh | 按行地址刷新 | Page 5 | controller 指定 row 进行 refresh，而非标准 auto-refresh。 | 是 |

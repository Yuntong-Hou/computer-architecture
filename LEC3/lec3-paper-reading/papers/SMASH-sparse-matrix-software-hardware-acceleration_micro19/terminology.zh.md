# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Hierarchical bitmap | 层次化位图 | Page 4-5 | 用多层位图表示哪些块含非零元素。 | 是 |
| Bitmap Management Unit (BMU) | 位图管理单元 | Page 6 | 硬件扫描位图层次并返回非零块位置。 | 是 |
| CSR | 压缩稀疏行格式 | Page 1-2 | 常见稀疏矩阵格式，但 indexing/pointer chasing 开销高。 | 是 |
| SpMV / SpMM | 稀疏矩阵向量/矩阵乘法 | Page 2 | SMASH 的两个核心稀疏线性代数用例。 | 是 |

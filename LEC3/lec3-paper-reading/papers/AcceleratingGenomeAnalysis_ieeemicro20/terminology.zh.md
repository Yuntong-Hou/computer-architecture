# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Read Mapping | 读段映射 | Page 1-3 | 将 reads 定位到 reference genome | 是 |
| Approximate String Matching (ASM) | 近似字符串匹配 | Page 2 | 允许 insertion/deletion/substitution 的匹配 | 是 |
| Indexing | 索引 | Page 3 | 用 seeds 找候选位置 | 是 |
| Pre-alignment Filtering | 预比对过滤 | Page 3-6 | 在 alignment 前丢弃明显不相似候选 | 是 |
| Sequence Alignment | 序列比对 | Page 3, Page 6-8 | 精确计算 read 与 reference segment 的相似性 | 是 |
| Edit Distance | 编辑距离 | Page 2-3 | 两序列之间最少 edits 数 | 是 |
| q-gram Filtering | q-gram 过滤 | Page 5 | 用长度 q 的子串判断相似性 | 中 |
| Pigeonhole Principle | 鸽巢原理 | Page 4 | 若相似序列至多 E edits，则存在无错片段 | 中 |
| FASTQ/FASTA | 基因组数据格式 | Page 9 | 常用 reads/reference 表示格式 | 中 |
| GenASM | GenASM 加速框架 | Page 9 | bitvector-based ASM 加速框架 | 是 |

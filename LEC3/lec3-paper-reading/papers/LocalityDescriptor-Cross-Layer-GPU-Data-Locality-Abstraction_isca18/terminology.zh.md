# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Locality Descriptor | 局部性描述符 | Page 1-2 | 软件表达数据结构局部性、tile 关系和优化意图的跨层抽象。 | 是 |
| CTA scheduling | CTA 调度 | Page 2-3 | 把共享数据的 Cooperative Thread Arrays 调度到相同/相近资源上以提高局部性。 | 是 |
| Reuse-based locality | 基于复用的局部性 | Page 1 | 为了提高 cache 利用率而关注数据复用关系。 | 是 |
| NUMA locality | NUMA 局部性 | Page 1 | 把数据放到使用它的线程附近，减少远端访问。 | 是 |
| INTRA-THREAD / INTER-THREAD / NO-REUSE | 线程内/线程间/无复用局部性类型 | Page 5-6 | descriptor 中驱动底层优化选择的 locality type。 | 是 |

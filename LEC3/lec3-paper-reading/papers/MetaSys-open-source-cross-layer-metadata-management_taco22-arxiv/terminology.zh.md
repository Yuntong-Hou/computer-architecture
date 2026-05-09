# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Metadata | 元数据 | Page 1 | 软件传给硬件的额外语义信息，如访问模式、bounds、reuse 等。 | 是 |
| Tagged memory | 带标签内存 | Page 1 and Section 3 | 每个地址关联 tag ID，再由 ID 指向对应 metadata。 | 是 |
| Metadata Mapping Table (MMT) | 元数据映射表 | Page 4 | 保存地址范围到 tag ID 的映射，通常在内存中由 OS 管理。 | 是 |
| Metadata Mapping Cache (MMC) | 元数据映射缓存 | Page 4 | 缓存常用 MMT 映射，减少 metadata lookup 开销。 | 是 |
| Private Metadata Table (PMT) | 私有元数据表 | Page 4 | 靠近具体 optimization component 存储该模块需要的 metadata。 | 是 |

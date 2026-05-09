# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Virtual Block (VB) | 虚拟块 | Page 1-3 | 全局 VBI address space 中可变大小、语义相关的连续区域。 | 是 |
| Memory Translation Layer (MTL) | 内存翻译层 | Page 2-4 | memory controller 侧管理 allocation 和 VBI-to-physical translation 的硬件层。 | 是 |
| Client-VB Table (CVT) | 客户端-VB 表 | Page 4-6 | 记录 process/client 对哪些 VBs 有访问权限。 | 是 |
| VBI address | VBI 地址 | Page 3-4 | 由 VB ID 和 offset 构成的系统唯一地址。 | 是 |

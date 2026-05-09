# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| IMPICA | in-memory pointer chasing accelerator | Page 1 | 部署在 3D-stacked memory logic layer 的 pointer traversal 加速器。 | 是 |
| Address-access decoupling | 地址生成-访问解耦 | Page 2-4 | 在等待 memory access 时处理其他 traversal stream 的地址生成。 | 是 |
| Region-based page table | 区域式页表 | Page 2 and Page 4 | 利用连续 virtual memory regions 简化 PIM-side address translation。 | 是 |
| Pointer chasing | 指针追踪 | Page 1-2 | 通过当前 node 中的指针访问下一个 node 的串行遍历。 | 是 |

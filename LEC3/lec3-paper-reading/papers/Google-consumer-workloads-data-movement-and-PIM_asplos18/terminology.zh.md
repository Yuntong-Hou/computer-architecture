# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Processing-in-Memory (PIM) | 存内/近存处理 | Page 1-2 | 把部分计算放到 memory logic 附近，以减少主存到 CPU/GPU/accelerator 的数据搬移。 | 是 |
| PIM target | PIM 目标函数 | Page 2-3 | 能耗占比较高、以数据移动为主、适合简单近存逻辑执行的函数或 primitive。 | 是 |
| PIM core | PIM 通用核心 | Page 2, Section 3.3 | 低功耗通用 embedded core，可服务多种 target。 | 是 |
| PIM accelerator | PIM 专用加速器 | Page 2, Section 3.3 | 面向特定 target 的 fixed-function logic，通常收益更高但面积更大。 | 是 |
| Texture tiling | 纹理分块 | Page 4, Section 4.2 | Chrome 渲染中把 bitmap 转成 tiled texture 的数据整理步骤。 | 是 |

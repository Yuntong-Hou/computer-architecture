# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Panopticon | in-DRAM RowHammer 防御 | Page 1 | 在 DRAM 内部追踪 row activations 并刷新 victim rows 的完整机制。 | 是 |
| ALERTn | DDR4 错误提示信号 | Page 1 and Page 5 | 被 Panopticon 复用来暂停 controller 命令流。 | 是 |
| Counter mat | 计数器 mat | Page 4 | 与 data mat 共同布局的薄 counter 存储阵列。 | 是 |
| Service queue | 服务队列 | Page 3-5 | 保存达到 threshold 的 aggressor rows，等待刷新 victims。 | 是 |

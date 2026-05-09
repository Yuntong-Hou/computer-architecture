# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Application Slowdown Model (ASM) | 应用 slowdown 模型 | Page 1 | 在线估计共享 cache/主存干扰导致应用性能下降的模型。 | 是 |
| Cache Access Rate (CAR) | cache 访问率 | Page 2-4 | 单位时间内 shared cache accesses，用作性能代理。 | 是 |
| Auxiliary Tag Store (ATS) | 辅助 tag 存储 | Page 4-5 | 用于估计应用在无 cache contention 情况下的 cache behavior。 | 是 |
| Soft slowdown guarantee | 软 slowdown 保证 | Page 11-12 | 尽量把目标应用 slowdown 控制在用户给定 bound 内。 | 是 |

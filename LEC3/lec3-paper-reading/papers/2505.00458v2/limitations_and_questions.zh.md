# Limitations and Questions

## 1. 作者明确承认的局限
- MCC 采用难，主要挑战在 software、interfaces、frameworks 和 prototypes；位置：Page 6, Section 4。
- 需要渐进式采用路径，而不是一夜之间切换范式；位置：Page 6。

## 2. 论文中隐含的局限
- 本文是愿景/综述，未提出新硬件并独立评估。
- 引用的 PIM/PUM/SMD 案例成熟度不一，不能简单等同于可立即商用。

## 3. 实验设计可能存在的问题
- 没有统一实验平台比较 SMD、PNM、PUM 的成本收益。
- 引用结果来自不同论文、工艺、workload 和模拟/实测环境。

## 4. 方法可能不适用的场景
- 计算密度高、数据复用强、cache 友好的 workload 可能不需要 PIM。
- 需要严格一致性、安全隔离或复杂控制流的 workload 迁移到 memory 附近会更难。

## 5. 我阅读时应该追问的问题
- MCC 的最小可部署接口是什么？
- SMD、PRAC、Chronus 之间如何形成标准化演进？
- PIM 编程模型如何避免把复杂度转移给程序员？
- PUM 的可靠性、测试、错误恢复和安全边界如何定义？

## 6. 后续可以继续阅读的方向
- Modern Primer on PIM：系统读 PIM 分类。
- SMD/Chronus/PRAC：读 memory self-management。
- Tesseract、PAPI、CENT、UPMEM 相关论文：读 PNM 应用案例。

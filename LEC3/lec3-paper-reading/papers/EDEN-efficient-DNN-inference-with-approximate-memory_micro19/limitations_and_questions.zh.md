# Limitations and Questions

## 1. 作者明确承认的局限
- error model 必须足够贴合真实 DRAM；poor-fit model retraining 效果差；位置：Page 10, Figure 10。
- performance speedup 主要出现在 latency-bound networks；位置：Page 12。

## 2. 论文中隐含的局限
- 需要 retraining 和 profiling，部署前成本不低。
- 环境温度、老化、data pattern 变化可能让 error model 过期。
- 2019 DNN 工作负载不覆盖现代 Transformer/LLM。

## 3. 实验设计可能存在的问题
- 部分系统结果基于模拟器和 error model，而非全系统真实 approximate DRAM 部署。
- fine-grained mapping 需要 memory controller/OS/runtime 支持，实际复杂度较高。

## 4. 方法可能不适用的场景
- 对 accuracy safety 极严、不能容忍任何偶发错误的场景。
- 对没有 retraining 权限的闭源模型或动态模型。
- 对 error distribution 快速变化的 DRAM。

## 5. 我阅读时应该追问的问题
- EDEN 能否用于 transformer/LLM KV cache 和 weights？
- on-die ECC 会如何改变 approximate DRAM errors？
- runtime 如何监测 BER drift？
- fine-grained mapping 与 page allocator 如何集成？

## 6. 后续可以继续阅读的方向
- Voltron、Flexible-Latency DRAM、DIVA-DRAM。
- ApproxANN / DNN error resilience。
- PIM for DNN inference。

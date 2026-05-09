# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Self-Managing DRAM (SMD) | 自管理 DRAM | Page 1 | 让 DRAM 自主执行维护操作的框架 | 是 |
| maintenance operation | 维护操作 | Page 1 | refresh、RowHammer protection、scrubbing 等保持可靠性的操作 | 是 |
| ACT_NACK | 激活拒绝信号 | Page 4-5 | DRAM 拒绝对锁定区域的 ACT command 的信号 | 是 |
| lock region | 锁定区域 | Page 4 | bank 中可被维护机制临时锁定的小区域 | 是 |
| Lock Controller | 锁控制器 | Page 4-6 | 记录并管理 region 是否正在维护的结构 | 是 |
| ACT Retry Interval (ARI) | ACT 重试间隔 | Page 5 | MC 收到 ACT_NACK 后等待的时间 | 是 |
| DRAM refresh | DRAM 刷新 | Page 7 | 周期性恢复 DRAM cell 电荷 | 是 |
| RowHammer protection | RowHammer 防护 | Page 8-10 | 防止高频激活 aggressor row 导致 victim row bit-flip | 是 |
| memory scrubbing | 内存巡检/擦洗 | Page 11-12 | 定期读取并纠正内存错误 | 是 |
| DARP | Dynamic Access Refresh Parallelization | Page 13-15 | memory controller 侧的 refresh scheduling/parallelization 技术 | 中 |
| DSARP | Dynamic Subarray Access Refresh Parallelization | Page 13-15 | 支持 subarray-level refresh-access parallelization 的机制 | 中 |
| No-Refresh | 无刷新 oracle | Page 13-14 | 假想完全消除维护开销的上界 | 中 |
| SMD-FR | SMD fixed-rate refresh | Page 7 | 固定频率的 SMD refresh 实现 | 是 |
| SMD-VR | SMD variable-rate refresh | Page 8 | 基于 retention variation 的 SMD refresh | 是 |
| SMD-PRP | SMD probabilistic RowHammer protection | Page 9 | SMD 版概率 RowHammer 防护 | 是 |
| SMD-DRP | SMD deterministic RowHammer protection | Page 10 | SMD 版确定性 RowHammer 防护 | 是 |
| SMD-MS | SMD memory scrubbing | Page 11-12 | SMD 版内存巡检 | 是 |

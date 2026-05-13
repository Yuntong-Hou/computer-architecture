# Extraction Log

- Input Type: GitHub repository PDF
- Source: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/ambit-bulk-bitwise-dram_micro17.pdf
- Local PDF: lec4-paper-reading/sources/original-paper/ambit-bulk-bitwise-dram_micro17.pdf
- Extracted Text: lec4-paper-reading/extracted_text/ambit-bulk-bitwise-dram_micro17.txt
- Access Status: Public PDF downloaded through GitHub API/raw URL
- Full Text Retrieved: Yes
- PDF Pages: 15
- Sections Detected: Abstract; 1 Introduction; 2 DRAM Background; 3 Ambit-AND-OR; 4 Ambit-NOT; 5 Design and System Integration; 6 SPICE Simulations; 7 Throughput and Energy; 8 Applications; 9 Related Work; References
- Figures Detected: Yes, figure captions detected in extracted text
- Tables Detected: Yes, table captions detected in extracted text
- Equations Detected: Yes
- Appendix Detected: 未检测到明确 appendix
- Supplementary Material Detected: 未检测到
- OCR Used: No
- Missing Content: 图像本体未裁剪；公式/图形细节建议回到 PDF 人工查看
- Parsing Problems: 双栏 PDF 的部分行在抽取文本中交错；已用页码、章节和图表编号辅助定位
- Uncertain Parts: DOI、正式会议/期刊信息若 PDF 未显式给出则标为“未找到”或 arXiv
- Need User Action: 如需逐图截图或逐字全文翻译，请确认版权/用途并指定优先论文

## Quality Self-Check

- [x] 已读取 PDF 抽取文本，不只依据标题或摘要
- [x] 已覆盖背景、方法、实验、结果、局限
- [x] 已记录关键原文位置
- [x] 已整理图表/公式笔记
- [x] 已整理术语表
- [x] 已标注无法确认或需人工复核内容

## 2026-05-12 High-Completeness Translation Expansion

- Updated File: full_translation.zh.md
- Expansion Scope: 追加高完整度扩写版，覆盖 bulk bitwise workloads、TRA majority、DCC NOT、designated rows、AAP primitive、system interface、coherence/ECC/scrambling、SPICE reliability、throughput/energy、applications、limitations。
- Hardware Engineer Perspective Added: Yes，重点补充 sense amplifier 计算、designated-row 工程折中、subarray placement、ECC/scrambling/coherence、bitcount/reduction 边界。
- Current Translation File Length: 213 lines
- Remaining Manual Check: Page 4-6 TRA/DCC 图和 Page 10-12 性能图建议回 PDF 原图核对。

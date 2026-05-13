# Extraction Log

- Input Type: GitHub repository PDF
- Source: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/in-dram-bulk-and-or-ieee_cal15.pdf
- Local PDF: lec4-paper-reading/sources/original-paper/in-dram-bulk-and-or-ieee_cal15.pdf
- Extracted Text: lec4-paper-reading/extracted_text/in-dram-bulk-and-or-ieee_cal15.txt
- Access Status: Public PDF downloaded through GitHub API/raw URL
- Full Text Retrieved: Yes
- PDF Pages: 4
- Sections Detected: Abstract; 1 Introduction; 2 Background on DRAM Operation; 3 In-DRAM AND and OR; 4 Latency, Throughput, and Energy Analysis; 5 Analysis of a Real-World Bitmap Index; 6 Related Work; 7 Conclusion; References
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
- Expansion Scope: 追加高完整度扩写版，覆盖 Abstract、Introduction、DRAM background、triple-row activation、RowClone 临时行流程、latency/throughput/energy、FastBit case study、related work、conclusion。
- Hardware Engineer Perspective Added: Yes，重点补充 destructive compute、subarray locality、临时行/常量行、cache coherence、ECC、timing guardband、应用筛选条件。
- Current Translation File Length: 246 lines
- Remaining Manual Check: Page 2 Figure 4 的 majority/triple-row activation 建议结合原图复核。

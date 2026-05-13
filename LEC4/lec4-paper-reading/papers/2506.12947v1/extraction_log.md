# Extraction Log

- Input Type: GitHub repository PDF
- Source: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/2506.12947v1.pdf
- Local PDF: lec4-paper-reading/sources/original-paper/2506.12947v1.pdf
- Extracted Text: lec4-paper-reading/extracted_text/2506.12947v1.txt
- Access Status: Public PDF downloaded through GitHub API/raw URL
- Full Text Retrieved: Yes
- PDF Pages: 20
- Sections Detected: Abstract; 1 Introduction; 2 Background; 3 Methodology; 4 CoMRA Read Disturbance; 5 SiMRA Read Disturbance; 6 Combined RowHammer and PuDHammer; 7 TRR; 8 Countermeasures; 9 Related Work; 10 Conclusion; References
- Figures Detected: Yes, figure captions detected in extracted text
- Tables Detected: Yes, table captions detected in extracted text
- Equations Detected: No core numbered equations detected in extracted text
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
- Expansion Scope: 追加高完整度扩写版，覆盖 CoMRA/SiMRA、HCfirst、真实 DDR4 表征、RowHammer/TRR bypass、PRAC countermeasures、limitations。
- Hardware Engineer Perspective Added: Yes，重点补充 PuD 多行激活的 read disturbance 风险、tail vulnerability、mitigation counter 成本、安全产品化边界。
- Current Translation File Length: 224 lines
- Remaining Manual Check: Page 5、Page 9、Page 12、Page 14 的关键图建议回 PDF 原图核对。

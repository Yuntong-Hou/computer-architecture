# Extraction Log

- Input Type: GitHub repository PDF
- Source: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/simdram_asplos21.pdf
- Local PDF: lec4-paper-reading/sources/original-paper/simdram_asplos21.pdf
- Extracted Text: lec4-paper-reading/extracted_text/simdram_asplos21.txt
- Access Status: Public PDF downloaded through GitHub API/raw URL
- Full Text Retrieved: Yes
- PDF Pages: 21
- Sections Detected: Abstract; 1 Introduction; 2 Background; 3 SIMDRAM Overview; 4 SIMDRAM Framework; 5 System Integration; 6 Methodology; 7 Evaluation; 8 Related Work; 9 Conclusion; Appendix; References
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
- Expansion Scope: 追加高完整度扩写版，覆盖 motivation、DRAM/Ambit background、SIMDRAM subarray organization、MAJ/NOT synthesis、row allocation、µOps/µProgram、system integration、programming interface、transposition、evaluation、reliability、data movement、limitations、conclusion。
- Hardware Engineer Perspective Added: Yes，重点补充 vertical layout、destructive MAJ row allocation、coherence/pinning、RowHammer/security、transposition overhead、适用 workload 边界。
- Current Translation File Length: 257 lines
- Remaining Manual Check: Appendix 的 MIG transformation rules 和 Page 12-15 的评估图建议回 PDF 原图核对。

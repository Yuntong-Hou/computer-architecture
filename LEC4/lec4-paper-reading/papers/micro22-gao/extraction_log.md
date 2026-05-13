# Extraction Log

- Input Type: GitHub repository PDF
- Source: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/micro22-gao.pdf
- Local PDF: lec4-paper-reading/sources/original-paper/micro22-gao.pdf
- Extracted Text: lec4-paper-reading/extracted_text/micro22-gao.txt
- Access Status: Public PDF downloaded through GitHub API/raw URL
- Full Text Retrieved: Yes
- PDF Pages: 15
- Sections Detected: Abstract; I Introduction; II Background; III Primitive Operations; IV Evaluation Methodology; V Evaluation; VI Use Cases; VII Related Work; VIII Conclusion; References
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
- Expansion Scope: 追加高完整度扩写版，覆盖 Abstract、Introduction、Background、Frac/Half-m primitives、verification methodology、Frac/Half-m evaluation、F-MAJ、Frac-based PUF、other uses、related work、conclusion。
- Hardware Engineer Perspective Added: Yes，重点补充 fractional value 的 destructive readout、refresh/ECC 风险、F-MAJ 校准意义、PUF enrollment/environment/aging、ternary storage 未成熟边界。
- Current Translation File Length: 288 lines
- Remaining Manual Check: Page 5-8 的 retention/MAJ3 验证图和 Page 10-12 的 PUF 分布图建议回 PDF 原图核对。

---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3282
issue_type: ''
status: ''
tags:
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3282
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: partial
---
EPMTDCPROT-3282: 

| 問題

Award Recommendation 表單中，PO 金額驗證（Checking against supplier's quote per Item Category）錯誤地對所有 Item Group 的總金額進行校驗，包含未被選中授予（award）的 Item Group，而非僅校驗已選中授予的 Item Group 金額總和。

| 根因

系統的 PO 金額驗證邏輯在計算總金額基準時，將未選中授予的 Item Group 金額也納入計算，導致驗證比較基準不正確。Description 明確指出：「system validation is against the total tender price which unselected items are included」。

| 解法

修正驗證邏輯，使 PO 金額僅與已選中授予（awarded）的 Item Group 總金額進行比對，排除未選中的 Item Group。Jeffrey wen 在 UAT 環境驗證：當 PO amount 超過 awarded offer amount 時正確觸發 validation reminder，test passed。

| 相關資訊

- Jira: [EPMTDCPROT-3282](https://ctil.atlassian.net/browse/EPMTDCPROT-3282)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT | 附件: [72440](https://ctil.atlassian.net/rest/api/3/attachment/content/72440) | [72444](https://ctil.atlassian.net/rest/api/3/attachment/content/72444) |

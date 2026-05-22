---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1902
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
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1902
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---
EPMTDCPROT-1902: 

| 問題

在 Opening Team Record 中進行 Technical Proposal Compliance Check 時，無回應（No Response）供應商的狀態標籤顯示不正確，應顯示為「No Response」。

| 根因

前端/後端對供應商「無回應」狀態對應的顯示標籤配置錯誤，未正確映射至「No Response」文字標籤。

| 解法

修正標籤映射邏輯，確保無回應供應商在 Compliance Check 介面中正確顯示為「No Response」。Benson Xu 確認已 fixed，Gavin Zhou 確認 uat pass。

| 相關資訊

- Jira: [EPMTDCPROT-1902](https://ctil.atlassian.net/browse/EPMTDCPROT-1902)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT | 附件: [57905](https://ctil.atlassian.net/rest/api/3/attachment/content/57905) | [57906](https://ctil.atlassian.net/rest/api/3/attachment/content/57906) | [57980](https://ctil.atlassian.net/rest/api/3/attachment/content/57980) | [58378](https://ctil.atlassian.net/rest/api/3/attachment/content/58378) |

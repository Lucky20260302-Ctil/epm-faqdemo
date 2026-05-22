---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3395
issue_type: ''
status: ''
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3395
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---
EPMTDCPROT-3395: EPRO-938 [Production] Validation of Info Change form only checks if a row is added but not if any information is inputte

| 問題

在 Info Change form 的 Client Reference 區段中，只新增了空白列但未填入任何資訊，Validation 卻通過了，為什麼？

| 根因

根據 Comment (Gavin Zhou)：原先 Info Change form 的驗證邏輯僅檢查「是否新增了一列」（row existence），並未檢查該列中各個必填欄位是否實際填入了內容，導致空白列也能通過驗證。

| 解法

修正 Client Reference 區段的驗證邏輯，改為逐一檢查每個必填欄位（mandatory fields）是否有實際輸入內容，而非僅檢查列是否存在。

| 相關資訊

- Jira: [EPMTDCPROT-3395](https://ctil.atlassian.net/browse/EPMTDCPROT-3395)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT

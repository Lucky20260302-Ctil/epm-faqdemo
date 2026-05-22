---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1052
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
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1052
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-1052: 

## 症狀

在 Supplier Invitation Request (Pre-Reg) 中，勾選 Exception Approval 並選擇 Online 後，若未填寫任何 Approvaler 即提交，系統回傳 500 錯誤；若不選擇 Online 直接進行後續操作，同樣回傳 500 錯誤。

## 根因

後端在處理 Exception Approval 流程時，未對必要參數（Online 選項、Approvaler）進行伺服器端校驗，導致參數缺失時觸發未處理的 Null Reference 異常，回傳 HTTP 500。

## 解法

後端修正了 Exception Approval 流程的參數校驗邏輯，確保 Online 選項與 Approvaler 為必填時先進行驗證再執行後續動作，避免未處理異常。最後由 Jett.He 確認 bug is fixed。

## 相關資訊

- Jira: [EPMTDCPROT-1052](https://ctil.atlassian.net/browse/EPMTDCPROT-1052)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT | 附件: [53186](https://ctil.atlassian.net/rest/api/3/attachment/content/53186) | [54876](https://ctil.atlassian.net/rest/api/3/attachment/content/54876) |

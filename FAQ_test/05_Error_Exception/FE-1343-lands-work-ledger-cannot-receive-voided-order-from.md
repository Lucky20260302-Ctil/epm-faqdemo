---
project: FE
issue_key: FE-1343
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1343
created: '2024-02-15'
resolved: '2024-02-16'
fix_version: v760.01R03R
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1343: work ledger cannot receive voided order from shopping cart

| 問題
Lands 工作帳本無法接收從購物車 void 的訂單，API 呼叫失敗。

| 根因
Void Lands Order 呼叫 Lands Web API 時的例外處理與日誌記錄不完善，導致 API 發送失敗未被正確捕捉。

| 解法
增強例外處理機制與日誌記錄，已於 KTS 240208 V760.01R03R 修復。

| 相關資訊
- Jira: [FE-1343](https://ctil.atlassian.net/browse/FE-1343)
- Fix Version: v760.01R03R
- 解決日期: 2024-02-16
- 組件: Front End
- 負責人: Sang
- 附件: [RE_ Void Memo Call Lands Web API - V760_01R03R.msg](https://ctil.atlassian.net/rest/api/3/attachment/content/37934)
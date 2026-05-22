---
project: FE
issue_key: FE-1547
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1547
created: '2024-11-04'
resolved: '2024-11-05'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1547: Fail to display mutiple member results when backend DB has more than 1 same telephone number

| 問題
在 Coach POS 中，使用電話號碼搜尋會員時，若後端資料庫存在多筆相同電話號碼的會員紀錄，前端畫面僅顯示載入中狀態，無法顯示多重會員搜尋結果，亦無任何錯誤訊息提示。

| 根因
系統設定 tblconfig.ONLINERETRIEVEFIRSTMEMONLY 未被正確設定為 'N'（允許回傳多重會員），導致前端僅期待單一結果，無法處理多筆回傳資料。Acxiom CRM 的 Web API 雖可返回多重會員集合，但前端未啟用對應的選擇功能。

| 解法
將 tblconfig.ONLINERETRIEVEFIRSTMEMONLY 設定為 'N'，啟用前端多重會員選擇功能。此修正已包含於 v750.04R09 及 v750.05 版本（KTS 241104）。

| 相關資訊
- Jira: [FE-1547](https://ctil.atlassian.net/browse/FE-1547)
- 解決日期: 2024-11-05
- 組件: Front End
- 負責人: Sang
- 附件: [image-20241104-104502.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47701) | [image-20241105-023351.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47937)
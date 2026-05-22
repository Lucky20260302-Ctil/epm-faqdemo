---
project: FE
issue_key: FE-1665
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1665
created: '2025-03-31'
resolved: '2025-03-31'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1665: Click on Profile no response when member who is not existing in CRM

| 問題
Coach 品牌 POS 套用不存在於 CRM 系統中的會員時，點擊「Profile」按鈕沒有任何反應，點擊「Purchase History」則彈出「Object reference not set to an instance of an object」錯誤。此情況發生於會員資料存在於後端資料庫但不存在於 CRM 系統時。

| 根因
BEAPI 對於不存在於 CRM 的會員回傳 jsonData 為 null，前端程式（FEPOS）未處理此 null 值，導致 NullReferenceException。點擊 Profile 時因 null 值造成靜默失敗無反應，點擊 Purchase History 時則觸發未處理的例外錯誤。

| 解法
此問題已在 v750.04R11A 版本中修復，修復範圍包含 v750.04R11A、v750.04R12 及 v75.05 分支。修復後，對於不存在於 CRM 的會員，點擊 Profile 和 Purchase History 時會顯示「Profile not available」提示訊息，而非無反應或錯誤彈窗。

| 相關資訊
- Jira: [FE-1665](https://ctil.atlassian.net/browse/FE-1665)
- 解決日期: 2025-03-31
- 組件: Front End
- 負責人: Sang
- 附件: [image-20250331-074613.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54007) | [image-20250331-085033.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54015)
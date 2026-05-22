---
project: FE
issue_key: FE-1700
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1700
created: '2025-05-22'
resolved: '2025-07-31'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1700: Exchange order show incorrect Misc amount after select MM coupon

| 問題
Coach 品牌進行換貨（Exchange）交易並使用 Gain 退款方式時，在付款介面加入再刪除 MM Coupon 後，返回付款方式頁面時 Misc 金額顯示不正確，導致金額計算異常。

| 根因
POS 前端在處理 Exchange + Gain 退款流程中，當用戶於付款步驟增刪 MM Coupon 後返回付款方式頁面時，Misc（雜項金額）欄位的重算邏輯未正確處理優惠券變動後的狀態，導致殘留錯誤的 Misc 數值。

| 解法
開發團隊修正了 Exchange 訂單中 Gain Excess Amt 的 Misc 金額計算邏輯，確保增刪 MM Coupon 後返回付款頁面時金額正確重算。修正版本：v750.04R13B、v750.05（KTS 250529）。

| 相關資訊
- Jira: [FE-1700](https://ctil.atlassian.net/browse/FE-1700)
- 解決日期: 2025-07-31
- 組件: Front End
- 負責人: Sang
- 附件: [image-20250522-094910.png](https://ctil.atlassian.net/rest/api/3/attachment/content/57743) | [image-20250529-073941.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58374) | [image-20250529-073952.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58375)
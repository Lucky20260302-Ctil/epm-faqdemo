---
project: FE
issue_key: FE-1837
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1837
created: '2025-12-19'
resolved: '2026-03-25'
fix_version: FE-75.004.2200.0000
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1837: An error occurs when setting the POS of the cash drawer balance to 'All'.

| 問題
當POS櫃檯現金抽屜餘額查詢選擇「All」（全部櫃檯）時，系統顯示錯誤訊息「Sorry, cannot connect to the main-till, do you want to change the till to standalone mode?」。單獨查詢自己的櫃檯正常，但查詢其他櫃檯或全部櫃檯時出現此錯誤。所有V75版本的櫃檯均有此問題，V72版本則正常。

| 根因
櫃檯POS在彙整多個櫃檯的現金抽屜資料時，無法透過SSE（Shop Server Engine）連線取得其他櫃檯的彙總資料，導致連線逾時並觸發獨立模式（standalone mode）錯誤訊息。此問題存在於特定的V75.04版本中，為已知的程式缺陷，後續版本已修復。

| 解法
將POS版本升級至v750.04R21或更新版本，該版本已包含此問題的修復。若尚未升級，可先使用個別收銀員ID（cashier_id）進行查詢作為暫時替代方案，此方式可正常取得資料而不觸發錯誤。修復版本：v750.04R13I/R14+，最終確認納入R21版本。

| 相關資訊
- Jira: [FE-1837](https://ctil.atlassian.net/browse/FE-1837)
- Fix Version: FE-75.004.2200.0000
- 解決日期: 2026-03-25
- 組件: Front End
- 負責人: Sherman tse
- 附件: [DAL20251218.log](https://ctil.atlassian.net/rest/api/3/attachment/content/71365) | [DAL20251218 (aefc551e-007e-4bce-9eaa-6360ffbe485d).log](https://ctil.atlassian.net/rest/api/3/attachment/content/71454) | [image-20251219-100101.png](https://ctil.atlassian.net/rest/api/3/attachment/content/71362) | [image-20251219-100258.png](https://ctil.atlassian.net/rest/api/3/attachment/content/71361) | [image-20251222-032901.png](https://ctil.atlassian.net/rest/api/3/attachment/content/71456)
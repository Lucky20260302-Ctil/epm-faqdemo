---
project: FE
issue_key: FE-1440
issue_type: Bug QA
status: Closed
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1440
created: '2024-06-28'
resolved: '2024-07-09'
fix_version: v750.01R02J
components:
- Front End
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: partial
---
FE-1440: REMS - Member search in offline mode will result in execption

| 問題
在 HKJC REMS 系統的離線模式（TBLCONFIG.ENABLEDASEC = 'N' 且網路已停用）下，使用 QR Code 搜尋會員時會出現例外錯誤訊息。此問題發生於 POS 無法連接後端服務時，前端無法正確處理會員查詢請求。

| 根因
離線模式下，前端搜尋邏輯未完整支援透過 QR Code 所攜帶的會員編號（Member No）、身份證號（ID No）、職員編號（Staff No）、投注編號（Betting No）及 PCard 等多種識別碼進行本地查詢，導致程式拋出例外。

| 解法
開發人員在 v750.01R02H 版本中修正了離線模式下的會員搜尋邏輯，使其可比對 PCard 與投注編號。後續在 v750.01R02J 進一步擴充支援會員編號、身份證號、職員編號等多種搜尋條件，並加入 POS 啟動及 Z-file 更新時自動同步 vipmas_Id_no 及 vipmas_Staff_Code 欄位。修復版本：v750.01R02J。

| 相關資訊
- Jira: [FE-1440](https://ctil.atlassian.net/browse/FE-1440)
- Fix Version: v750.01R02J
- 解決日期: 2024-07-09
- 組件: Front End
- 負責人: Sang
- 附件: [DAL20240702.log](https://ctil.atlassian.net/rest/api/3/attachment/content/42702) | [image-20240701-053923.png](https://ctil.atlassian.net/rest/api/3/attachment/content/42650) | [image-20240701-054019.png](https://ctil.atlassian.net/rest/api/3/attachment/content/42651) | [image-20240702-085932.png](https://ctil.atlassian.net/rest/api/3/attachment/content/42703) | [image-20240702-085939.png](https://ctil.atlassian.net/rest/api/3/attachment/content/42704)
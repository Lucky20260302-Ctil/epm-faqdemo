---
project: "FE"
issue_key: "FE-1645"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1645"
created: "2025-03-10"
resolved: "2025-03-21"
fix_version: ""
components: [Front End]
category: "05_Error_Exception"
---

FE-1645: Always message 'This member does not consent to enquire out of border' while searching CN member which is existing in HK

| 問題
在香港 POS 查詢已存在於香港後台資料庫的中國（CN）會員時（透過手機號碼或會員編號），系統持續顯示「This member does not consent to enquire out of border」訊息，無法顯示該 CN 會員的資訊。

| 根因
根據 CBDT 設計規範，當 HK/MO 查詢 CN 會員紀錄（vip_comp_code = 11）時，會先透過 CDP 客戶隱私檢查 API 驗證，若該客戶未在 CDP 系統中註冊（API 回傳 CDP-CUST-404），則隱私檢查失敗，系統顯示跨境拒絕訊息。此為符合 CBDT 設計的預期行為。

| 解法
此為 CBDT 設計規範下的預期行為：HK/MO 查詢 CN 會員時，會員姓名與電話號碼將被遮罩處理，Tapestry 已接受此設計。若需完整顯示 CN 會員資訊，需確保該會員已在 CDP 系統中完成註冊並授權跨境查詢。

| 相關資訊
- Jira: [FE-1645](https://ctil.atlassian.net/browse/FE-1645)
- 解決日期: 2025-03-21
- 組件: Front End
- 負責人: Anson Cheung
- 附件: [beapi_apilog_20250307.sqlite](https://ctil.atlassian.net/rest/api/3/attachment/content/52844) | [beapi_apilog_20250307 (d88dc7e4-34e6-4fdd-90b0-264716885d87).sqlite](https://ctil.atlassian.net/rest/api/3/attachment/content/52845) | [image-20250310-065245.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52768) | [image-20250310-070046.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52770) | [image-20250311-023438.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52818)
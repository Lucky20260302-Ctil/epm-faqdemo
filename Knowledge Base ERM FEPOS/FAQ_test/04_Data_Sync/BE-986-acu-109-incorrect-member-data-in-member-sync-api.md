---
project: "BE"
issue_key: "BE-986"
issue_type: "Bug QA"
status: "Closed"
tags: [faq, be]
jira_url: "https://ctil.atlassian.net/browse/BE-986"
created: "2025-01-15"
resolved: "2025-03-06"
fix_version: ""
components: [API]
category: "04_Data_Sync"
---

BE-986: Incorrect Member data in Member Sync API

| 問題
Member Sync API（v2/cdp/member/pos/sync）回傳的會員資料中，部分布林欄位（如 address_flag）應回傳 Y/N，但實際卻回傳 0/1 的數值格式，導致呼叫端資料更新異常。此問題影響 ACXIOM CRM 會員資料的同步流程。

| 根因
POS 系統透過 BEAPI 更新後端 VIP 記錄時，若 CRM 回傳的會員有效期（expiry date）與本地記錄不符，現有邏輯會拒絕此次更新，以防止 API 意外覆寫有效期。當更新被拒絕後，部分欄位的資料格式未正確轉換（0/1 vs Y/N），導致同步資料異常。

| 解法
在 BEAPI v1.6.20 版本中加入針對 ACXIOM CRM 的設定選項，允許繞過有效期檢查並直接以 CRM 資料覆寫本地 VIP 記錄中的會員資料。Release：\\ds411\public\samuel\beapi\v1.6.20_20250115。2025年3月4日完成 QA 驗證。

| 相關資訊
- Jira: [BE-986](https://ctil.atlassian.net/browse/BE-986)
- 解決日期: 2025-03-06
- 組件: API
- 負責人: Sherman tse
- 附件: [image-20250115-093123.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50529) | [image-20250303-102424.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52401) | [Test case of ACU-109-Incorrect Member data in Member Sync API (AutoRecovered).xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/52408)
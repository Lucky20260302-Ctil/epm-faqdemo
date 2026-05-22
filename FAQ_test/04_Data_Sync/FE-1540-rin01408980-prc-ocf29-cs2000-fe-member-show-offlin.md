---
project: "FE"
issue_key: "FE-1540"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1540"
created: "2024-10-24"
resolved: ""
fix_version: ""
components: [Front End]
category: "04_Data_Sync"
---

FE-1540: RIN01408980 - PRC - OCF29 - CS2000 - FE : member show offline on CS2000 FE

| 問題
在CS2000 FE查詢會員資料時，系統顯示「會員升級訊息(離線)」，但此問題會在未進行任何操作的情況下自行恢復，造成門市人員困惑。

| 根因
第一次查詢會員時FE從後端資料庫取得會員資料並寫入暫存資料表，顯示為線上狀態；第二次查詢同一會員時FE直接從暫存資料表讀取，因未重新連接後端而顯示為離線狀態。此為FE暫存資料表快取機制導致的設計問題。

| 解法
CN V75版本將改由CRM直接擷取會員資料，因此不會再發生此問題。V75以下版本需注意此暫存快取機制導致的離線顯示現象，可透過重新查詢或清除暫存來暫時解決。

| 相關資訊
- Jira: [FE-1540](https://ctil.atlassian.net/browse/FE-1540)
- 組件: Front End
- 負責人: Sang
- 附件: [DAL20241018_OCF1_Till7.log](https://ctil.atlassian.net/rest/api/3/attachment/content/47440) | [image-20241024-015401.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47349) | [image-20241024-015516.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47350) | [image-20241025-013530.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47376) | [image-20241025-061017.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47401)
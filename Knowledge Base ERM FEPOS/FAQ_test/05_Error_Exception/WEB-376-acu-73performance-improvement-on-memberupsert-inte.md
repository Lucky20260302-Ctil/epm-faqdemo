---
project: "WEB"
issue_key: "WEB-376"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, web]
jira_url: "https://ctil.atlassian.net/browse/WEB-376"
created: "2024-12-05"
resolved: "2025-01-03"
fix_version: "BE-V70R3.78"
components: [API]
category: "05_Error_Exception"
---

WEB-376: Performance Improvement on member/upsert Interface of POS

| 問題
POS 的 member/upsert API 效能低落：單次呼叫回應時間超過 4 秒（預期 <200ms），且當同時連線數超過 25 個 vusers 時，API 開始出現失敗呼叫並變為不可用狀態。錯誤訊息顯示資料庫發生 deadlock：『Transaction was deadlocked on lock resources with another process and has been chosen as the deadlock victim』。

| 根因
經觀察與分析，deadlock 問題極可能由對 'wtmnlog' 資料表的並行讀寫操作所引起。多個併發請求同時對 wtmnlog 表進行寫入時，SQL Server 發生鎖定資源競爭，導致其中一個交易被選為 deadlock victim 而強制終止，連帶影響整體 API 回應時間及可用性。

| 解法
若 wtmnlog 表的寫入並非必要，可在 appsettings.json 中將 'wtmnlog' 設定設為 'N' 以跳過該記錄寫入，從而消除 deadlock 根源。正式修復版本：BE-V70R3.78（於 2025-01-03 發佈）。

| 相關資訊
- Jira: [WEB-376](https://ctil.atlassian.net/browse/WEB-376)
- Fix Version: BE-V70R3.78
- 解決日期: 2025-01-03
- 組件: API
- 負責人: Sherman tse
- 附件: [CRM program logs.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/49017) | [image-20241205-062441.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49009) | [image-20241206-063233.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49052) | [image-20241206-064903.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49051) | [QA web21_beapi_apilog_20241205.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/49043)
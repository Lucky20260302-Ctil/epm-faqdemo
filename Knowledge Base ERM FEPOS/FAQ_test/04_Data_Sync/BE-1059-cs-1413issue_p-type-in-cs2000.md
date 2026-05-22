---
project: "BE"
issue_key: "BE-1059"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, be]
jira_url: "https://ctil.atlassian.net/browse/BE-1059"
created: "2025-04-28"
resolved: "2025-07-04"
fix_version: "BE-V70R3.101"
components: [API]
category: "04_Data_Sync"
---

BE-1059: Issue_P type in CS2000

| 問題
當API回傳P類型會員時，CS2000應將「P」自動轉換為「C」類型，但CS2000未進行轉換，直接將「P」傳送給POS，導致會員類型錯誤。

| 根因
非同步插入工作流程（Async Insertion）導致資料直接傳遞至FEPOS，繞過了會員類型轉換邏輯。當背景服務進行upsert操作時，P類型會員未正確觸發轉換為C類型的程序。

| 解法
更新BEAPI至V1.07.18版本（隨BE-V70R3.101於2025-04-26發布），該版本修正了背景服務執行upsert時P類型會員未轉換為C類型的問題。相關Jira：FE-1678。

| 相關資訊
- Jira: [BE-1059](https://ctil.atlassian.net/browse/BE-1059)
- Fix Version: BE-V70R3.101
- 解決日期: 2025-07-04
- 組件: API
- 負責人: Sherman tse
- 附件: [image-20250428-004323.png](https://ctil.atlassian.net/rest/api/3/attachment/content/55780)
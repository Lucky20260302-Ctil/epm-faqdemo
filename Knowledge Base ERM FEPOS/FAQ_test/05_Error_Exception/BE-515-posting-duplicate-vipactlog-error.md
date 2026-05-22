---
project: "BE"
issue_key: "BE-515"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, be]
jira_url: "https://ctil.atlassian.net/browse/BE-515"
created: "2021-08-18"
resolved: "2021-08-24"
fix_version: "BE-V70R2.63"
components: [Backend (ChainStorePlus 7.0)]
category: "05_Error_Exception"
---

BE-515: Posting - duplicate vipactlog error

| 問題
Posting 程式在執行時拋出「Cannot insert duplicate key in object vipactlog」錯誤，導致日結過帳失敗。

| 根因
多個 posting node 同時建立新會員記錄（race condition），導致 vipactlog 表中產生重複主鍵衝突。

| 解法
升級至 BE-V70R2.63，該版本修正了多節點併發建立會員時的重複鍵寫入邏輯。注意：此問題在 QA 環境難以重現，屬生產環境併發情境。

| 相關資訊
- Jira: [BE-515](https://ctil.atlassian.net/browse/BE-515)
- Fix Version: BE-V70R2.63
- 解決日期: 2021-08-24
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Joy Li
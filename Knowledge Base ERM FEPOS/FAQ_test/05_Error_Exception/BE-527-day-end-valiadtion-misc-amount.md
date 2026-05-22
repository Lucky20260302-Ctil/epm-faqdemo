---
project: "BE"
issue_key: "BE-527"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, be]
jira_url: "https://ctil.atlassian.net/browse/BE-527"
created: "2021-10-26"
resolved: "2021-10-26"
fix_version: "BE-V70R2.69"
components: [Backend (ChainStorePlus 7.0)]
category: "05_Error_Exception"
---

BE-527: Day end valiadtion (Misc Amount)

| 問題
執行 Day End posting 與 Day End validation 時，因 Misc Amount 驗算錯誤導致日結無法標記為 Y（完成）。

| 根因
Misc Amount 的計算邏輯存在偏差，導致日結驗證時金額核對失敗。

| 解法
修正 Misc Amount 的計算邏輯，升級至 BE-V70R2.69。重現步驟：建立含 Misc Amount 的 Sales Memo → 執行 Day End → 上傳銷售及日結記錄即可觸發。

| 相關資訊
- Jira: [BE-527](https://ctil.atlassian.net/browse/BE-527)
- Fix Version: BE-V70R2.69
- 解決日期: 2021-10-26
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Joy Li
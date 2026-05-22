---
project: "FE"
issue_key: "FE-1318"
issue_type: "Task"
status: "Closed"
tags: [faq, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1318"
created: "2023-11-30"
resolved: "2024-05-07"
fix_version: "v720.02R26A, v750.04"
components: [Front End]
category: "07_Workflow_Business"
---

FE-1318: HK eName follow up - pre-scan vip barcode before submit

| 問題
在 eName 註冊提交前掃描 VIP 條碼，交易過程中無法查詢到 VIP 資料（VIP 姓名顯示為空白或 '-'）。此問題影響香港地區的 Coach eName 流程，因為 CBDT 隱私政策限制，API 只會查詢一次 VIP 資料。

| 根因
HK eName 流程因 CBDT 機制僅呼叫一次線上會員 API 查詢 VIP，但 eName 註冊在提交前 VIP 尚未建立於 BE，導致第一次查詢時無法取得會員資料。而 FE 不會進行第二次查詢，因此 VIP 資訊遺失。

| 解法
增強程式邏輯：在列印時新增第二次 API 查詢。若第一次查詢結果 VIP 姓名為 '-' 或空白，則執行第二次查詢以取得完整會員資料。此修正僅適用於 Coach（CompanyCode 以 'COACH' 開頭）且排除 COACHJP 及 KS_JP。修正版本：v720.02R26A, v750.04。

| 相關資訊
- Jira: [FE-1318](https://ctil.atlassian.net/browse/FE-1318)
- Fix Version: v720.02R26A, v750.04
- 解決日期: 2024-05-07
- 組件: Front End
- 負責人: Sang
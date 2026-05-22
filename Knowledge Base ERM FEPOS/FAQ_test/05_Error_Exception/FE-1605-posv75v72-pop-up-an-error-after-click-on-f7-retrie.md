---
project: "FE"
issue_key: "FE-1605"
issue_type: "Bug QA"
status: "Closed"
tags: [faq, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1605"
created: "2025-01-13"
resolved: "2025-02-24"
fix_version: ""
components: [Front End]
category: "05_Error_Exception"
---

FE-1605: Pop up an error after click on 'F7 Retrieve Order'

| 問題
當 Syscon_Open_Item_Mod='N' 時，重複點擊 F7 Retrieve Order 會彈出錯誤訊息。

| 根因
當 OpenItem 功能被禁用時，SALE UI 中的 OpenItem 按鈕功能未正確替換為 Retrieve Order 指令，導致重複操作時觸發錯誤。

| 解法
在 OpenItem 禁用時，將 SALE UI 的 OpenItem 按鈕功能替換為 Retrieve Order 指令，已於 KTS 250109 修復（v720.02R25B, v750.05, v750.04R10）。

| 相關資訊
- Jira: [FE-1605](https://ctil.atlassian.net/browse/FE-1605)
- 解決日期: 2025-02-24
- 組件: Front End
- 負責人: Sang
- 附件: [image-20250113-054931.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50250)
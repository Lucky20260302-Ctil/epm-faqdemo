---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3319
tags: [faq, epm, epmtdcprot, 06-procurement-workflow]
jira_url: "https://ctil.atlassian.net/browse/EPMTDCPROT-3319"
category: 06_Procurement_Workflow
category_name: "採購流程"
---

EPMTDCPROT-3319: [Phase 2 DEV] Delegation Email - Tender Role

| 問題

Tender Role 委派電子郵件內容不一致，且 System Notification 未顯示 CC 資訊，如何處理？

| 根因

根據 Comment (William Qiu)：System Notification 上未顯示 CC 資訊，但實際郵件發送時有抄送給 Delegator 及提交者，造成使用者對郵件行為的誤解。

| 解法

同步 Delegator 與 Delegate-To 的郵件模板（Email Template）內容。針對不同委派類型（如 Finance Users / Price Accessor），需確保郵件中包含正確的委派資訊（Delegated-To person、Delegation Role、Delegation Type、Remarks 等）。若由 sysadmin 創建委派，sysadmin 也應收到郵件通知。

| 相關資訊

- Jira: [EPMTDCPROT-3319](https://ctil.atlassian.net/browse/EPMTDCPROT-3319)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT

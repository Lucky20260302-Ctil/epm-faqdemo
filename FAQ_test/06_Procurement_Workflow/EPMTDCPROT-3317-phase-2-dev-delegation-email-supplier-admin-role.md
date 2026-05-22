---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3317
issue_type: ''
status: ''
tags:
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3317
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---
EPMTDCPROT-3317: [Phase 2 DEV] Delegation Email - Supplier Admin Role

| 問題

Supplier Admin Role 委派電子郵件中，Delegator 與 Delegate-To 收到的內容不一致，如何修正？

| 根因

根據 Comment (William Qiu)：與 Supplier Role 委派相同，System Notification 上未顯示 CC 資訊，但實際郵件有抄送給相關人員，導致畫面呈現與實際發送行為不符。

| 解法

同步 Delegator 與 Delegate-To 的郵件模板內容。若委派是由 sysadmin 創建，sysadmin 也應收到郵件通知（每個角色委派需要 3 個郵件模板）。

| 相關資訊

- Jira: [EPMTDCPROT-3317](https://ctil.atlassian.net/browse/EPMTDCPROT-3317)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT

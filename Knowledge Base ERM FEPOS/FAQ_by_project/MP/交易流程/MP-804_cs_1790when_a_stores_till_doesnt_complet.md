---
tags: [faq, mp, 交易流程]
component: "Frontend"
symptom: "Symptom:"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: MP-804
resolved: 
fix-version: ""
---

# MP-804: [CS-1790]When a store's Till doesn't complete Dayend, there is no prompt on Till 0

## 問題

Symptom:
When a store's Till doesn't complete Dayend, there is no prompt on Till 0
Troubleshooting:
When upgrading to V75 in the Outlet store, it was found that when the dayend of a certain till is not completed, there will be no prompt on Tile 0 indicating that the till has not completed its dayend.
The store will only discover the missing sales of a certain till when it needs to complete the total dayend of Tile 0 and print the total dayend report.
Attached is the error prompting missing data from certain sub-till, but no message will show up in v75 POS.
As per suggestion from sanyo team, please create JIRA ticket for checking. Thanks!
若店铺某台Till没有完成或者是某台Till完成日结，但该Till的数据没有反映到Till0的这两种情况下，V72版本无论在那种情况Till0提示该Till没有完成日结（如下方V72截图一样）。
但outlet升级到V75后上述的两种情况，均没有出现如V72一样的提示。店铺需要在完成日结后，才会发现某台Till的销售没有在总日结报告上。

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Tovi Wang** (2025-10-22):
@@Sang  Please take a look this jira.
@@Joy Li As we talked in yesterday.Please help to share the details info to sang for further checking.Thanks!
**Sang** (2025-10-22):
@@Tovi Wang @@Joy Li Fixed in v750.04R14D ( Jira FE-1766)
v750.04R14D
Process consolidated day end before sub till complete day end, POS fail to alert missing till message fixed, add log (KTS 251006 FE-1766 v750.04R14D, v750.05)
 [20251006 12:10:35 -0511]: The day-end file cannot be found from the following sub-tills, tills number are [ 1 ]. Do you want to continue with consolidated report?
**Automation for Jira** (2025-10-22):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2025-10-22):
Updated the details to Coach team.
**Andrew_Au** (2026-05-05):
@@Tovi Wang Please update the ticket status
**Tovi Wang** (2026-05-07):
can be closed.

## 相關資訊

- Jira: [MP-804](https://ctil.atlassian.net/browse/MP-804)
- Fix Version: 未記錄
- 解決日期: 未記錄

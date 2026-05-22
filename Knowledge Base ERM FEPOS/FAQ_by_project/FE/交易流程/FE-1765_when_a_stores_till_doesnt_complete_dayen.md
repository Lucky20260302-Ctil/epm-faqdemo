---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Symptom:"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: FE-1765
resolved: 
fix-version: ""
---

# FE-1765: When a store's Till doesn't complete Dayend, there is no prompt on Till 0 (INC3227274)

## 問題

Symptom:
When a store's Till doesn't complete Dayend, there is no prompt on Till 0
Troubleshooting:
When upgrading to V75 in the Outlet store, it was found that when the dayend of a certain Tile is not completed, there will be no prompt on Tile 0 indicating that the Tile has not completed its dayend. The store will only discover the missing sales of a certain Tile when it needs to complete the total dayend of Tile 0 and print the total dayend report

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Sherman tse** (2025-10-03):
@@Sang  i can resproduce this issue with VM: 172.16.138.61 (Till: 0) & 172.16.138.60 (Till: 1)
vm acc: .\sxd    pwd: Yan20201104@
Salady: YZHANG China123
Reproduce steps:
1. 
2. 
3. 
Exsiting result:
No any notice mentioned that Till 1 still not day end yet
V75 version:
172.16.138.61 (Till: 0) 7.5.0.04R14B (Build250911)
172.16.138.60 (Till: 1) 7.5.0.05(Build250918)
**Automation for Jira** (2025-10-06):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1765](https://ctil.atlassian.net/browse/FE-1765)
- Fix Version: 未記錄
- 解決日期: 未記錄

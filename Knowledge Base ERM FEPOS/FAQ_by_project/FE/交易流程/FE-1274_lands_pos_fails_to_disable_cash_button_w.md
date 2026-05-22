---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Reproduce step:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1274
resolved: 2023-08-08
fix-version: ""
---

# FE-1274: [Lands] POS fails to disable Cash button when order needs to be refunded

## 問題

Reproduce step:
1. 
2. 
3. 
Existing result:
POS fails to disable Cash button when order needs to be refunded
Remark:
VM: .245 (Lands side)
Tblsyscon set:
- 
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-08-08
### Jira Comments (2 則)
**Sherman tse** (2023-08-01):
@@Cy Lau
**Sherman tse** (2023-08-08):
Set back a correct payment code (000 in LANDS), then Cash can be disable when items need to be refunded.
Close case

## 相關資訊

- Jira: [FE-1274](https://ctil.atlassian.net/browse/FE-1274)
- Fix Version: 未記錄
- 解決日期: 2023-08-08

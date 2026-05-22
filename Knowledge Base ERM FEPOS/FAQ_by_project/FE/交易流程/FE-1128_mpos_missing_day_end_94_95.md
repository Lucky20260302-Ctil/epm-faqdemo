---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "Case 1: J364 20220705"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1128
resolved: 2024-03-05
fix-version: ""
---

# FE-1128: MPOS missing day end 94 95

## 問題

Case 1: J364 20220705
version 7.2.0.02R14
missing day end 94 95 for M till. Have RP m till report
Case 2: J396 20220704
version 7.2.0.02R14
missing day end 94 95 for M till. Have RP m till report
RIN01017990

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-03-05
### Jira Comments (3 則)
**Joy Li** (2022-07-06):
Case 1 Log: \\172.16.183.201\localuser\support\JIRA_DB\FE-1128\J364_20220705
Sang generated the day end record for Day end checking. Continuous checking
**Joy Li** (2022-07-06):
Case 2 Log: \\172.16.183.201\localuser\support\JIRA_DB\FE-1128\J396_20220704_RIN01017990
**Sang** (2022-07-07):
Can't reproduce. Add Log and add command to POSSupp to re-generate MPOS Day End PCD
15. POSSupp Add -WriteMPOSDayEndPCD Date SalesAssociate (KTS 220707 v720.02R18,750.02 Jira [🔗](https://ctil.atlassian.net/browse/FE-1128#icft=FE-1128))

## 相關資訊

- Jira: [FE-1128](https://ctil.atlassian.net/browse/FE-1128)
- Fix Version: 未記錄
- 解決日期: 2024-03-05

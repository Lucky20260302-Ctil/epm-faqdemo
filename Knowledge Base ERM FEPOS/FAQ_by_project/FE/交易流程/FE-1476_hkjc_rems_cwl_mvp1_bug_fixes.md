---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "1. "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1476
resolved: 2024-09-04
fix-version: ""
---

# FE-1476: HKJC REMS CWL MVP1 Bug fixes

## 問題

1. 
2.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-04
### Jira Comments (6 則)
**Sang** (2024-08-02):
1. 
2. 
3. 
4.
**Sang** (2024-08-03):
'v750.01R021
1. 
2. 
3.
**Sang** (2024-08-03):
Test Case:
Scenarios 1 – API return Member type ‘03’, Local DB has not member records, Not effective MM, Apply Member disc 20%
Scenarios 2 – API return Member type ‘03’, has record in Local DB with diff Member type ‘05’, No effective MM, Apply Member disc 20% (‘03’)
Scenarios 3 – API return Member type ‘03’, Local DB has not member records, Has effective MM, Apply MM disc
Scenarios 4 – API return Member type ‘03’, has record in Local DB with diff Member type ‘05’, No effective MM, Apply Member disc 20% (‘03’)
JC’s Issue properly is Scenarios 4 -
wrong member discount apply to the VIP with same vip type of member when both vip discount and Mix & Match discount are 20% off.
**Sang** (2024-08-03):
1.
**Sang** (2024-08-03):
Case Member ‘PS07770915’:
1. 
1. 
1.
**Andrew_Au** (2024-09-04):
@@Andy Ko Please update the ticket status

## 相關資訊

- Jira: [FE-1476](https://ctil.atlassian.net/browse/FE-1476)
- Fix Version: 未記錄
- 解決日期: 2024-09-04

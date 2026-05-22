---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[ANZ] Incorrect amount of change after apply rounding: CHANGEROUND=R settings"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1882
resolved: 
fix-version: ""
---

# FE-1882: [ANZ] Incorrect amount of change after apply rounding: CHANGEROUND=R settings

## 問題

[ANZ] Incorrect amount of change after apply rounding: CHANGEROUND=R settings
Ordered an item: CAY08 price: 1094.11
Reprodure steps:
1. 
2. 
3. 
4. 
5. 
Existing result:
Change part in the receipt displayed incorrect amount of change: 0.80
Expected result:
Change part in the receipt should display correct amount of change: 0.9
Config settings in POS:
CHANGEROUND=R
CHANGERNDDEC=0.1
CHANGEROUND_ENABLE=Y

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Automation for Jira** (2026-02-10):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-02-10):
Coach ANZ (FE-1882)
A.      Change Round =”R”
A. 794.11 --> 791.10   (Adj -0.01)
B1. Paid 795.00  Change 0.89 à 0.90
B2. Paid 794.11  Change 0
B. 794.15 --> 791.20   (Adj 0.05)
B1. Paid 795.00  Change 0.85 à 0.80
B2. Paid 794.15  Change 0
C. 794.17 --> 791.20   (Adj 0.03)
C1. Paid 795.00  Change 0.83 à 0.80
C2. Paid 794.13  Change 0
**Sang** (2026-02-10):
revised program uploaded to \\ds411\share\POS_FE_Release_64\20260210 Coach v750.04R21 - ANZ
**Andrew_Au** (2026-05-05):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [FE-1882](https://ctil.atlassian.net/browse/FE-1882)
- Fix Version: 未記錄
- 解決日期: 未記錄

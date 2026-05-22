---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "@@Cy Lau @@Andrew_Au @@Sang @@Joy Li"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1529
resolved: 2024-10-19
fix-version: ""
---

# FE-1529: Coach MY BDO FE - gift cert total amount calculation error

## 問題

@@Cy Lau @@Andrew_Au @@Sang @@Joy Li
In FE (7.5.0.04R07 Build 241004), I created a gift cert issuance memo that has 3 lines:
The total amount here is correct so far. But in the PCD file the total amount becomes 1400.00:
This is causing problems in BE posting and potentially problems for the e-invoice interface.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-10-19
### Jira Comments (7 則)
**Joy Li** (2024-10-18):
@@Sang Please advise ETA
the original plan to send the FE package to COACH today.
**Sang** (2024-10-19):
PCD fixed
**Sang** (2024-10-19):
TMU PRint Out Bug
**Sang** (2024-10-19):
TMU Print Out Fixed
**Sang** (2024-10-19):
v750.04R07A
1. 
2.
**Sang** (2024-10-19):
Uploaded to \\ds411\share\POS_FE_Release_64\20241019 Coach v750.04R07A - MY
**Andy Ko** (2024-10-19):
fixed in version: 7.5.0.04R07A (build 241019)

## 相關資訊

- Jira: [FE-1529](https://ctil.atlassian.net/browse/FE-1529)
- Fix Version: 未記錄
- 解決日期: 2024-10-19

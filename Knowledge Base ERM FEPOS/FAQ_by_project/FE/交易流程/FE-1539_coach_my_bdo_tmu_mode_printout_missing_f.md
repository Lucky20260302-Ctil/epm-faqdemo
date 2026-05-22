---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "mpos printout in TMU mode"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1539
resolved: 2024-10-28
fix-version: ""
---

# FE-1539: Coach MY BDO - TMU mode printout missing footer

## 問題

mpos printout in TMU mode
mpos ereceipt in TMU mode
mpos printout zebra
POS ereceipt in TMU mode
POS printout in TMU mode
all these printout/ereceipt is missing
as per the SOW:
current TMU and zebra:
current POS ereceipt when printing is set to TMU:
current MPOS ereceipt when printing is set to TMU:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-10-28
### Jira Comments (3 則)
**Andy Ko** (2024-10-24):
**Sang** (2024-10-24):
Coach TMU Print Out - Footer file Config
Sales/Deposit Settle - tblconfig.FOOTERFILENAMENORMAL
Sales Exchange - tblconfig.FOOTERFILENAMEEXCHANGE
Sales Return/Void/VoidDeposit Settle - tblconfig.FOOTERFILENAMERETURN
Void Sales Return / Void Sales Exchange - tblconfig.FOOTERFILENAMERETURN
**Sang** (2024-10-24):
Please check file

## 相關資訊

- Jira: [FE-1539](https://ctil.atlassian.net/browse/FE-1539)
- Fix Version: 未記錄
- 解決日期: 2024-10-28

---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "[INC2931120]AWS JP J317 POS v75,"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1694
resolved: 2025-09-10
fix-version: ""
---

# FE-1694: [INC2931120]new password of account 933969changed in FE can't be sync to SRC/HHT/namecapture   

## 問題

[INC2931120]AWS JP J317 POS v75,
new password of account 933969 changed in FE can't be sync to SRC/HHT/namecapture.
If the password changed in BE , it can be sync to SRC/HHT/namecapture and FE normally. only this account has the issue.
User changed the password to Aa123456 in FE , but the password in ename is still Www0213. Sync password failed.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-10
### Jira Comments (5 則)
**Sang** (2025-05-15):
@@Cy Lau @@Bobby   Anyone can help to check sync salady password to ename system?  @@Joy Li
@@Bobby
**Andrew_Au** (2025-06-05):
@@pierre.shi @@Tovi Wang Please update the ticket status
**Andrew_Au** (2025-09-10):
@@pierre.shi @@Tovi Wang@@Joy Li  Please update the ticket status
**pierre.shi** (2025-09-10):
@@Andrew_Au please help to close
**Automation for Jira** (2025-09-10):
Issue has been created since
Days since: 118
Week since : 16
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1694](https://ctil.atlassian.net/browse/FE-1694)
- Fix Version: 未記錄
- 解決日期: 2025-09-10

---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "@@Sang 请教一个小问题哈。CS2000 POS前台有一个 SignOut button是哪个xconfig来control的呀？"
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: FE-1930
resolved: 
fix-version: ""
---

# FE-1930: [CS-2632]How to enable Signout button in CS2000 POS FE

## 問題

@@Sang 请教一个小问题哈。CS2000 POS前台有一个 SignOut button是哪个xconfig来control的呀？
下面2个xconfig都enable,但还是没有sign Out button.
ENABLESIGNINOUT                 Y
Syscon_Sign_Out_Pass_Need       Y

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Automation for Jira** (2026-04-20):
Issue has been created since
Days since: 3
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2026-04-20):
@@Sang PRC region.Dbtrans here,Please help to check.
**Tovi Wang** (2026-04-20):
@@Sang 这个是CN Pro的测试机，有sign out 和log out button.Dbtrans for your reference.Thanks!
1.
[2.BE](http://2.BE) UI  role setting.
**Sang** (2026-04-20):
@@Tovi Wang This bug will be fixed in next release (v750.04R25)
**Sang** (2026-04-20):
@@Tovi Wang OC9990 and OCT910 has different CashierControl setting,  This bug triggered when EnableSignInOut='Y' and CashierControl='N'
**Tovi Wang** (2026-04-20):
@@Sang Noted. I can reproduce it in OC9990 PC.
@@Joy Li Please help to arrange this bug released ETA.Thanks!
Reproduce steps:
1.Setting EnableSignInOut='Y' and CashierControl='N'.
2.Then signout button and logout butong disapeared.
Changed before:
Changed after:
**Sang** (2026-04-20):
@@Tovi Wang  Fixed in v750.05R25
1.
**Tovi Wang** (2026-04-20):
@@Joy Li @@Sherman tse Please help to arrange the testing and released ETA.Thanks!
**Sang** (2026-04-22):
@@Tovi Wang @@Sherman tse Program uploaded to  \\ds411\share\POS_FE_Release_64\20260422 Coach v750.04R25

## 相關資訊

- Jira: [FE-1930](https://ctil.atlassian.net/browse/FE-1930)
- Fix Version: 未記錄
- 解決日期: 未記錄

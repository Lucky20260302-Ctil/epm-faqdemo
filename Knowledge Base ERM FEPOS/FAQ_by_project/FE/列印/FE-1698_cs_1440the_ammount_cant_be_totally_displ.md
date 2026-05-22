---
tags: [faq, fe, 列印]
component: "Printing"
symptom: "@@Cy Lau @@Sang  As talked in teams."
root-cause: "待提取"
solution: "### Jira Comments (14 則)"
jira: FE-1698
resolved: 
fix-version: ""
---

# FE-1698: [CS-1440]The ammount can't be totally displayed as bellow:

## 問題

@@Cy Lau @@Sang  As talked in teams.
CC @@Joy Li
1.the ammount can't be totally displayed as bellow:
2.Preview page also have this issue.
3.
a.TMU_PRINTER_REC_LINE_CHAR setting is 40 now
b.PRINTCHARSETCODE setting is KO now.
c.CHARSETCODE setting also is KO.
Troubleshooting:
1.Whether TMU_PRINTER_REC_LINE_CHAR setting is 42 or 48，but issue still.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (14 則)
**Sang** (2025-05-20):
@@Tovi Wang @@Cy Lau Enhance layout on next release v750.04R13B
**Tovi Wang** (2025-05-21):
@@Sang @@Cy Lau  Many Thanks for your quick action.Please help to provide the released ETA.Thanks!
**Sherman tse** (2025-05-26):
Still meet the issue when I purchase items that over 10,000,000 KRW = 57,530 HKD
Also, I met the issue when **return **a sales memo over 1,000,000
Related result as below:
Return sales memo:
**Sang** (2025-05-26):
Please advise yr testing CSPLUS compiled date?
Get Outlook for iOS<[https://aka.ms/o0ukef](https://aka.ms/o0ukef)>
**Sherman tse** (2025-05-26):
@@Sang I am tesing with version: 7.5.0.04R13A (Build250520)
**Sang** (2025-05-26):
Will be check and fix tmr
Get Outlook for iOS<[https://aka.ms/o0ukef](https://aka.ms/o0ukef)>
**Sang** (2025-05-27):
@@Sherman tseI got the correct result by using v750.04R13A.  Let me know your testing VM.
**Sherman tse** (2025-05-27):
@@Sang I tested with VM: 172.16.138.148 of KR
Password: Yan20201104@
**Tovi Wang** (2025-06-05):
@@Sherman tse @@Sang
Coach QA said the issue still in latest released.Could you help to double check and confirm this one?
Thanks!
CC @@Joy Li
**Sherman tse** (2025-06-05):
@@Sang Just tested on KR VM, when memo is return type, receipt would still display -1,050,…
as below capture:
KR VM: 172.16.138.148
**Sang** (2025-06-05):
@@Sherman tse
program updated in v750.04R13B. uploaded to \\ds411\share\POS_FE_Release_64\20250605 Coach v750.04R13B
**Sherman tse** (2025-06-05):
Tested with R13B and get positive result as below:
**Tovi Wang** (2025-06-05):
@@Sherman tse Many Thanks!
@@Joy Li @@Sang 这个是要等下一个package再发给Coach QA,还是等这几个问题一起全解决了。再补一个 package给到Coach QA?
**Tovi Wang** (2025-08-29):
Coach QA Confirmed the issue is fixed by  FE V75.004.1301.0002 in QA

## 相關資訊

- Jira: [FE-1698](https://ctil.atlassian.net/browse/FE-1698)
- Fix Version: 未記錄
- 解決日期: 未記錄

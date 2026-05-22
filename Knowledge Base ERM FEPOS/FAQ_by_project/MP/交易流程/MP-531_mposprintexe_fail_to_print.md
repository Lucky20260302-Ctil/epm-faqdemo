---
tags: [faq, mp, 交易流程]
component: "MPOSPrint.exe"
symptom: "Log path in FE:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-531
resolved: 2024-03-01
fix-version: ""
---

# MP-531: MPOSPrint.exe fail to print

## 問題

Log path in FE:
C:\CS2000POS\MPOSPrint_YYYYMMDD.log
C:\retdata6\T9YYMMDD.dat
C:\retdata6\DALYYYYMMDD.log
**Case 1: User start FE. auto recovery.**
2022-06-15 J421 &J487
J421 and J487 call out that they fail to print MPOS memo at 1400. But reported can print without any remote at 1600.
**Case 2: Sanyo kill MPOSprint.exe and start. then work**
2022-06-15 J486
J486 call out at 2pm too. I remote at 14:55 and found that the MPOSprint.exe in task manager but fail to found in notice bar. fail to open.
Therefore i kill MPOSprint.exe in task manager and start MPOSprint.exe manually. User reported that mpos print back to normal after i restart mposprint.exe
***No server IIS reset on 2022-06-14 ***
**Case 3: MPOS IIS fail call print Hub >> Restart IIS then work**
2022-06-16 J368

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-03-01
### Jira Comments (5 則)
**Joy Li** (2022-06-16):
Add 2022-06-14 Server log for J486 & J487
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\Server_20220614_J486_J487.zip
Case 1 & 2
**Joy Li** (2022-06-16):
Add POS Log J486
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\DAL20220614J486.log
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\T9220614J486.dat
Add POS Log J487
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\DAL20220614J487.log
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\T9220614J487.dat
**Joy Li** (2022-06-16):
Add 2022-06-16 Server log for J368
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\Server_20220616_J368.zip
Case 3
**Joy Li** (2022-06-16):
Add POS Log J368 2022-06-16
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\FE_Log_20220616_J368\
- 
- 
-
**Steven Yuen** (2022-06-24):
RIN01004843, J461, J486, J396 reported Mpos printing failure and screen keeps loading. 
Joy tried printing on Swagger and keep loading too.
Restart Cloud IIS and Mpos printing resumed.
- 
- 
Add MPOSPrint log on 2022-06-24 for comparison.
\\172.16.183.201\localuser\support\JIRA_DB\MP-531\FE_Log_2022-06-24
- 
- 
-

## 相關資訊

- Jira: [MP-531](https://ctil.atlassian.net/browse/MP-531)
- Fix Version: 未記錄
- 解決日期: 2024-03-01

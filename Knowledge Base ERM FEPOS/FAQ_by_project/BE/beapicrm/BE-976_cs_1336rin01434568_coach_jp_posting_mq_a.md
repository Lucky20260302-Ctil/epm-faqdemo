---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "APP_CS2000_JP-Start Posting MQ_01;APP_CS2000_JP-Start Posting MQ_A;"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-976
resolved: 2025-05-02
fix-version: ""
---

# BE-976: [CS-1336]RIN01434568-COACH JP Posting MQ_A&MQ_01 terminated

## 問題

APP_CS2000_JP-Start Posting MQ_01;APP_CS2000_JP-Start Posting MQ_A;
Error file attached caused the posting termination;
error code:TRX.ROLLBACK
error msg:ExecuteReader requires the command to have a transaction when the connection ass
Could you please help to check the root cause?

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (21 則)
**Joy Li** (2024-12-30):
@@Jerry Wong Posting Log: \\172.16.183.201\localuser\support\JIRA_DB\BE-976\BE-976_postign Log.zip
**pierre.shi** (2025-01-14):
Hi @@Jerry Wong ,have we got any progress about this issue?
**Jerry Wong** (2025-01-14):
@@pierre.shi Can you send the prj_ic8006.dll to me for the testing?
**pierre.shi** (2025-01-14):
@@Jerry Wong  could you please show me the path of this file?
**Cy Lau** (2025-01-14):
@@pierre.shi the path would be same as the program running folder
**pierre.shi** (2025-01-14):
Hi @@Jerry Wong @@Cy Lau ,the file has been uploaded as attachment.
**pierre.shi** (2025-01-15):
Hi @@Jerry Wong @@Cy Lauhave we got any progress?
**Jerry Wong** (2025-01-16):
@@pierre.shi
Release:
\\ds411\csms60\delivery\coach\update-coach-IC8006-2024-01-16
**pierre.shi** (2025-01-16):
Hi @@Jerry Wong 这个路径里是已经做好的补丁包吗？如果是的话，这个补丁包测试过了，能直接使用吗？
**Jerry Wong** (2025-01-16):
@@pierre.shi 可以幫我test一下嗎? 因為我這邊測試過，但找不到這個issue，所以加了一些log，如果再有問題跟我說
**pierre.shi** (2025-01-16):
Hi @@Jason Wu@@Jerry Wong  could you help on this?
I have never done this action. And don’t know what should be done to avoid  risk on the server.
**Jason Wu** (2025-01-16):
@@pierre.shi Please pass to QA team for the testing
**pierre.shi** (2025-01-16):
Hi @@Jerry Wong ,could you share the root  cause to us? Coach want to the RCA.
**pierre.shi** (2025-01-16):
Hi@@Joseph_Hu please help to test the program. thanks.
\\ds411\csms60\delivery\coach\update-coach-IC8006-2024-01-16
**Jerry Wong** (2025-01-17):
@@pierre.shi @@Joseph_Hu wait a second, I have changing later
**Cy Lau** (2025-01-17):
\\ds411\csms60\delivery\be\update.be7.coach.250117\prj_ic8006
**Cy Lau** (2025-01-17):
RCA : 
In prj_ic8006 module , the pstlog instance would share the same SQL connection with taskUpdate  instance. When taskUpdate  instance begins transaction, and pstlog instance perform database query, crashes may be caused.
Fixing :
The pstlog instance would now have its own SQL connection , independent with taskUpdate instance. The issue is fixed at version 
1.25.01.1700
**Cy Lau** (2025-01-22):
For the testing enviroment,
Please use the current CJ CS2KBNV1 modules, and replace the latest prj_ic8006
1. 
2. 
Positive: log written and no crash
Negative: crashed with the same error.
@@Jerry Wong  Please assit QAQC team
**Sherman tse** (2025-01-24):
Verified on QA
**pierre.shi** (2025-01-26):
Hi Team,this issue occurred again. logs has been uploaded.
**Andrew_Au** (2025-03-20):
@@pierre.shi @@Tovi Wang  Please update the ticket status

## 相關資訊

- Jira: [BE-976](https://ctil.atlassian.net/browse/BE-976)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

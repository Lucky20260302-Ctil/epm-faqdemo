---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "SOG callout KR new V72 store OC872 till1 keep missing RP file.Till0 is normal."
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1817
resolved: 
fix-version: ""
---

# FE-1817: [INC3310467] KR new V72 store OC872 till1 keep missing RP file

## 問題

SOG callout KR new V72 store OC872 till1 keep missing RP file.Till0 is normal.
I remote to Till1 and rollback 2025-11-24 dayend.Nothing error pop out when I rollback dayend.
@@Sang Could you help to take a look this case and double check the till1 FE log if any other something wrong?If anything xconfig to control the RP file generated?
CC @@Joy Li @@pierre.shi
1.
2.Checked the T9 log find follow error:
[24/11/2025 19:59:29 -5238]: 2025-11-24 19:59:29-Prepare_Print_DayEnd_Info_DO - Start :
[24/11/2025 19:59:31 -2827]: 2025-11-24 19:59:31-Prepare_Print_DayEnd_Info_DO - End
[24/11/2025 19:59:31 -3127]: 2025-11-24 19:59:31-<span style="color:#ff5630">Init_PrintFunc_DO Failure :Automation error</span>
<span style="color:#ff5630">ClassFactory cannot supply requested class</span>
[24/11/2025 19:59:31 -3137]: 2025-11-24 19:59:31-After Print Dayend - DO

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Tovi Wang** (2025-11-25):
@@Sang
All OC872 till1 FE logs here.Contains dbtrans & dbhist
**Sang** (2025-11-25):
@@Tovi Wang POS fail to load COM Print library, please try reg reg to register vb 6 COM library first.
**Tovi Wang** (2025-11-25):
@@Sang Thanks for your advice,Let me try this first.
**Automation for Jira** (2025-11-25):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2025-11-25):
@@Sang reg reg done.Keep monitoring tonight dayend.
**Tovi Wang** (2025-11-25):
@@Sang  after reg reg,Till1 dayend still failed to generate RP file on Nov. 25th,
Please kindly help to check and assist.
**Tovi Wang** (2025-11-28):
Good news.Re-installed Till1 POS,Can normal generated Till1 RP file now.Issue fixed.
@@Sang May I know the RCA?
CC @@Joy Li

## 相關資訊

- Jira: [FE-1817](https://ctil.atlassian.net/browse/FE-1817)
- Fix Version: 未記錄
- 解決日期: 未記錄

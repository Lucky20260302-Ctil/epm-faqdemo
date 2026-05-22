---
tags: [faq, fe, 交易流程]
component: "Deposit, Payment, Sales"
symptom: "Dear @@Cy Lau ,"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1567
resolved: 2025-03-20
fix-version: ""
---

# FE-1567: [CS-1128] - For CN OCF87-10013580 is used to void OCF87-10013577 on 2024-08-09, why payment amount is -2568 for 10013580 ?

## 問題

Dear @@Cy Lau ,
For CN OCF87-10013580 is used to void OCF87-10013577 on 2024-08-09, why payment amount is -2568 for 10013580 ?What’s the correct details logic for this case situation?
Follow details and logs for your reference.
Deposit memo : 00000017
payment amount: 2568
joudep_stage: 21
Resource memo: 10013577
BE Payment amount: 0
FE PC file payment amount: 2568
Void memo: 10013580
BE Payment amount: -2568
FE PC file payment amount: -2568
I has applied the data patch for this case.And I can’t reproduce this issue in QA PC.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-20
### Jira Comments (14 則)
**Tovi Wang** (2024-11-21):
@@Cy Lau 这个case，前台和后台数据都不一致，我对此也很confuse。针对这种情况下case,请帮忙检查确认系统在前后台数据处理的详细逻辑，谢谢！
**Tovi Wang** (2025-01-19):
@@Cy Lau Double checked S9 log,the issue caused by user select the incorrect payment code LGV with 2568 amount when settled the deposit memo.
Please help to enhance the settled workflow to prevent the abnormal action happened again.Bellow capture for your reference.
**Tovi Wang** (2025-01-20):
@@Cy Lau @@Sang
the next action would be the bug fixing for the LGV payment type.
-->Please help to provide the bug fixing.Which POS version can covered this issue?R09 or R10?Thanks!
**Tovi Wang** (2025-02-05):
Dear @@Cy Lau @@Sang  Please help to provide the bug fixing.Thanks!
**Cy Lau** (2025-02-05):
@@Tovi Wang  I think it is the LGV payment issue.
@@Sang  As I remember, you did a fix on that am I right ?
**Sang** (2025-02-05):
@@Cy Lau @@Tovi Wang Relevant to LGV payment, but different case as [🔗](https://ctil.atlassian.net/browse/FE-1514). In this case non-allow return amount has not recorded as misc amt.  I am not able to re-produce in v7504R10.  Any way to found out the POS version at that time memo was created.
**Cy Lau** (2025-02-06):
@@Sang
From the log :
[09/08/2024 08:43:06 -5995]: Ver. **7.2.0.02R21A**
**Sang** (2025-02-06):
@@Cy Lau @@Tovi Wang Able to re-produce issue on v72.02 and v750.04R10.  Re-produce Step
1. 
2. 
3. 
4. 
5. 
To be fixed in next release.
**Tovi Wang** (2025-02-12):
@@Sang Many thanks for your keep updating.Please help to the bug fixing release.Which release will cover this issue?R11?
**Sang** (2025-02-14):
@@Tovi Wang @@Sherman tse @@Cy Lau
v750.04R11
1. 
2. 
3.
**Tovi Wang** (2025-02-14):
@@Sang Many thanks for your update.
@@Sherman tse Please help to arrange testing once R11 applied.Thanks!
**Andrew_Au** (2025-03-20):
@@Tovi Wang @@pierre.shi Please update the ticket status
**Tovi Wang** (2025-03-20):
@@Andrew_Au It has included in R12.1 FEV75.04R11 released on 5/3/2025.
**Sang** (2025-03-20):
@@Tovi Wang @@Andrew_Au @@Jason Wu
Please send FE version log of FEV750.04R11 to me which included in R12.1 - released on 5/3/2025.  I need to know the Released R11 cut-off .
v750.04R11 - Up-to-date full list
1. 
2. 
3. 
4. 
5. 
6. 
7.

## 相關資訊

- Jira: [FE-1567](https://ctil.atlassian.net/browse/FE-1567)
- Fix Version: 未記錄
- 解決日期: 2025-03-20

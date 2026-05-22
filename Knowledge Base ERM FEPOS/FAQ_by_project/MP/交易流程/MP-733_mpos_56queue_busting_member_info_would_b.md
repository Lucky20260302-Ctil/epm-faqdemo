---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "Issue - JP - Memo＆Customer Info will be cleaned up when call out transaction in MPOS"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-733
resolved: 2025-02-24
fix-version: ""
---

# MP-733: [MPOS-56]Queue Busting - Member Info would be cleared out after update on MPOS

## 問題

Issue - JP - Memo＆Customer Info will be cleaned up when call out transaction in MPOS
Reproduce steps:
Issue sales in MPOS >>Send to POS >> call out transaction in MPOS to modify items>>Send to POS once again(Memo & customer info became blank)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-24
### Jira Comments (9 則)
**Cy Lau** (2024-12-01):
@@Joy Li  Please help to explain about [Send to POS] ?
@@Daniel Leung  Please help check for the MPOS , does it happen in MPOS
**Cy Lau** (2024-12-01):
Reviewed the code, the Create and Update do include the Member Info as saving ,
Suspected as
1. 
2. 
DevTeam would like to have the env or log for easy investigation , please advice.
**Daniel Leung** (2024-12-10):
Get Memo from Queue Busting:
Load memo
Added new Item
Save to Queue Busting
Member still here
Same result on FE
**Sherman tse** (2024-12-31):
I cannot reproduce the issue
**Sherman tse** (2025-01-07):
Picture from external jira:
Steps: 
1. MPOS Link with V72 POS
2. Add an item & a member
3. Fill in Remark & customers info
4. Save to queue busting with Remaks & customers info
5. Open the saved order in queue busting to sales memo
6. Add one more item into the order & try to save to queue busting
Existing result:
Remaks & customers info cleared after add one more item into the order in queue busting
V75
Can reproduce the issue partly
Steps:
1. 
2. 
3. 
4. 
5. 
6. 
Existing result:
Only Remaks cleared after add one more item into the order in queue busting
**Daniel Leung** (2025-01-08):
3.29.5-20250107.1 uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)
Bug fix: `queueData will pass to PaymentController now. `
**Scanner fix(**[🔗](https://ctil.atlassian.net/browse/MP-725) **) are **<span style="color:#ff5630">**not **</span>**included in this version**
**Cy Lau** (2025-02-13):
Pending to be reopened for R12 
Please check if
Include the fix
**Andrew_Au** (2025-02-24):
@@Sherman tse  Can I close the ticket  ?
**Sherman tse** (2025-02-24):
Issue has test on:
MPOS API:
Version: 3.29.5(20250106.1-b1)
[\\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20250106.1b1](file://ds411/share/POS_MPOS_Release/3.29.X/3.29.5-20250106.1b1)
MPOS ipa:
Version: 3.29.5-20250108.2
Health check with MPOS ipa: 3.29.5-20250212.1, Queue Busting fucntion still works fine
Just viewed with Tapestry jira, they will retest the issue with COACH_MPOSWebAPI_3.29.5c.zip release on Jan-27th & conduct the testing by Feb-06th
I think we can close the Jira first, if COACH has any issue on the jira, we would reopen it.

## 相關資訊

- Jira: [MP-733](https://ctil.atlassian.net/browse/MP-733)
- Fix Version: 未記錄
- 解決日期: 2025-02-24

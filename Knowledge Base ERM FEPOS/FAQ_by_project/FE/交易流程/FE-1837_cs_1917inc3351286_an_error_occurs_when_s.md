---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "An error occurs when setting the POS of the cash drawer balance to 'All'."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1837
resolved: 2026-03-25
fix-version: ""
---

# FE-1837: [CS-1917][INC3351286] An error occurs when setting the POS of the cash drawer balance to 'All'.

## 問題

An error occurs when setting the POS of the cash drawer balance to 'All'.
Symptom:
When checking the cash drawer balance on all registers by setting the POS to 'All,' it displays '[Sorry, cannot connect to the main-till, do you want to change the till
to standalone mode?].'
Err:'[Sorry, cannot connect to the main-till, do you want to change the till to standalone mode?].'
Troubleshooting:
1. 
2. 
3. 
4.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-03-25
### Jira Comments (20 則)
**Tovi Wang** (2025-12-19):
@@Joy Li KSJ pilot store callout another issue.Let me sahre the details to you in next Monday.Deatils in SOG ticket.
CC @@Cy Lau @@Sang
**Sang** (2025-12-19):
@@Tovi Wang This error due to till pc fail to connect to shop SSE. Please change config / local net work connection
**Sang** (2025-12-19):
@@Tovi Wang get consolidated data from SSE timeout also show this message. Please check DAL / T9 log
**Tovi Wang** (2025-12-19):
@@Sang
NPOS log error:
T9 log error:
[20251218 16:56:00 -4729]: doEnq_CashDrawBalance- Start : Avail V.  Memory : 140732160.684
[20251218 16:56:10 -0167]: doRefresh.Error: Invalid object name 'invtrx file Header'.
[20251218 17:00:22 -1167]: Standalone Change Mode
[20251218 17:00:25 -3037]: Change Standalone mode from False to False
**Tovi Wang** (2025-12-19):
@@Sang Thanks for your advice.Let me share the more find to Joy first in next Monday.
**Sang** (2025-12-22):
@@Tovi Wang Bug already fixed in v750.04R13I, R14+
v750.04R13I
1.
**Tovi Wang** (2025-12-22):
@@Sang
As we talked in teams meeting.Add more info for your reference:
远程到店铺测试发现,如果我选择了cashier_id 可以正常搜索出来data;
如果不选cashier id,则会出现 stand alone mode error.
请帮忙进一步检查确认。如果需要我可以借个远程再reproduce一起看下。
**Tovi Wang** (2025-12-23):
@@Sang @@Joy Li The package v750.04R13I, R14+ if released to Caoch QA,I can’t find the version in Jira FE-1681,Could you double check and confirm it?
BTW,Could we covered this issue in v750.04R13E,v750.04R13F(75.004.1305.XXXX,75.004.1306.XXXX)?
**Tovi Wang** (2025-12-23):
@@Sang 请帮忙确认 现在哪一个版本可以包含之前所有的 bug fix?包括KSJ 的两个 hotfix,一个 printing issue,另一个 KSJ dayend issue，还有这个柜台余额查询问题？我们需要一个最新版本同时涵盖之前所有的bug fix.
CC @@Joy Li
**Sang** (2025-12-29):
I have used v75.04R13E, checking other Tills or 'All' + cashier ID shows errors also
**Tovi Wang** (2025-12-29):
@@Sang Yes,Double confirmed with SOG,All KSJ V75 store have the same issue.V72 store are normal for this section.
**Sang** (2025-12-29):
@@Tovi Wang recommend to deploy v750.04R13J or R14
v750.04R13D
1. 
v750.04R13E
1. 
2. 
3. 
v750.04R13F
1. 
2. 
v750.04R13G
1. 
v750.04R13H
1. 
v750.04R13I
1. 
v750.04R13J
1.
**Tovi Wang** (2026-01-07):
Hi @@Joy Li @@Sang  Could you help to double confirm the latest version for all KSJ bug fix?Thanks!
**Tovi Wang** (2026-03-06):
@@Sang May I know the newest version R21 if covered this issue?
@@Sherman tse Could you help to test and confirm this one?Thanks!
**Sang** (2026-03-10):
@@Tovi Wang @@Sherman tse Yes. R21 included this bug fixing.
**Tovi Wang** (2026-03-11):
@@Joy Li @@Sherman tse Could you help to arrange the testing and the released ETA?Thanks!
**Sherman tse** (2026-03-20):
@@Tovi Wang Just test the issue will be included to next FE release
**Automation for Jira** (2026-03-20):
Issue has been created since
Days since: 90
Week since : 12
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2026-03-20):
Verified on QA
**Tovi Wang** (2026-03-20):
@@Sherman tse Thanks for your confirm.
@@Joy Li Please help to advice the released ETA.Thanks!

## 相關資訊

- Jira: [FE-1837](https://ctil.atlassian.net/browse/FE-1837)
- Fix Version: 未記錄
- 解決日期: 2026-03-25

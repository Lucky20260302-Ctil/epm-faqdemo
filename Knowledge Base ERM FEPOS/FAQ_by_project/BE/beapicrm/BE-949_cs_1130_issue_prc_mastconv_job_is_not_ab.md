---
tags: [faq, be, beapicrm]
component: "Backend (V66)"
symptom: "Issue_PRC_Mastconv job is not able to be completed in 10 hours"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-949
resolved: 2025-09-11
fix-version: ""
---

# BE-949: CS-1130 Issue_PRC_Mastconv job is not able to be completed in 10 hours

## 問題

Issue_PRC_Mastconv job is not able to be completed in 10 hours
Since there are item price setting down to loctaion, therefore the mastconv request long tijme to generate and cannot complete in 10 hours or longer.
As discuss with Bobby and Yau, we are thinking to separate item price in mastconv.
Let user have a way to generate.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-11
### Jira Comments (17 則)
**Andrew_Au** (2025-02-24):
@bobby Can I close the ticket ?
**Tovi Wang** (2025-02-24):
@@Andrew_Au I think this issue still under discussion.
CC @@Bobby @@Cy Lau  FYI.
**Andrew_Au** (2025-03-06):
@@Bobby Should I change the ticket status to Close
**Andrew_Au** (2025-03-20):
@bobby @@Cy Lau  Should I change the ticket status to Hold
**Joy Li** (2025-07-04):
Assigned to Shie-San to arrange sprint
@@Andrew_Au @@Tovi Wang
**Andrew_Au** (2025-07-10):
@@Joy Li  This issue pending for a long time. What status should I change ?
**Joy Li** (2025-07-11):
TP Jira ticket assigned to Shie-San for sprint arrangement.
Waiting for Shie-San to confirm when start.
**Cy Lau** (2025-08-21):
Total item price record would be 8M+ , and. effective pricing would be 6.8M+
With this among, it shall be believed that 10 hours may not be able to finish the mastconv job.
With StoreLoc specific approach, the roughly estimation would be around 60k+
---
With respect to the statics , there would be a proposal of reducing the number of records during normal mastconv.
Normal mastconv : export records except itmprx.
Itmprx records would be on-demand , by storeloc , to generate not expired record (both effective and effective to be)
This enhancement would cover
1. 
1. 
---
For the delivery timeframe, it would take 0.5 spirit for dev and unit test
and at least 1 day for QAQC. So it would suggest to put it in R25
**Cy Lau** (2025-08-29):
Confirmed as R25
**Cy Lau** (2025-08-31):
source checked to svn : 
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/CS2000BNV1_Prod
**Cy Lau** (2025-08-31):
@@Jerry Wong  please verify the enhancement with unit test
@@Sherman tse  @@Joy Li
**Jerry Wong** (2025-09-01):
db: 172.16.138.30,40002 csuser csuser
csdata01
Normal:
count = 62013
Location: (AC1SK)
count = 62001
Auto:
no skip table
skip itmprx
**Joy Li** (2025-09-01):
Email From @@Jerry Wong :
Release:
\\DS411\csms60\delivery\coach\DI9008-2025-09-01
Note:
‧	di9008.dll - Itmprx records would be on-demand by storeloc , to generate not expired record (both effective and effective to be)
‧	(di9008_auto) CS2000BNV1.exe in \\DS411\csms60\delivery\coach\DI9008-2025-09-01\di9008_auto
‧	di9008_add_config.sql – skip table to processing in di9008_auto
‧	JIRA BE-949
Sources:
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/CS2000
**Joy Li** (2025-09-01):
@@Sherman tse  Please start the testing.
ETA for this is next week.
**Automation for Jira** (2025-09-01):
Issue has been created since
Days since: 284
Week since : 40
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2025-09-11):
Verified on QA
**Release for DI9008:**
\\DS411\csms60\delivery\coach\DI9008-2025-09-01\NEW-09-09
**Release for DI9008  auto:**
\\DS411\csms60\delivery\coach\DI9008-2025-09-01\di9008_auto
**SQL:**
di9008_add_config.sql
**Joy Li** (2025-09-11):
released to Tapestry in BE V70R3.118 on 2025-09-11.

## 相關資訊

- Jira: [BE-949](https://ctil.atlassian.net/browse/BE-949)
- Fix Version: 未記錄
- 解決日期: 2025-09-11

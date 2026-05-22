---
tags: [faq, be, beapicrm]
component: "API"
symptom: "**Subject:** [HK][Alert] Error occurred when call ACXIOM CRM API: Profile Search"
root-cause: "待提取"
solution: "### Jira Comments (13 則)"
jira: BE-1062
resolved: 
fix-version: ""
---

# BE-1062: [HK][Alert] Error occurred when call ACXIOM CRM API: Profile Search

## 問題

**Subject:** [HK][Alert] Error occurred when call ACXIOM CRM API: Profile Search
ACXIOM CRM API return an error response. Please find IT support.
---------------------------------------------------
Endpoint:
v2/cdp/profile/search
Body:
{"pageSize":"100","pageNum":0,"queryCondition":{"operationType":"AND","subQueryConditions":[]}}
Error:
200; Invalid arguments, sub query condition is required
<span style="color:#ff991f">Error occurred time:</span>
<span style="color:#ff991f">0001-01-01 12:00:00</span>
where come from the <span style="color:#ff991f">Error occurred time</span>?
<span style="color:#ff991f">Error occurred time:</span>
<span style="color:#ff991f">0001-01-01 12:00:00</span>

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (13 則)
**Tovi Wang** (2025-04-28):
@@Anson Cheung @@Joy Li
FYI.If need CRMBEAPI log,please ping me.
**Tovi Wang** (2025-04-29):
@@Anson Cheung web22 BEAPI log here.Because copy Ali CRMBEAPI log need so many time.If need web21 BEAPI log.Please ping me again.
**Anson Cheung** (2025-04-29):
@@Tovi Wang For the <span style="color:#ff991f">Error occurred time</span>, a wrong value assigned, program fix is needed.
For the error “sub query condition is required”, a home phone is inputted but BEAPICRM and Acxiom is excepted the mobile phone. Do I need to map the home phone to mobile phone field to meet the search criteria?
**Tovi Wang** (2025-04-29):
@@Anson Cheung @@Cy Lau @@Joy Li
在QA我把电话号码不管是输入在 “住宅电话” 还是 “手提电话”，都可以搜索出来会员信息。
Follow video for your reference.
**Anson Cheung** (2025-04-30):
@@Tovi Wang Please get the QA BEAPICRM log for me, thanks
**Tovi Wang** (2025-05-06):
@@Anson Cheung QA CRMBEAPI log here.Please check.
Tel No: 15008476947
**Anson Cheung** (2025-05-06):
@@Tovi Wang   The error “sub query condition is required” cannot reproduce now, seems CRM response has changed.
**Tovi Wang** (2025-05-09):
@@Anson Cheung
“For the <span style="color:#ff991f">Error occurred time</span>, a wrong value assigned, program fix is needed.”
-->Please help to fix this one first.Thanks!
CC @@Joy Li @@Bobby
**Anson Cheung** (2025-05-09):
Release
[\\ds411\public\samuel\beapi\v1.7.19_20250509](file://ds411/public/samuel/beapi/v1.7.19_20250509)
-
**Tovi Wang** (2025-05-09):
@@Joy Li @@Bobby @@Sherman tse @@Joseph_Hu  Anson has provided the Release.Please help to next action.Thanks!
**Tovi Wang** (2025-05-09):
@@Anson Cheung This Release fixed all Email alert error occurred time,right?
**Anson Cheung** (2025-05-12):
@@Tovi Wang yes
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi Please update the ticket status

## 相關資訊

- Jira: [BE-1062](https://ctil.atlassian.net/browse/BE-1062)
- Fix Version: 未記錄
- 解決日期: 未記錄

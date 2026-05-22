---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Hi Bobby/Sanyo Team,"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1027
resolved: 2026-05-05
fix-version: ""
---

# BE-1027: [CS-1374] Issue-PRC-[Alert] Error occurred when call ACXIOM CRM API

## 問題

Hi Bobby/Sanyo Team,
We received an alert that when cs2000 call acxiom CRM API, could you help to investigate the reason.
Error occurred time: 2025-03-07 04:52:05 to 2025-03-07 04:59:54
1. 
1. 
Please ping me directly if any log needed, I'll try to get them.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-05
### Jira Comments (13 則)
**Tovi Wang** (2025-03-10):
@@Anson Cheung Please help to check this issue.Thanks!
正在让同事copy CRMBEAPI log,还需要哪些log请提前和我说。
@@Jason Wu @@Bobby  可以提供log path让Dahui帮忙拿log。
**Tovi Wang** (2025-03-10):
@@Anson Cheung CRMBEAPI log for your further checking.Thanks!
CC @@Bobby @@Cy Lau
**Tovi Wang** (2025-03-11):
@@Anson Cheung As talked in teams.Please help to double check and confirm if anything error in our logs at that time zone.
1.Error occurred time: 2025-03-07 16:52:05 HKT to 2025-03-07 16:59:54 HKT
2.Error occurred time: 2025-03-10 14:23 HKT
**Anson Cheung** (2025-03-11):
@@Tovi Wang  CRM API returns: {"code":"CDP-CUST-404","message":"Customer not found","data":null}, 
it caused an email alert sent.
**Tovi Wang** (2025-03-11):
@@Anson Cheung Many Thanks for your double check.Let me share the details to Coach team first.
**Tovi Wang** (2025-03-11):
@@Anson Cheung One more question.这个Alert Email是我们设定并且发出去的嘛？
**Anson Cheung** (2025-03-11):
@@Tovi Wang Yes
**Tovi Wang** (2025-03-11):
@@Anson Cheung @@Bobby
As talked in CRM daily meeting.正常应该是用手机号去CRM request data,而不应该是会员号。Please help to double check and confirm.
**Tovi Wang** (2025-03-14):
@@Bobby @@Anson Cheung Please help to prepare the new released and ETA with high priority.Thanks!
**Anson Cheung** (2025-03-21):
Release:
[\\ds411\public\samuel\beapi\v1.7.10_20250319](file://ds411/public/samuel/beapi/v1.7.10_20250319)
- 
-
**Andrew_Au** (2025-10-08):
@@Tovi Wang Please update the status
**Tovi Wang** (2025-10-09):
Fixed,Please closed.
**Automation for Jira** (2025-10-09):
Issue has been created since
Days since: 212
Week since : 30
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [BE-1027](https://ctil.atlassian.net/browse/BE-1027)
- Fix Version: 未記錄
- 解決日期: 2026-05-05

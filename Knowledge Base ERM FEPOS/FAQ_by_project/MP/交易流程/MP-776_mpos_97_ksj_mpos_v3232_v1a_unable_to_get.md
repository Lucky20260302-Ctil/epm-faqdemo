---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Neil callout during testing for **COACH_MPOSWebAPI_3.23.2-v1a_KSJ.zip**, for the customer just regis"
root-cause: "待提取"
solution: "### Jira Comments (14 則)"
jira: MP-776
resolved: 
fix-version: ""
---

# MP-776: [MPOS-97] KSJ MPOS - v3.23.2-v1a - Unable to get just-registered vip info

## 問題

Neil callout during testing for **COACH_MPOSWebAPI_3.23.2-v1a_KSJ.zip**, for the customer just register via SFCC. CS2K able to get the vip info, but MPOS can not. vip phone no: 1778148266,UI log(apawiqwposweb02) uploaded. FE Testing machine IP: 172.24.253.70(C424). Kindly help to check.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (14 則)
**Tovi Wang** (2025-05-23):
@@Daniel Leung  Please help to take a look this issue.All MPOS logs in Jira ticket MPOS-95. Thanks!Thanks!
CC @@Cy Lau @@Joy Li
**Cy Lau** (2025-05-23):
From FEPOS WA Log  searching with mobileno:1778148266
MPOS Log:
Even FEPOS got the +ve result until 18:50:37, 18:50:48 already giving -ve result
Next check the BEAPI log to see the result
**Daniel Leung** (2025-05-23):
@@Tovi Wang Please also get the beapi log and pos api log, thanks
**Tovi Wang** (2025-05-23):
@@Daniel Leung @@Cy Lau
apawiqwposweb02 server没有05-22的BEAPI log…
**Tovi Wang** (2025-05-23):
@@Daniel Leung
05-22 POS API for your checking.
**Daniel Leung** (2025-05-23):
# @@Tovi Wang  Can you get apawiqwposweb<span style="color:#4c9aff">**01**</span> beapi log and pos api log? Thanks
**Tovi Wang** (2025-05-26):
@@Daniel Leung apawiqwposweb<span style="color:#4c9aff">**01**</span> server NOT have 05-22 beapi log.bellow capture for your reference.
**Tovi Wang** (2025-05-26):
@@Daniel Leung Web01 POS_API log here.
But apawiqwposweb<span style="color:#4c9aff">**01**</span> server NOT have 05-22 beapi log.bellow capture for your reference.
**Daniel Leung** (2025-05-26):
This error message is coming from C360
**Tovi Wang** (2025-05-26):
@@Daniel Leung Many Thanks for your double confirm.I has updated in Coach Jira ticket.
CC @@Joy Li @@Cy Lau
**Andrew_Au** (2025-09-30):
@@Tovi Wang Please update the status
**Andrew_Au** (2025-10-08):
@@Tovi Wang @@Joy Li Please update the status
**Tovi Wang** (2025-10-09):
Fixed,Please closed.
**Automation for Jira** (2025-10-09):
Issue has been created since
Days since: 138
Week since : 19
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [MP-776](https://ctil.atlassian.net/browse/MP-776)
- Fix Version: 未記錄
- 解決日期: 未記錄

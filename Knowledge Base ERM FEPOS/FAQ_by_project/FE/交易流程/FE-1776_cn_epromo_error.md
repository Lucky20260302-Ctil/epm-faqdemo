---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Issue details:"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1776
resolved: 
fix-version: ""
---

# FE-1776: CN Epromo error

## 問題

Issue details:
User reported that when she submit an coupon in CS2000, error "The connection to the SMTP server failed with SmtpStatusCode: ServiceNotAvailable" and "You do not have the permission to perform this action."
Region: PRC 11
UserID: Aliu05
Related coupon: 1023RTWSS

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Tovi Wang** (2025-10-24):
Hi @@Cy Lau Could someone help to take a look this issue and give some advice?Thanks!
CC @@Joy Li @@Bobby
**Cy Lau** (2025-10-27):
after support team describe ,
"The connection to the SMTP server failed with SmtpStatusCode: ServiceNotAvailable" 
maybe various reasons.
"You do not have the permission to perform this action." may not related to permissions.
Woud like to investigate the BEDB log with crossing coding , but being told it is too large to query.
@@Joy Li  perhaps a clearnace for the log before we do the investigation ?
**Cy Lau** (2025-10-27):
Meanwhile , @@Jerry Wong  ,
Please cosolidate the source of exception which will give out these two error :
"The connection to the SMTP server failed with SmtpStatusCode: ServiceNotAvailable"
"You do not have the permission to perform this action."
**Tovi Wang** (2025-10-27):
@@Jerry Wong @@Cy Lau@@Joy Li  Many Thanks for your check and advice.
@@Jerry Wong As we talked.I has shared our details found to Coach [team.](http://team.QA) Testing in QA is normal in our side.They will create new MM coupon to double check the error if gone or not.I will keep monitoring.Thanks!
**Tovi Wang** (2025-11-03):
Not callout again.Closed first.
**Automation for Jira** (2025-11-03):
Issue has been created since
Days since: 9
Week since : 1
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1776](https://ctil.atlassian.net/browse/FE-1776)
- Fix Version: 未記錄
- 解決日期: 未記錄

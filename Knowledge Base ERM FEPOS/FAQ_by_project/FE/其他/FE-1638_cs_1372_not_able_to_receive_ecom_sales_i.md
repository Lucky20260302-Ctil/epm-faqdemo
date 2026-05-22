---
tags: [faq, fe, 其他]
component: "Service"
symptom: "for example."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1638
resolved: 2025-07-04
fix-version: ""
---

# FE-1638: [CS-1372] Not able to receive Ecom sales import alert email

## 問題

for example.
1.We have import error on TW 2025-02-07, but i dont have TW Ecom sales imorting alert email.
2.and you can find Coach support team is in receiption list.
Web url:
[https://cs2000web.coach.com/cs2000v4/csplus/WP0002](https://cs2000web.coach.com/cs2000v4/csplus/WP0002)
user name:SXD
PWD:000000
Troubleshooting:
1.我们看到02-07 TW Ecom sales 有 import error.
1. 
我看到有 I_ITEM  and   I_EAN     error.有发送Email Alert.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-04
### Jira Comments (19 則)
**Tovi Wang** (2025-03-05):
@@Anson Cheung @@Jerry Wong 这个Email alert issue帮忙看一下。在CS2K web设置了 Ecom sales error Email alert.有error时但是没有触发Email alert.Please help to take a look and advice.Thanks!
CC @@Bobby @@Cy Lau
**Bobby** (2025-03-06):
@@Anson Cheung @@Jerry Wong, could you help to follow up this issue with Tovi?
cc @@Cy Lau for your visbility.
**Anson Cheung** (2025-03-06):
CSPlus web WP0002 will modify the backend table ‘alertcnf' and 'alertacc’.
**Anson Cheung** (2025-03-07):
@@Tovi Wang  Can you get the log of ALCHKPOLL program?
**Tovi Wang** (2025-03-10):
Dear ALL,
same issue with Jira FE_1644.
We can closed this one first.
**Ken Wang** (2025-05-16):
@@Tovi Wang please contact Sophia to get the log of ALCHKPOLL program to see why email sending failure. (Is the SP failed to add record to ‘alertcnf' and 'alertacc’?)
**Tovi Wang** (2025-05-16):
@@Ken Wang Sure.Thanks!
Let me copy the log of ALCHKPOLL program first.But I can’t access the Job server. Thanks!
@@Joy Li Can you access the job server to got the log?Thanks!
QA job server:
|  |
| --- |
|  |
**Tovi Wang** (2025-05-19):
@@Anson CheungAs talked in teams. Log here.Please help to further checking.Thanks!
CC @@Joy Li @@Ken Wang  FYI.
**Tovi Wang** (2025-05-19):
@@Anson Cheung  Pro 13 MY region log for your reference,
**Tovi Wang** (2025-05-20):
@@Anson Cheung All log here.Please further checking and give an update in today.Thanks!
\\Apawiqwposapp21\csms70\ALCHKIMPORT14
**Anson Cheung** (2025-05-20):
@@Tovi WangThe email sending program work normally. It only sends email if error record exists in table 'erralert'. Based on the data you provide, there is no record for erralert_type = 'I_WEBSAL'.
**Tovi Wang** (2025-05-20):
@@Anson Cheung Many Thanks for your double confirm.
@@Cy Lau @@Joy Li @@Bobby @@Anson Cheung Could you help to further checking why I_WEBSAL error info NOT write to erralert table?What’s the details setting logic and design?Or could you advice how to explain this issue to Coach team?Thanks!
**Cy Lau** (2025-05-20):
@@Jerry Wong  , @@Bobby
Please advise that which module would possible for I_WEBSAL ?
And corresponding error info handling
**Jerry Wong** (2025-05-21):
I found that the program call Coach_ECOMM, but erralert type is I_ECOM_SAL based on interlog_file_type = 102
**Cy Lau** (2025-05-23):
@@Jerry Wong so in case with that erralert type ‘I_ECOM_SAL’ does it include in email alert list ?
**Jerry Wong** (2025-05-23):
@@Cy Lau @@Tovi Wang said erralert type ‘I_ECOM_SAL’ does not include in alertcnf table, and not have this record in erralert table. So, I’m waiting for Tovi to send me the eCom sales log.
**Tovi Wang** (2025-05-23):
@@Cy Lau @@Joy Li @@Jerry Wong As talked in teams.Bellow capture for your reference.
select * from alertcnf where alertcnf_pgcode in ('I_WEBSAL','I_ITEM','I_EAN')
---Can normal send email alert for intertyp 07(Item Master)
select intertyp_desc, interlog.* from interlog join intertyp on (interlog_type=intertyp_type)
where interlog_file_date ='2025-02-07' and interlog_type = '07'
---Can't send email alert for intertyp 102(eCom Sales)
select intertyp_desc, interlog.* from interlog join intertyp on (interlog_type=intertyp_type)
where interlog_file_date ='2025-02-07' and interlog_type = '102'
select * from erralert where erralert_date = '2025-02-07'
**Cy Lau** (2025-05-27):
advice : adding the config I_ECOM_SAL in alertcnf
**Joy Li** (2025-07-04):
released on 2025-05-15 with BE V70R3.103

## 相關資訊

- Jira: [FE-1638](https://ctil.atlassian.net/browse/FE-1638)
- Fix Version: 未記錄
- 解決日期: 2025-07-04

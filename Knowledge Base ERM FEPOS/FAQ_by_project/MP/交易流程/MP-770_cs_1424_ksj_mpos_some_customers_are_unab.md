---
tags: [faq, mp, 交易流程]
component: "MPOS API"
symptom: "As KSJ MPOS performance has been improved(Ref: [CS-1339](https://jira.tapestry.support/browse/CS-133"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-770
resolved: 2025-07-04
fix-version: ""
---

# MP-770: [CS-1424] KSJ MPOS : Some customers are unable to be selected on mPOS

## 問題

As KSJ MPOS performance has been improved(Ref: [CS-1339](https://jira.tapestry.support/browse/CS-1339)) KSJ mPOS pilot stores started using mPOS from April 23rd.
SOG received callout from the stores that they can search the member on mPOS however when select the customer to attach to the transaction,they got an error "400 Invalid customer type" there`re also customers who has no issuand able to search and select to the transaction
Sample:es
Store Code :C312
Phone number : 09021616611 (Failed with Invalid customer type)
Phone number: 09046067786 (No issues for search and select to the transaction)
*These 2 phone numbers are store associatets`s
*Pls refer the screenshot attached to the ticket
Store C320 also callout that when search by Customer ID, they got the error "C360 connection error(400)Bad Request"
KSJ mPOS pilot stores:
J312(KSJ Kisarazu Outlet)
J309(KSJ Gotemba Outlet)
C311( KSJ Karuizawa Outlet)
C316 (KSJ Rinku Outlet)
C318 (KSJ Sanda Outlet)
C320 (KSJ Nagashima Outlet)
C322 (KSJ Tosu Outlet)
1.On 06 May, Neil connected to C320, did some member search, able to reproduce the issue reported from store. log was uploaded, testing vip phone no is 0542617762. Member No: 2017368212.Kindly help to check the log. BTW, He also did same testing in QA Env, no such issues.
2.We can see the “Error: [400] 無効な顧客タイプです。” from MPOS UI log:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-04
### Jira Comments (17 則)
**Tovi Wang** (2025-05-07):
@@Cy Lau @@Daniel Leung Please Help to take a look this issue.Details MPOS log here.
CC @@Joy Li
**Tovi Wang** (2025-05-07):
Add one more info from Shie.
**Daniel Leung** (2025-05-08):
@@Tovi Wang I think data in [dbMas].[dbo].[TblVipTyp] is different between C320 and QA env. Please check the member type is contain in this table or not.
**Tovi Wang** (2025-05-08):
@@Daniel Leung Thanks for your info.One more question.As I know,KSJ member was return from C360,right?
这和Dbmas 的member data有关嘛？
**Daniel Leung** (2025-05-08):
@@Tovi Wang It should be, only member type validation will return this error message
**Tovi Wang** (2025-05-08):
1.C320 Till0 pro env [dbMas].[dbo].[TblVipTyp] table
2.C309 Till0 QA env [dbMas].[dbo].[TblVipTyp] table
**Tovi Wang** (2025-05-09):
@@Daniel Leung @@Cy Lau
For KSJ MPOS, PRD QA testing version is totally same, API version: COACH_MPOSWebAPI_3.23.2-b2B_KSJ, IPA version: v3.23.1
CC @@Joy Li @@Bobby
**Tovi Wang** (2025-05-09):
[https://tapestry.zoom.us/rec/share/y9GmVv34Pj7di1BKh97hFmzrF28cghRrOZeoPE5G-kXdeEgHw6hNqKOb0zaaUgc.oMBw8S0cH-At7Rbs](https://urldefense.com/v3/__https:/tapestry.zoom.us/rec/share/y9GmVv34Pj7di1BKh97hFmzrF28cghRrOZeoPE5G-kXdeEgHw6hNqKOb0zaaUgc.oMBw8S0cH-At7Rbs__;!!HzN2yyM!jpZXwY7m13XjkggBNloZ6hu0Kiob_Cic4695Rg4zwD0AhLL_iQygB-21TN5rZlzl4OP3EggOSTblaW2T$)刚才PRD的录屏
**Tovi Wang** (2025-05-09):
@@Daniel Leung @@Cy Lau
1.QA MPOS log:
From Neil:
08076881179这个手机号在QA DB查不到会员的，但是在C360有存在的。QA MPOS可以通过手机号搜索到这个会员并且可以select到这个会员
2.PRO MPOS log:
**Cy Lau** (2025-05-15):
\\ds411\share\POS_MPOS_Release\3.23.2\3.23.2-20250515-b1
Situation:
1. 
2. 
3. 
400 - Invalid member type error return
Updates:
1) GetMember flow for C360 align with FEPOS: Get From local for temp member
**Cy Lau** (2025-05-15):
Please also test for
3.29.X
3.30.X
The get member flow switched from getmember-> getmembers
**Tovi Wang** (2025-06-12):
@@Daniel Leung @@Cy Lau  As talked in teams.All logs here.Please help to further checking.
**Tovi Wang** (2025-06-12):
@@Daniel Leung As talked in teams.
把 EnableVerifyBirthday N掉再测一下也是同样error.UI log里面可以看到400 error.
UI log和录屏都在下面。Please further checking
UI log:
{className: API, methodName: httpGetDataAsync, text: httpClient:921339929 URL:[https://10.250.7.31/sanyoservice.api.fe_38/api/v1/Members/1173942824?noValidation=false,](https://10.250.7.31/sanyoservice.api.fe_38/api/v1/Members/1173942824?noValidation=false,) timestamp: 12 June 2025 10:58:03 AM, timeInMillis: 1749697083565, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: API, methodName: responsehandling2, text: httpClient:921339929 API:StatusCode:400, timestamp: 12 June 2025 10:58:04 AM, timeInMillis: 1749697084722, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: API, methodName: responsehandling2, text: httpClient:921339929 Error: [400] 無効な顧客タイプです。, timestamp: 12 June 2025 10:58:04 AM, timeInMillis: 1749697084723, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null}
{className: _ErrorPageState, methodName: inintState, text: Error: [400] 無効な顧客タイプです。, timestamp: 12 June 2025 10:58:04 AM, timeInMillis: 1749697084736, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null}
{className: MemoController, methodName: doExit, text: User performs exit, timestamp: 12 June 2025 10:58:16 AM, timeInMillis: 1749697096184, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: MemoController, methodName: doExit, text: User performs exit without Save - Yes, timestamp: 12 June 2025 10:58:17 AM, timeInMillis: 1749697097089, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
.
**Tovi Wang** (2025-06-12):
@@Daniel Leung 最新测试的MPOS log.
**Tovi Wang** (2025-06-12):
@@Cy LauJira ticket CS-1424,MPOS log here.PLease help to further checking as Neil said.
**Daniel Leung** (2025-06-13):
@@Tovi Wang fixed version means 3.29.6?  And also please get the UI log, thanks
**Tovi Wang** (2025-06-13):
@@Daniel Leung For question “fixed version means 3.29.6?“,I not confirm this question,
@@Joy Li @@Cy Lau Could you help to confirm this question?Thanks!
I am waiting SOG team upload the UI log,Let me send Email tracing the UI log.

## 相關資訊

- Jira: [MP-770](https://ctil.atlassian.net/browse/MP-770)
- Fix Version: 未記錄
- 解決日期: 2025-07-04

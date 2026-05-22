---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API, MPOSPrint.exe"
symptom: "J388 Kyoto Takashimaya mens"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-818
resolved: 2026-04-17
fix-version: ""
---

# MP-818: [CS-2505] Cloud IIS MPOS Performance - Printing

## 問題

J388 Kyoto Takashimaya mens
3月19日 JST 17:06 MA002330
最後の完了ボタンが進まずレシートが印刷されないが、POSには反映されている。
However it is already reflcted this transation in POS side, needed to re-print receipt.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-04-17
### Jira Comments (6 則)
**Cy Lau** (2026-03-26):
Printing flow :
RCA would be tentative the
1) MPOSPrint connections VS CloudPrintHub.
2) Long waiting owing to Upload result failed from CloudhubNotificationService VS MPOS API
**Automation for Jira** (2026-03-26):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Cy Lau** (2026-04-08):
CloudPrintHubNotification : 
\\ds411\share\POS_MPOS_Release\CloudPrintHubNotification\20260331_1.0.0.5
MPOS  - with v75 R24 :
\\ds411\share\POS_FE_Release_64\20260408 Coach v750.04R24
**Daniel Leung** (2026-04-08):
MPOS API: \\ds411\share\POS_MPOS_Release\3.30.x\3.30.7-20260408.1
MPOS:[🔗](https://ios.ctil.com/mpos/PreCoach/) - 3.30.8-20260415.1
@@Cy Lau @@Joy Li @@Sherman tse
**Daniel Leung** (2026-04-14):
Release note:
MPOS : Printing status UI update , will display printing status now. Retry button will be shown if printing error or timeout.
MPOS API:
     1.  Will send JWT token to CloudPrintHub
     2. CloudPrintHub will use this token to authenticate when calling the check status api
CloudPrintHub : 
    1.  Will receive a JWT token from MPOS API and store it in CloudPrintHubNotification_[date].db - Requests table.
    2. Will pass the JWT token to check status api 
@@Sherman tse please Test:
1. MPOS UI display for success, error, and timeout.
2. MPOS is able to retry or exit the printing flow if an error occurs
3. Error handling if CloudPrintHub is down.
4. Error handling if MPOS Print is down.
5. Error handling if MPOS API is down.
6. Error handling if FE is down
7. Error handling if Network is slow or down
8. Error handling if JWT token is removed/changed
Feel free to add more test cases.
**Joy Li** (2026-04-17):
PrintHub release: [MPOSPrintHub_1.0.0.5](https://jira.tapestry.support/issues/?jql=project+%3D+CS+AND+fixVersion+%3D+MPOSPrintHub_1.0.0.5)
- 
FE package : [FE_V75.004.2400.0000](https://jira.tapestry.support/issues/?jql=project+%3D+CS+AND+fixVersion+%3D+FE_V75.004.2400.0000)
- 
- 
MPOS IPA : [MPOS IPA 3.30.8-20250415.1](https://jira.tapestry.support/issues/?jql=project+%3D+CS+AND+fixVersion+%3D+%22MPOS+IPA+3.30.8-20250415.1%22)
- 
MPOS API : [MPOS API 3.30.7](https://jira.tapestry.support/issues/?jql=project+%3D+CS+AND+fixVersion+%3D+%22MPOS+API+3.30.7%22)
-

## 相關資訊

- Jira: [MP-818](https://ctil.atlassian.net/browse/MP-818)
- Fix Version: 未記錄
- 解決日期: 2026-04-17

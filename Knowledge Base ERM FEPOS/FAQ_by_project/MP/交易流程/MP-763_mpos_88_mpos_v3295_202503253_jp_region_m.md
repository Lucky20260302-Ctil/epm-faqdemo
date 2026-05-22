---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Hi [Bobby Chu](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Bobby_Chu) , [Tovi Wang](h"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-763
resolved: 2025-05-02
fix-version: ""
---

# MP-763: [MPOS-88] MPOS - v3.29.5 20250325.3 JP region member search issue

## 問題

Hi [Bobby Chu](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Bobby_Chu) , [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) , for v3.29.5 20250325.3, JP region we found member search issue. kindly help to check, testing machine ip J805(IP: 172.24.253.20), log also upload to apawiqwposweb24. vip phone no: 17781482669(This member able to get via CS2K)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (6 則)
**Tovi Wang** (2025-03-28):
@@Sherman tse As talked in teams.Please help to double confirm if can reproduced this issue in our JP QA MPOS.Thanks!
CC: @@Cy Lau @@Bobby @@Daniel Leung
**Tovi Wang** (2025-03-31):
@@Daniel Leung @@Cy LauMPOS log for your further checking.Thanks!
**Tovi Wang** (2025-04-01):
@@Cy Lau @@Daniel Leung From MPOS UI log,We can found the Error: [404] 記録が見当たりませんでした.Please help to further checking.
{className: API, methodName: httpGetDataAsync, text: httpClient:908800109 URL:[https://10.250.11.217/sanyoservice.api.fe_18/api/v1/Members?pagingParameters.page=1&pagingParameters.pageSize=100&search.vipPhoneNo=17781482669,](https://10.250.11.217/sanyoservice.api.fe_18/api/v1/Members?pagingParameters.page=1&pagingParameters.pageSize=100&search.vipPhoneNo=17781482669,) timestamp: 28 March 2025 10:01:59 AM, timeInMillis: 1743127319155, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: API, methodName: responsehandling2, text: httpClient:908800109 API:StatusCode:200, timestamp: 28 March 2025 10:02:00 AM, timeInMillis: 1743127320739, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: API, methodName: responsehandling2, text: U2FsdGVkX1+gAcnUQkC/EMzpUXQjmvjQsaqHvRIOXpFbuUnUwmuVe7qHf5n6ooF61MEr7M9d535MGbAKgM4IaiVkPN/Fem7TzYquSN3Y+k3xoizwB0BHI9fq6rIoKk6vCFn/M2+mt2yXk1aeRtix/1DmvTzuXzCtf41vTzjqJcA=, timestamp: 28 March 2025 10:02:00 AM, timeInMillis: 1743127320740, exception: null, dataLogType: null, logLevel: LogLevel.WARNING, stacktrace: null}
{className: _MemberEnquiryState, methodName: getMembersList->vipPhoneNo, text: Error: [404] 記録が見当たりませんでした。, timestamp: 28 March 2025 10:02:00 AM, timeInMillis: 1743127320741, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null}
**Cy Lau** (2025-04-01):
@@Tovi Wang 
As you mentioned , the log you provided is only showing the error on MPOS IPA :
there is no other log on the searching operations.
**Cy Lau** (2025-04-01):
@@Tovi Wang 
After Dev team access to the webserver for additional log , the error is obviously showing the wrong config of BEDB:
After correction on the config , 200 result has been made via swagger:
**Sherman tse** (2025-05-02):
Issue has been closed in Tapestry JIRA
Close case
[https://jira.tapestry.support/browse/MPOS-88](https://jira.tapestry.support/browse/MPOS-88)

## 相關資訊

- Jira: [MP-763](https://ctil.atlassian.net/browse/MP-763)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

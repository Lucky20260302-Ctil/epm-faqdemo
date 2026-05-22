---
tags: [faq, web, member_api]
component: "API"
symptom: "According to test result, we expect the following improvement:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: WEB-376
resolved: 2025-01-03
fix-version: ""
---

# WEB-376: [ACU-73]Performance Improvement on member/upsert Interface of POS

## 問題

According to test result, we expect the following improvement:
1, Improve single call performance(currently is more than 4s)
2, Could support more concurrency number(currently if more than 25 vusers ,the api starts not available)
3, Inspect the dead lock issue and try to evite this issue happened(refer to test result)
4, This test result is baed on  QA environment.
Following is the test result:
1, Manually call api to test if performance fulfill baseline requirement(response time less than 200ms and accuracy is more than 99%)
Failed: response time is more than 4s commonly
2, Try 2 vusers to test check if system could support concurrency testing
Failed:
2vuser per 1s  with different member for 566 times:
Avg RT: 5112ms is more than 200ms but with one failed call.
3, Find out when will appear error when we increase concurrency:
We found when vuser number is more than 25, there starts to appear failed call and api start to be unavailable.
1. 
{"successful":false,"data":\{"errorType":"Exception","errorCode":9999,"errorMessage":"Transaction (Process ID 179) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction.","errorDetails":null,"errorDisplayMessage":"","errorDesc":"","message":"Transaction (Process ID 179) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction."}

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-01-03
### Jira Comments (11 則)
**Jason Wu** (2024-12-05):
@@Tovi Wang Please help to copy the logs then assign the ticket to Dev team.
**Tovi Wang** (2024-12-05):
Coping the external logs with SOG team.
**Tovi Wang** (2024-12-05):
@@Cy Lau  External server log for your reference.
**Jason Wu** (2024-12-05):
@@Tovi Wang  This is not an SQLite log, please inform SOG try again.
**Tovi Wang** (2024-12-06):
@@Cy Lau @@Jason Wu This is QA web21 BEAPICRM log.Please check.
**Tovi Wang** (2024-12-06):
@@Cy Lau @@Jason Wu  This is QA web22 BEAPICRM log.Please check.
**Anson Cheung** (2024-12-06):
after observation, the deadlock is most likely caused by the read/write on 'wtmnlog' table
if update 'wtmnlog' is not necessary, config ‘wtmnlog' in appsettings.json  can be set to 'N’ to skip it.
**Cy Lau** (2024-12-09):
@@Joy Li  @@Tovi Wang 
Please reference to @@Anson Cheung 's suggestion 
ETA : 09Dec / 10 Dec
**Andrew_Au** (2024-12-24):
@@Sherman tse  Please update the ticket status
**Sherman tse** (2024-12-24):
Verified on qa
test case attached
**Joy Li** (2025-01-03):
Tested by @@Sherman tse  and released by @@Joy Li  on 2025-01-03

## 相關資訊

- Jira: [WEB-376](https://ctil.atlassian.net/browse/WEB-376)
- Fix Version: 未記錄
- 解決日期: 2025-01-03

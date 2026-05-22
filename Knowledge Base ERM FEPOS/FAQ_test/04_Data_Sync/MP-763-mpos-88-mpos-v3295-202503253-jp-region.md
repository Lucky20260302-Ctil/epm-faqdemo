---
project: MP
issue_key: MP-763
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-763"
created: 2025-03-28
resolved: 2025-05-02
resolution: Done
has_images: True
---

# MP-763: [MPOS-88] MPOS - v3.29.5 20250325.3 JP region member search issue

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.5
> **解決日期:** 2025-05-02
> **負責人:** Tovi Wang
> **組件:** MPOS

## 問題描述

Hi [Bobby Chu](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Bobby_Chu) , [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) , for v3.29.5 20250325.3, JP region we found member search issue. kindly help to check, testing machine ip J805(IP: 172.24.253.20), log also upload to apawiqwposweb24. vip phone no: 17781482669(This member able to get via CS2K)

> 📎 **image-20250328-082450.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/25d3dbba-8c8f-4685-9893-242d9b13a03d)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250328-082450.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/25d3dbba-8c8f-4685-9893-242d9b13a03d)


## Jira Comments

> **Tovi Wang** (2025-03-28):
>  As talked in teams.Please help to double confirm if can reproduced this issue in our JP QA MPOS.Thanks! CC:     

> **Tovi Wang** (2025-03-31):
>   MPOS log for your further checking.Thanks!    

> **Tovi Wang** (2025-04-01):
>    From MPOS UI log,We can found the Error: [404] 記録が見当たりませんでした.Please help to further checking. {className: API, methodName: httpGetDataAsync, text: httpClient:908800109 URL: https://10.250.11.217/sanyoservice.api.fe_18/api/v1/Members?pagingParameters.page=1&pagingParameters.pageSize=100&search.vipPhoneNo=17781482669,  timestamp: 28 March 2025 10:01:59 AM, timeInMillis: 1743127319155, exception: null, dataLogType: null, logLevel:  LogLevel.INFO , stacktrace: null} {className: API, methodName: responsehandling2, text: httpClient:908800109 API:StatusCode:200, timestamp: 28 March 2025 10:02:00 AM, timeInMillis: 1743127320739, exception: null, dataLogType: null, logLevel:  LogLevel.INFO , stacktrace: null} {className: API, methodName: responsehandling2, text: U2FsdGVkX1+gAcnUQkC/EMzpUXQjmvjQs

> **Cy Lau** (2025-04-01):
>   As you mentioned , the log you provided is only showing the error on MPOS IPA : there is no other log on the searching operations.

> **Cy Lau** (2025-04-01):
>   After Dev team access to the webserver for additional log , the error is obviously showing the wrong config of BEDB: After correction on the config , 200 result has been made via swagger:

> **Sherman tse** (2025-05-02):
> Issue has been closed in Tapestry JIRA Close case https://jira.tapestry.support/browse/MPOS-88

## 相關資訊

- **Jira:** [MP-763](https://ctil.atlassian.net/browse/MP-763)
- **解決方式:** Done
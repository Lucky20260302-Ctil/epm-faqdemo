---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Environment: Prorunner 01 Production"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-721
resolved: 2023-11-16
fix-version: ""
---

# BE-721: Cannont load to view Physical Adjustment Process Modify

## 問題

Environment: Prorunner 01 Production
ACC: sx1                        PW: sx1
Location: Physical Adjustment Process > Create > Create New Batch > Click on that Batch >
Reproduce step
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
Attachment for your reference but onlt fit in 01 production DB

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-11-16
### Jira Comments (3 則)
**Jacky Lam** (2023-02-24):
Assigned to @@Hans Wong, for your information @@Jerry Wong
**Hans Wong** (2023-02-24):
@@Jerry Wong is investigating the front-end code to determine if there can have any improvement to handle the request sequence, otherwise, the whole UI and API may need to be re-worked accordingly.
FYR, currently, for 50 records, the page will generate 100+ request to server, takes 80+ sec to display finally.
but the client has thousands of records to display, this is impossible for the client browser and server to finish the job, it is like the client attacking web server (plus DB) by DDOS method with just 1 browser generating a few thousands of requests.
CC: @@Thomas, @@Johnny Cheung
**Hans Wong** (2023-02-24):
server is [https://172.16.138.55/ChainStorePlus_AIGLE](https://172.16.138.55/ChainStorePlus_AIGLE)
screenshot1 is the test item
screenshot2 displayed the record count for test

## 相關資訊

- Jira: [BE-721](https://ctil.atlassian.net/browse/BE-721)
- Fix Version: 未記錄
- 解決日期: 2023-11-16

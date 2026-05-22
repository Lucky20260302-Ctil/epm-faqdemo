---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "QA CN POS: 10.33.248.4"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1648
resolved: 2025-05-02
fix-version: ""
---

# FE-1648: [ACU-119]Always 0 for each field on member profile page while querying CN member with exit_permit=1 on HK POS FE

## 問題

QA CN POS: 10.33.248.4
QA HK POS:  10.33.248.2
Reproduce steps:
1. 
2. 
3.Query CN member with mobile '19921610075' on HK POS FE, the member information will be displayed as bellow:
4.But Click Profile button, There is always 0 for each field.@@Anson Cheung  Is this expected display or bug?Please clarify.Thanks!

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (10 則)
**Tovi Wang** (2025-03-13):
@@Anson Cheung CRM logs for your further checking.Please help to check.
CC @@Bobby
**Anson Cheung** (2025-03-13):
@@Tovi Wang CRM return null so the screen displays as 0.
**Tovi Wang** (2025-03-13):
@@Anson Cheung Many Thanks For your double confirm.what about the CN POS?CN POS上搜索的时候CRM回的是有值的，right?
**Anson Cheung** (2025-03-13):
@@Tovi Wang This issue is due to the wrong mapping for search members in out border, program fix is needed.
**Anson Cheung** (2025-03-13):
Release:
[\\ds411\public\samuel\beapi\v1.7.7_20250313](file://ds411/public/samuel/beapi/v1.7.7_20250313)
-
**Tovi Wang** (2025-03-14):
@@Bobby @@Jason Wu @@Cy Lau  @@Joseph_Hu Could you please help to arrange the testing and provide me the ETA?Coach Yoyo are asking me the released ETA.Thanks!
**Cy Lau** (2025-03-14):
QAQC team , represented by @@Sherman tse  please make a reasonable ETA for your testing for @@Tovi Wang
**Joseph_Hu** (2025-03-14):
QAQC: 3-14, 3-17
**Sherman tse** (2025-03-14):
Verified on QA
test case attached
**Sherman tse** (2025-05-02):
Issue has closed in Tapestry JIRA,
Close case

## 相關資訊

- Jira: [FE-1648](https://ctil.atlassian.net/browse/FE-1648)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

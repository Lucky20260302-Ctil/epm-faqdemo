---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "When KSJ store staff search customer, even customer birth year info is exist in C360."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1649
resolved: 2025-10-03
fix-version: ""
---

# FE-1649: [CS-1360] KSJ_CS2K_show birth year as 1900, when staff search customer

## 問題

When KSJ store staff search customer, even customer birth year info is exist in C360.
however customer search result on CS2K showing as birth year as 1900.
CRM team confirmed this customer data in C360 and see this data has right birth date.
can you look into API logic?
#==< C360 >================================
Customer No : 1209510912
Name        : 佐川 愛実
Kana Name   : サガワ マナミ
Gender      : F
Birthday    : 1994/07/01

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-10-03
### Jira Comments (19 則)
**Cy Lau** (2025-03-14):
@@Tovi Wang  Please help to get the log and version from this issue
**Tovi Wang** (2025-03-14):
@@Cy Lau @@Sang  FYI.
**Sang** (2025-03-14):
@@Tovi Wang Please get FE log include WA log
**Tovi Wang** (2025-03-14):
@@pierre.shi 帮忙拿下25-02-18 log，Thanks!
**pierre.shi** (2025-03-14):
@@Tovi Wang @@Sang logs have been uploaded as attachment.
**pierre.shi** (2025-03-14):
no wa log found
**Anson Cheung** (2025-03-17):
There are no records of member 1209510912 in the BEAPI logs. 
For C360 member, POS_API should handle the search. Please get the POS_API sqlite log.
@@Tovi Wang
**Tovi Wang** (2025-03-17):
@@Cy Lau @@Anson Cheung Neil 正在QA测试确认是否可以reproduce,正在等待Neil测试结果。
**Tovi Wang** (2025-03-17):
@@Cy Lau @@Anson Cheung @@Sang This issue can be reproduced in QA PC 172.24.253.69(C309).Follow log for your further checking.
**Anson Cheung** (2025-03-17):
@@Tovi Wang Please get the POS_API log from web server
**Tovi Wang** (2025-03-17):
@@Anson Cheung   please check.
**Tovi Wang** (2025-03-17):
@@Anson Cheung
从WA log来看，出生日期 1900 是C360 回过来的？right?还是从dbsse dbmas里面来的？
**Anson Cheung** (2025-03-17):
@@Tovi Wang C360 does returns the birth year, but this field does not map to the vipmas_birth_date field.
**Cy Lau** (2025-03-17):
It is nailed down as POS_API doesnt map the birthday, it will treat as null as year of DOB.
@@Anson Cheung  will provide the updates of the POS_API not later than 18 Mar 1230nn
@@Sherman tse prepare the testing case , we might need the help from tapestry
**Anson Cheung** (2025-03-18):
Release:
[\\ds411\public\samuel\POS_API\POS_API\v2.09.03_20250318](file://ds411/public/samuel/POS_API/POS_API/v2.09.03_20250318)
-
**Sherman tse** (2025-03-18):
The new release deployed into our QA enviroment, it can call C360 api, and return forbidden without other error. I will prepare test case first.
**Sherman tse** (2025-03-18):
I prepare a test case for testing the issue
**Tovi Wang** (2025-08-29):
Released to Coach team.Can be closed.
**Automation for Jira** (2025-10-03):
Issue has been created since
Days since: 203
Week since : 29
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1649](https://ctil.atlassian.net/browse/FE-1649)
- Fix Version: 未記錄
- 解決日期: 2025-10-03

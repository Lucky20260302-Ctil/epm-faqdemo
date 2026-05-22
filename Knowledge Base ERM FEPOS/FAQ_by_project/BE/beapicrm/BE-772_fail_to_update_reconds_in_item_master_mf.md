---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-772
resolved: 2023-07-27
fix-version: ""
---

# BE-772: Fail to update reconds in Item Master (MF0001)

## 問題

Reproduce steps:
1. 
2. 
3. 
4. 
Existing result:
Pop up an error: Fail to save record (Related screenshot as below)
Testing Env: [https://172.16.138.55/ChainStorePlus_LandsD_QA](https://172.16.138.55/ChainStorePlus_LandsD_QA)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-07-27
### Jira Comments (5 則)
**Hans Wong** (2023-06-21):
@@Jerry Wong and @@Sherman tse, let's align the understanding about LANDS item master Maintenance on Friday morning 2023-06-23.
The item page suppose view only, with only 1 field(
```java
itmpubl_gov_order_limit
```
) editable.
**Sherman tse** (2023-07-05):
Column: itmast_lock MUST fill with N/Y, else system would pop up mentioned above error
**Hans Wong** (2023-07-05):
@@Sherman tse dear sherman, which environment are you using?
**Hans Wong** (2023-07-10):
Dear @@Sherman tse, this problem should be fixed?
**Sherman tse** (2023-07-27):
Verified on LANDS UAT, close case
Only government order limit is editable

## 相關資訊

- Jira: [BE-772](https://ctil.atlassian.net/browse/BE-772)
- Fix Version: 未記錄
- 解決日期: 2023-07-27

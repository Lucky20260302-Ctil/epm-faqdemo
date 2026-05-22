---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Coach reports that the itmean import data interface process hang up. The root cause is the colsiz_se"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-841
resolved: 2024-05-24
fix-version: ""
---

# BE-841: Colsiz_seq fully occupied and causes ITMEAN interface hang up

## 問題

Coach reports that the itmean import data interface process hang up. The root cause is the colsiz_seq is fully occupied. The workaround is to delete unused color & size seq. and find space for the new color & size record create. Tapestry requests a long term solution now.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-24
### Jira Comments (3 則)
**Bobby** (2024-04-15):
I suggest adding a configuration setting 'max_colsiz_seq' in 'dbconfig' table to control max. value of colsiz_seq. Default is 99999. For Tapestry case, we should set to 9999999. Since Tapestry would not use ChainStorePlus barcode seq. It should not have any impact to Tapestry.
We should modify the programs that would create the colsiz record. They should be:
- 
- 
@Sang Ko, Any impact to the front end if the colsiz_seq > 99999?
**Sherman tse** (2024-05-06):
According to communicate with Bobby, max. value of colsiz_seq should set as 8 digits
I changed the following sql:
**Sherman tse** (2024-05-21):
Verified on QA, test case attached in the JIRA
No release, the issue is handled by SQL onyl

## 相關資訊

- Jira: [BE-841](https://ctil.atlassian.net/browse/BE-841)
- Fix Version: 未記錄
- 解決日期: 2024-05-24

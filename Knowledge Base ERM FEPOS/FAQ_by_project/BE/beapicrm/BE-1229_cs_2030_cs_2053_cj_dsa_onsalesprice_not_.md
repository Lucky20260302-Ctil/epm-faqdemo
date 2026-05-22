---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Temp Solution as Data patching with .BAT"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1229
resolved: 2026-02-26
fix-version: ""
---

# BE-1229: [CS-2030] -[CS-2053]  CJ DSA OnSalesPrice not effective owing to ZeroLength Temp solution

## 問題

Temp Solution as Data patching with .BAT
for case startDate = EndDate with 00:00:00.000

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-02-26
### Jira Comments (6 則)
**Cy Lau** (2026-02-05):
Scenario :
both the **effective-from** and **effective-to** datetimes are identical. Because of this, PriceChecker returns a result with **no OnSalePricing**.
- 
- 
- 
Although the *fromDateTime* is valid, it is immediately invalidated by the *toDateTime*.
The POS system currently handles cases where **fromDate = toDate** with a time of **00:00:00**, but **PriceChecker does not** handle this scenario.
Before the latest version of PriceCheckerJP delivery, 
**Avoid using 00:00:00 when fromDate = toDate**
Use **23:59:59** for the *toDateTime* instead (as in the existing test case), ensuring the full day is covered.
Yet, SAP dataset is not available for this changes, so schedule data patch on
**itmprx_onsale_to_date_1** & **onsale_to_date_2**
sqlcmd with bat is preferrable
**Cy Lau** (2026-02-05):
# Definintions :
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
---
# Deliverables :
Please help to place in DS411
---
# File structure:
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
Target to be executed:
|  |
| --- |
---
# Unit Test
Testing Env , CoachJPQA DB
Test case :
After the patch :
verify_pre log would log those spotted record :
patch log would indicates the patching result :
verify_post shall show no record after successfully patch:
---
Please arrange for QAQC before delivery to Tapestry 
@@Joy Li
Schedule with High priority as Production issue related to pricing
cc. @@Bobby  , @@Andrew_Au , @@Sherman tse
**Automation for Jira** (2026-02-05):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Andrew_Au** (2026-02-23):
@@Sherman tse  Please update the Jira ticket status
**Sherman tse** (2026-02-23):
Verified ok on QA with release:
\\ds411\public\daniel\pricechecker\20260223.1_JP_fullset
**Joy Li** (2026-02-26):
ken will release on 2026-02-27 with V70R3.145

## 相關資訊

- Jira: [BE-1229](https://ctil.atlassian.net/browse/BE-1229)
- Fix Version: 未記錄
- 解決日期: 2026-02-26

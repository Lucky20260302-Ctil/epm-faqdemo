---
tags: [faq, be, beapicrm]
component: "API"
symptom: "**Issue Summary:**"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: BE-1228
resolved: 
fix-version: ""
---

# BE-1228: CJ DSA displays Retail Price instead of correct On Sale Price before scheduled price changes (observed on 1/23 and 1/29)

## 問題

**Issue Summary:**
On 1/29, one day before a scheduled price change on 1/30, 
DSA (Price Checker) displayed the Retail Price instead of the correct On Sale Price for an outlet item.
The same issue was previously observed during a price update on 1/23.
**Expected Behavior:**
On 1/29, no price change was scheduled.
DSA should display the same On Sale Price as POS: ¥31,350.
**Actual Behavior:**
DSA displayed the Retail Price ¥104,500 instead of the On Sale Price.
At the same time, POS correctly displayed ¥31,350.
Item Details:
- 
- 
**Price Details:**
- 
- 
- 
- 
**Additional Information:**
An API response captured on 1/29 returned Retail Price (¥104,500)
with no On Sale Price information, which resulted in DSA displaying the Retail Price.
**Impact:**
Price inconsistency between POS and DSA at store opening on 1/29,
causing incorrect price display in the outlet store.
**Business Context (for reference):**
Starting from 1/23, a pricing initiative called "Shallow Discount" was introduced.
In this initiative:
- 
- 
- 
- 
Target items are being migrated to this initiative in phases (#1–#4).
This issue was first observed during the 1/23 price update
and occurred again on 1/29 before another scheduled price change.
**Attachments:**
- 
- 
- 
-

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Cy Lau** (2026-01-30):
**Please review our initial investigation on the case dated 29/1:**
In the PriceChecker logic, the system validates *OnSalePricing* in addition to the item details and location details. A key factor in this validation is the **effective time period**.
From our data inspection, both the **effective-from** and **effective-to** datetimes are identical. Because of this, PriceChecker returns a result with **no OnSalePricing**.
- 
- 
- 
Although the *fromDateTime* is valid, it is immediately invalidated by the *toDateTime*.
The POS system currently handles cases where **fromDate = toDate** with a time of **00:00:00**, but **PriceChecker does not** handle this scenario.
---
# **Suggested Next Steps**
1. 
1.
**Cy Lau** (2026-01-30):
Hi team ,
With concern for those OnSalePricing effective since 2026-01-30 :
there are **no records** in the Coach Japan database `csdata18_70` where **FromDateTime = ToDateTime** for OnSalePricing:
Based on this, the **zero‑length effective period issue should not be triggered** for any records effective from **2026‑01‑30 onward**.
**Automation for Jira** (2026-01-30):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Cy Lau** (2026-01-30):
```
public const string ApiGateway = "1.0.1";
public const string BuildDate = "20260130";
public const string BuildNum = "1";
```
@@Daniel Leung  Please follow up for checking later and build for QAQC
**Daniel Leung** (2026-01-30):
release package uploaded to  \\ds411\public\daniel\pricechecker\20260130.1_JP_fullset
@@Sherman tse @@Joy Li
**Daniel Leung** (2026-02-20):
a bug found by @@Sherman tse
bug fix version uploaded to: \\ds411\public\daniel\pricechecker\20260220.1_JP_fullset
@@Sherman tse  Please test
**Sherman tse** (2026-02-23):
Verified ok on QA with release:
\\ds411\public\daniel\pricechecker\20260223.1_JP_fullset

## 相關資訊

- Jira: [BE-1228](https://ctil.atlassian.net/browse/BE-1228)
- Fix Version: 未記錄
- 解決日期: 未記錄

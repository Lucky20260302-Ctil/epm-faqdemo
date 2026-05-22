---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Issue (CS-2030): on-sale effectiveness checking not align with FEPOS."
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: BE-1261
resolved: 
fix-version: ""
---

# BE-1261: Price Checker API - New Configuration to handle on-sales validation in Full Date mode

## 問題

Issue (CS-2030): on-sale effectiveness checking not align with FEPOS.
We have identified that the issue is caused by the on-sale price data having an end date of **“2026-04-30 00:00:000”**. The expected end timestamp should be **“2026-04-30 23:59:000”**, which is consistent with the alignment previously agreed during the earlier incident where on-sale prices were not reflected when the start and end dates fell on the same day.
**Proposed Change Details**
**AS-IS:**
The Price Checker API validates the on-sale price based on the effective **date-time** range.
For example, if an item’s on-sale price has:
- 
- 
The API will treat the effective period as **1 Jan to 30 Jan**, meaning **31 Jan** will not be included.
**TO-BE:**
A new API configuration (OnSaleFullDateMode) will be introduced to control validation in **Full Date** mode.
- 
-

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Daniel Leung** (2026-05-06):
released to 
pricechecker: \\ds411\public\daniel\pricechecker\20260506.1_JP_fullset
OMNI: \\ds411\public\daniel\pricechecker\20260506.1_OMNI_fullset 
 @@Sherman tse @@Cy Lau @@Joy Li @@Ken Wang 
added new config in appsetting.json -  AppConfiguration:OnSaleFullDateMode
**Automation for Jira** (2026-05-06):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [BE-1261](https://ctil.atlassian.net/browse/BE-1261)
- Fix Version: 未記錄
- 解決日期: 未記錄

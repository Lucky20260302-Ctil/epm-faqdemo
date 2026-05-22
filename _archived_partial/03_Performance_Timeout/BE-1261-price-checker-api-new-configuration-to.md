---
project: BE
issue_key: BE-1261
issue_type: Bug PRD
status: Test in Progress
tags:
- 03_performance_timeout
- api
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1261
created: '2026-05-04'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1261: Price Checker API - New Configuration to handle on-sales validation in Full Date mode'
---
# BE-1261: Price Checker API - New Configuration to handle on-sales validation in Full Date mode

## 問題描述

Issue (CS-2030): on-sale effectiveness checking not align with FEPOS.

We have identified that the issue is caused by the on-sale price data having an end date of **“2026-04-30 00:00:000”**. The expected end timestamp should be **“2026-04-30 23:59:000”**, which is consistent with the alignment previously agreed during the earlier incident where on-sale prices were not reflected when the start and end dates fell on the same day.

 

 

**Proposed Change Details**

 

**AS-IS:**
The Price Checker API validates the on-sale price based on the effective **date-time** range.
For example, if an item’s on-sale price has:

- Start date: *2026-01-01 00:00:00*

- End date: *2026-01-31 00:00:00*

The API will treat the effective period as **1 Jan to 30 Jan**, meaning **31 Jan** will not be included.

 

**TO-BE:**
A new API configuration (OnSaleFullDateMode) will be introduced to control validation in **Full Date** mode.

- When the configuration is **ON**, the API will validate only the effective **date** (ignoring time). In this case, an end date of *2026-01-31 00:00:00* will still be considered effective for **31 Jan**.

- When the configuration is **OFF**, the API will continue to validate the full **date-time** range, maintaining the current behaviour.



## 相關資訊

- **Jira:** [BE-1261](https://ctil.atlassian.net/browse/BE-1261)
- **標籤:** PriceCheck
---
project: BE
title: "BE-1228: CJ DSA displays Retail Price instead of correct On Sale Price before scheduled price changes (observed on 1/23 and 1/29)"
issue_key: BE-1228
issue_type: Bug PRD
status: Release
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1228"
created: 2026-01-30
resolved: 
resolution: 
has_images: True
---

# BE-1228: CJ DSA displays Retail Price instead of correct On Sale Price before scheduled price changes (observed on 1/23 and 1/29)

## 問題描述

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

- Item Name: GRAHAM TOTE IN SIGNATURE CANVAS

- Style Number: CCQ55

**Price Details:**

- Correct On Sale Price on 1/29 (POS): ¥31,350

- Retail Price displayed on DSA on 1/29: ¥104,500

- Scheduled price change date: 1/30

- Retail Price after price change (1/30): ¥64,900

**Additional Information:**
An API response captured on 1/29 returned Retail Price (¥104,500)
with no On Sale Price information, which resulted in DSA displaying the Retail Price.

**Impact:**
Price inconsistency between POS and DSA at store opening on 1/29,
causing incorrect price display in the outlet store.

**Business Context (for reference):**
Starting from 1/23, a pricing initiative called "Shallow Discount" was introduced.

In this initiative:

- Selling price and AUR remain unchanged

- J1 Price is reduced

- Base discount depth becomes shallower

- Discount rate presented to customers is reduced

Target items are being migrated to this initiative in phases (#1–#4).
This issue was first observed during the 1/23 price update
and occurred again on 1/29 before another scheduled price change.

**Attachments:**

- POS_20250129_OnSalePrice_31350.jpg (POS showing correct On Sale Price)

- DSA_20250129_RetailPriceDisplayed_104500.jpg (DSA showing Retail Price on 1/29)

- API_20250129_RetailPriceResponse_104500.jpg (API response captured on 1/29)

- 
> 📎 **image-20260130-073700.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5d74dc15-ce7f-496e-9189-e678b4c00826)（需 Jira 登入）

> 📎 **image-20260130-073709.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d834fb5f-3a39-4711-bb26-a48332b2376f)（需 Jira 登入）

> 📎 **image-20260130-073718.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fd541121-4e40-402b-84e2-1dbd27899866)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260130-073700.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5d74dc15-ce7f-496e-9189-e678b4c00826)
2. 📎 **image-20260130-073709.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d834fb5f-3a39-4711-bb26-a48332b2376f)
3. 📎 **image-20260130-073718.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fd541121-4e40-402b-84e2-1dbd27899866)

## 相關資訊

- **Jira:** [BE-1228](https://ctil.atlassian.net/browse/BE-1228)
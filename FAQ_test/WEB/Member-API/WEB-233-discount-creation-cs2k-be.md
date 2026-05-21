---
tags: [faq, WEB, bug]
component: "Backend API"
symptom: "After creating a discount in CS2K BE, attempting to update the discount fails — changes are not saved"
root-cause: "The discount update API was not correctly identifying existing discount records for modification, treating them as new creations instead."
solution: "Fixed discount update logic to correctly identify and modify existing records."
jira: WEB-233
resolved: 2022-06-28
fix-version: ""
---

# WEB-233: Discount Creation Cannot Be Updated in CS2K Backend

## 問題

After creating a discount in CS2K BE, attempting to update the discount fails — changes are not saved

## 根因

The discount update API was not correctly identifying existing discount records for modification, treating them as new creations instead.

## 解法

Fixed discount update logic to correctly identify and modify existing records.

## 相關資訊

- Jira: [WEB-233](https://ctil.atlassian.net/browse/WEB-233)
- Fix Version: 未記錄
- 解決日期: 2022-06-28

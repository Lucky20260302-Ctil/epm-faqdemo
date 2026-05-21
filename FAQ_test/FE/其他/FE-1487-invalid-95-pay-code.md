---
tags: [faq, FE, bug]
component: "Cash Flow"
symptom: "Invalid pay code '95' is being uploaded to Backend in cash flow data, causing downstream processing errors"
root-cause: "The frontend was not validating pay codes before uploading to BE. Code '95' is not defined in the pay code table but was passed through unchecked."
solution: "Added pay code validation function to filter out undefined pay codes before upload. Invalid codes are now logged and skipped. Fix in v750.04R04I."
jira: FE-1487
resolved: 2024-08-30
fix-version: "v750.04R04I"
---

# FE-1487: Invalid '95' Pay Code Uploaded to BE — Missing Validation

## 問題

Invalid pay code '95' is being uploaded to Backend in cash flow data, causing downstream processing errors

## 根因

The frontend was not validating pay codes before uploading to BE. Code '95' is not defined in the pay code table but was passed through unchecked.

## 解法

Added pay code validation function to filter out undefined pay codes before upload. Invalid codes are now logged and skipped. Fix in v750.04R04I.

## 相關資訊

- Jira: [FE-1487](https://ctil.atlassian.net/browse/FE-1487)
- Fix Version: v750.04R04I
- 解決日期: 2024-08-30

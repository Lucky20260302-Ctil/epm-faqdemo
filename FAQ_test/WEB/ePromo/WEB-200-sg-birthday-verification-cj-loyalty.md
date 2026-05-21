---
tags: [faq, WEB, bug]
component: "Member API"
symptom: "Singapore region: birthday verification returns error for members, and CJ Loyalty needs to be disabled for certain stores"
root-cause: "Birthday verification logic had a region-specific date format mismatch. CJ Loyalty flag was not being properly disabled per store configuration."
solution: "Fixed birthday verification to use correct date format for SG region. Added store-level CJ Loyalty disable toggle."
jira: WEB-200
resolved: 2021-07-12
fix-version: ""
---

# WEB-200: SG Birthday Verification Error + Disable CJ Loyalty Fix

## 問題

Singapore region: birthday verification returns error for members, and CJ Loyalty needs to be disabled for certain stores

## 根因

Birthday verification logic had a region-specific date format mismatch. CJ Loyalty flag was not being properly disabled per store configuration.

## 解法

Fixed birthday verification to use correct date format for SG region. Added store-level CJ Loyalty disable toggle.

## 相關資訊

- Jira: [WEB-200](https://ctil.atlassian.net/browse/WEB-200)
- Fix Version: 未記錄
- 解決日期: 2021-07-12

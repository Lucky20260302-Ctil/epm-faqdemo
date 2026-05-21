---
tags: [faq, WEB, bug]
component: "eName"
symptom: "eName registration: cannot move to next page when gender info is not input on the registration page"
root-cause: "The registration form validation requires gender field but does not provide clear error message when skipped, leaving user stuck on the page."
solution: "Added form validation error display for gender field. User now sees a clear message prompting to fill the required field. See CS-1241."
jira: WEB-369
resolved: 2025-01-03
fix-version: ""
---

# WEB-369: eName: Cannot Proceed Registration Without Gender Input

## 問題

eName registration: cannot move to next page when gender info is not input on the registration page

## 根因

The registration form validation requires gender field but does not provide clear error message when skipped, leaving user stuck on the page.

## 解法

Added form validation error display for gender field. User now sees a clear message prompting to fill the required field. See CS-1241.

## 相關資訊

- Jira: [WEB-369](https://ctil.atlassian.net/browse/WEB-369)
- Fix Version: 未記錄
- 解決日期: 2025-01-03

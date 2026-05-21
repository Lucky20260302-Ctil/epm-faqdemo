---
tags: [faq, MP, bug]
component: "MPOS"
symptom: "When users input Japanese characters during MPOS login, login fails AND the failed login records cause posting errors downstream"
root-cause: "Japanese characters in login input were not sanitized/blocked, causing encoding issues in posting records. The multi-byte characters corrupted posting data."
solution: "Short-term: instruct users not to input Japanese characters at login. Long-term fix: block Japanese/multi-byte characters at login input. Fixed in 3.28.2_IPA."
jira: MP-702
resolved: 2024-06-07
fix-version: "3.28.2_IPA"
---

# MP-702: Japanese Characters in MPOS Login Cause Posting Errors

## 問題

When users input Japanese characters during MPOS login, login fails AND the failed login records cause posting errors downstream

## 根因

Japanese characters in login input were not sanitized/blocked, causing encoding issues in posting records. The multi-byte characters corrupted posting data.

## 解法

Short-term: instruct users not to input Japanese characters at login. Long-term fix: block Japanese/multi-byte characters at login input. Fixed in 3.28.2_IPA.

## 相關資訊

- Jira: [MP-702](https://ctil.atlassian.net/browse/MP-702)
- Fix Version: 3.28.2_IPA
- 解決日期: 2024-06-07

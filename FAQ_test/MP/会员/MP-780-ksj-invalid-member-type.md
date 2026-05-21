---
tags: [faq, MP, bug]
component: "MPOS"
symptom: "KSJ MPOS: employee/VIP member can be selected but when proceeding to payment, 'invalid member type' error appears"
root-cause: "Flutter IPA code issue with member type handling in the payment flow for KSJ brand. The member type validation was incorrectly rejecting valid employee/VIP types."
solution: "Hotfix IPA 3.29.6-20250612.1 deployed. See also MPOS-101."
jira: MP-780
resolved: 2025-07-04
fix-version: "3.29.6-20250612.1"
---

# MP-780: KSJ MPOS v3.29.5f: Invalid Member Type Error During Payment

## 問題

KSJ MPOS: employee/VIP member can be selected but when proceeding to payment, 'invalid member type' error appears

## 根因

Flutter IPA code issue with member type handling in the payment flow for KSJ brand. The member type validation was incorrectly rejecting valid employee/VIP types.

## 解法

Hotfix IPA 3.29.6-20250612.1 deployed. See also MPOS-101.

## 相關資訊

- Jira: [MP-780](https://ctil.atlassian.net/browse/MP-780)
- Fix Version: 3.29.6-20250612.1
- 解決日期: 2025-07-04

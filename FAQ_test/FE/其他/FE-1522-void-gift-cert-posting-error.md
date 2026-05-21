---
tags: [faq, FE, bug]
component: "PCD Posting"
symptom: "V75 voiding a gift certificate transaction causes posting error: database null value in PCD record type 32"
root-cause: "The void gift cert flow does not properly populate all required fields for the PCD 32 record, leaving null values that cause the posting validation to fail."
solution: "Ensure all required PCD 32 fields are populated during gift cert void flow. Fix in V75 release."
jira: FE-1522
resolved: 2024-10-18
fix-version: "V75"
---

# FE-1522: Void Gift Certificate Causes DB Null Posting Error (PCD 32)

## 問題

V75 voiding a gift certificate transaction causes posting error: database null value in PCD record type 32

## 根因

The void gift cert flow does not properly populate all required fields for the PCD 32 record, leaving null values that cause the posting validation to fail.

## 解法

Ensure all required PCD 32 fields are populated during gift cert void flow. Fix in V75 release.

## 相關資訊

- Jira: [FE-1522](https://ctil.atlassian.net/browse/FE-1522)
- Fix Version: V75
- 解決日期: 2024-10-18

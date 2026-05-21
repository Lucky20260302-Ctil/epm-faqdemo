---
tags: [faq, MP, bug]
component: "MPOS"
symptom: "In Queue Busting flow, member information is cleared out after performing an update operation on MPOS"
root-cause: "Data retention issue in Queue Busting feature — member info was not being persisted after partial transaction updates in the MPOS state management."
solution: "Fixed member info persistence during Queue Busting partial updates. Member data now survives update operations."
jira: MP-733
resolved: 2025-02-24
fix-version: ""
---

# MP-733: Queue Busting: Member Info Cleared After Update on MPOS

## 問題

In Queue Busting flow, member information is cleared out after performing an update operation on MPOS

## 根因

Data retention issue in Queue Busting feature — member info was not being persisted after partial transaction updates in the MPOS state management.

## 解法

Fixed member info persistence during Queue Busting partial updates. Member data now survives update operations.

## 相關資訊

- Jira: [MP-733](https://ctil.atlassian.net/browse/MP-733)
- Fix Version: 未記錄
- 解決日期: 2025-02-24

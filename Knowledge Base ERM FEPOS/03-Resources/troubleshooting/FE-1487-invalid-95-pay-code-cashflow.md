---
tags: [bug, production]
component: Front End
symptom: "Invalid '95' pay code records uploaded from POS to Backend causing data inconsistency"
root-cause: "Invalid cash flow records with pay code '95' exist in tblcashFlow table and are being uploaded to BE"
solution: "Added a validation function to remove invalid cash flow records from tblcashFlow before upload"
jira: FE-1487
resolved: 2024-08-30
---

# FE-1487: Invalid '95' Pay Code Uploaded to Backend

## 問題

Invalid pay code '95' records are being uploaded from the Front End to the Backend system through `tblcashFlow`. This causes data inconsistency in the backend reporting and payment reconciliation.

## 根因

The `tblcashFlow` table contains cash flow records with pay code '95' which is not a valid/recognized pay code. These invalid records are being included in the upload process without validation, polluting the backend data.

## 解法

Added a function to **remove invalid cash flow records** from `tblcashFlow` before the upload to BE occurs. This acts as a data validation/cleanup step in the upload pipeline.

**Fix Version**: `v750.04R04I`

## 相關問題

- [[FE-???|Pay code management]]

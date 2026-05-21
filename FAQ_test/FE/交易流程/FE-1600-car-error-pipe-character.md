---
tags: [faq, FE, bug]
component: "Interface"
symptom: "CAR file generation fails with 'Unknown Sales item type code 9999' when remarks field contains pipe character (|)"
root-cause: "The CAR file format uses pipe (|) as field delimiter. When the remarks field contains a pipe character, it breaks the column structure of the pipe-delimited file, causing downstream systems to read incorrect field values."
solution: "Sanitize remarks field to remove or escape pipe characters before writing to CAR file. Fix in 2024-01-02 CAR Release."
jira: FE-1600
resolved: 2025-02-12
fix-version: "2024-01-02 CAR Release"
---

# FE-1600: CAR Error: Pipe Character (|) in Remarks Field Corrupts CAR File

## 問題

CAR file generation fails with 'Unknown Sales item type code 9999' when remarks field contains pipe character (|)

## 根因

The CAR file format uses pipe (|) as field delimiter. When the remarks field contains a pipe character, it breaks the column structure of the pipe-delimited file, causing downstream systems to read incorrect field values.

## 解法

Sanitize remarks field to remove or escape pipe characters before writing to CAR file. Fix in 2024-01-02 CAR Release.

## 相關資訊

- Jira: [FE-1600](https://ctil.atlassian.net/browse/FE-1600)
- Fix Version: 2024-01-02 CAR Release
- 解決日期: 2025-02-12

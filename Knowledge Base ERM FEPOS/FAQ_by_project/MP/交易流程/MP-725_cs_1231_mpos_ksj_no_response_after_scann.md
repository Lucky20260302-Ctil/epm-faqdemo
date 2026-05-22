---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Member Lookup page cannot read any barcode info from SFCC via mPOS."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-725
resolved: 2025-03-06
fix-version: ""
---

# MP-725: [CS-1231] mPOS | KSJ | No Response after Scanning Member ID Barcodes (through Member Lookup) directly using the iPhone Camera

## 問題

Member Lookup page cannot read any barcode info from SFCC via mPOS.
There is no problem with scanning from scanner with LPOS scranner.
---
Barcode is Code 39 format

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-06
### Jira Comments (5 則)
**Cy Lau** (2024-12-27):
From TP :
The codabar starting and ending byte are “A“
@@Daniel Leung  Please help to estimate the development effort
**Cy Lau** (2024-12-27):
Re-Open for Dev
**Cy Lau** (2025-01-03):
@@Daniel Leung  Please start the Dev not later than 06 Jan
The Dev ETA would be 08 Jan
**Daniel Leung** (2025-01-06):
new release - 3.29.5-20250106.2 uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)
**Sherman tse** (2025-01-21):
Verified on QA
Version : 3.23.2-20250120.1

## 相關資訊

- Jira: [MP-725](https://ctil.atlassian.net/browse/MP-725)
- Fix Version: 未記錄
- 解決日期: 2025-03-06

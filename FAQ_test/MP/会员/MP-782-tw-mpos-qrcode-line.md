---
tags: [faq, MP, bug, production]
component: "MPOS"
symptom: "Scanning member QR code from LINE app on TW MPOS shows 'Invalid QR Code' error. API returns HTTP 500."
root-cause: "MPOS 3.29 added dynamic token validation for Member QR Code, but the backend validation lacked backward compatibility for non-ACIXOM member types. The MPOS API was rejecting valid LINE QR codes."
solution: "Added restriction so dynamic token validation only occurs when OnlineMemberType == ACIXOM. Fix in MPOS API 3.29.6."
jira: MP-782
resolved: 2025-07-09
fix-version: "3.29.6"
---

# MP-782: TW MPOS: Cannot Add Member via QR Code Scan from LINE App

## 問題

Scanning member QR code from LINE app on TW MPOS shows 'Invalid QR Code' error. API returns HTTP 500.

## 根因

MPOS 3.29 added dynamic token validation for Member QR Code, but the backend validation lacked backward compatibility for non-ACIXOM member types. The MPOS API was rejecting valid LINE QR codes.

## 解法

Added restriction so dynamic token validation only occurs when OnlineMemberType == ACIXOM. Fix in MPOS API 3.29.6.

## 相關資訊

- Jira: [MP-782](https://ctil.atlassian.net/browse/MP-782)
- Fix Version: 3.29.6
- 解決日期: 2025-07-09

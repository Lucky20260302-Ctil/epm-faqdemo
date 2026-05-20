---
tags: [bug, production, hotfix]
component: MPOS API
symptom: "Citizen printer only prints one receipt from MPOS — iPhone cannot print receipt (RIN00884283)"
root-cause: "Citizen printer driver/API compatibility issue with MPOS cloud/local IIS API causing single-receipt print limit"
solution: "Fix printing API in version 3.14.1 to support multiple receipt printing from Citizen printer via MPOS"
jira: MP-521
resolved: 2022-04-29
---

# MP-521: Citizen Printer Only Prints One Receipt from MPOS

## 問題

Citizen printer connected to MPOS only prints one receipt. When multiple print jobs are sent, only the first one is processed. iPhone users reported they could not print receipts from MPOS at all.

**Callout reference**: `RIN00884283`

## 根因

The Citizen printer integration in MPOS API (`Cloud & Local IIS API & IPA version`) has a printing limitation where only the first print job is accepted. Subsequent print jobs are silently dropped. This is a driver-level or API-level compatibility issue affecting both cloud and local IIS deployments.

The exact root cause is in the print job handling — the API does not properly initialize/reset the printer connection between print jobs.

## 解法

Fix applied in **version 3.14.1** to correct the printing flow for Citizen printers, enabling multiple receipt printing from MPOS.

**Fix Versions**: `3.14.1_API_local`, `3.14.1_API`

## 相關問題

- [[MP-313]] — Related MPOS printing issue (local printing error)

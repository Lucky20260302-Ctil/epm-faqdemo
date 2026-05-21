---
tags: [faq, BE, bug]
component: "BEAPI / CRM"
symptom: "API returns member type 'P' but CS2000 should convert 'P' to 'C'. The conversion did not happen, causing incorrect member type in FEPOS."
root-cause: "The async insertion workflow in BEAPI bypassed the P-to-C conversion logic, passing data directly to FEPOS without conversion."
solution: "Fixed in BEAPI v1.7.18 (Acxiom CRM integration) — the background async service now correctly converts 'P' to 'C' during upsert."
jira: BE-1059
resolved: 2025-04-10
fix-version: "BEAPI v1.7.18"
---

# BE-1059: Member Type "P" Not Converted to "C" During Async Upsert

## 問題

API returns member type "P" but CS2000 should convert "P" to "C". The conversion did not happen, causing incorrect member type in FEPOS.

## 根因

The async insertion workflow in BEAPI bypassed the P-to-C conversion logic, passing data directly to FEPOS without conversion.

## 解法

Fixed in BEAPI v1.7.18 (Acxiom CRM integration) — the background async service now correctly converts "P" to "C" during upsert.

## 相關資訊

- Jira: [BE-1059](https://ctil.atlassian.net/browse/BE-1059)
- Fix Version: BEAPI v1.7.18
- 解決日期: 2025-04-10

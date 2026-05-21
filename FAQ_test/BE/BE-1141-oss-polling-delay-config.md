---
tags: [faq, BE, bug, config, performance]
component: "Polling / OSS"
symptom: "OSS polling experiencing significant delays; stores cannot poll in a timely manner due to multiple contributing factors"
root-cause: "Multiple issues: (1) 4.18 stx files present in OSS folder causing processing overhead, (2) OSS token only 1-hour effective window, (3) too many stores configured in OSS_B, (4) Zlog job blocking the POSTAB table."
solution: "Added configuration settings in OSSPolling.exe.config: IGNORE_STX, ENABLE_RESEND, and IGNORE_ACP to control polling behavior and bypass problematic processing steps."
jira: BE-1141
resolved: 2025-05-21
fix-version: ""
---

# BE-1141: PRC OSS Polling Delay — Stores Cannot Poll in Timely Manner

## 問題

OSS polling experiencing significant delays; stores cannot poll in a timely manner due to multiple contributing factors

## 根因

Multiple issues: (1) 4.18 stx files present in OSS folder causing processing overhead, (2) OSS token only 1-hour effective window, (3) too many stores configured in OSS_B, (4) Zlog job blocking the POSTAB table.

## 解法

Added configuration settings in OSSPolling.exe.config: IGNORE_STX, ENABLE_RESEND, and IGNORE_ACP to control polling behavior and bypass problematic processing steps.

## 相關資訊

- Jira: [BE-1141](https://ctil.atlassian.net/browse/BE-1141)
- Fix Version: 未記錄
- 解決日期: 2025-05-21

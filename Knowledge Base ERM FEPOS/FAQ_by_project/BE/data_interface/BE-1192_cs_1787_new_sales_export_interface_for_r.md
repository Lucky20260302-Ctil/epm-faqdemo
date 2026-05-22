---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "New Request from Lein that new Sales Interface is required to export Dayend Sales or Hourly Sales (f"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: BE-1192
resolved: 
fix-version: ""
---

# BE-1192: [CS-1787] New Sales Export Interface for Resorts World Sentosa

## 問題

New Request from Lein that new Sales Interface is required to export Dayend Sales or Hourly Sales (fallback in dayend data not available) to Tangent System (teant sales management system of Sentosa.)
Please note that <u>**RWS requires two API integration formats to be implemented concurrently**</u>, each serving a specific purpose:
1. 
2. 
This dual integration approach ensures data accuracy while maintaining operational reliability in the event of incomplete daily closures.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Ken Wang** (2025-10-24):
Attahced 2 API spec from Tengent. And SOW will be provided to @@Bobby  for review shortly.
**Andrew_Au** (2026-04-16):
@@Bobby **Can we update the ticket status to 'Closed'?**

## 相關資訊

- Jira: [BE-1192](https://ctil.atlassian.net/browse/BE-1192)
- Fix Version: 未記錄
- 解決日期: 未記錄

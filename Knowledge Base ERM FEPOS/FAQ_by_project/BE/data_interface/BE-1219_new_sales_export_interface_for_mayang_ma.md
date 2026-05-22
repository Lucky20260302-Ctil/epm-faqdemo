---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "New Request from Lein that new Sales Interface is required to export Hourly Sales to Tangent System "
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: BE-1219
resolved: 
fix-version: ""
---

# BE-1219: New Sales Export Interface for Mayang Mall 

## 問題

New Request from Lein that new Sales Interface is required to export Hourly Sales to Tangent System (tenant sales management system of Mayang.)
The API integration will be implemented for below purpose:
1.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Ken Wang** (2025-12-03):
Attached is the API Documentation POS Sales Hourly to submit and integrate via Web API.
Please send hourly sales via API to the test URL
Here is the Staging phase url :
User ID:      postestapimy
Password:  @APITest1234
Machine ID:  50100902
URL GET TOKEN:
[https://staging.synthesis.bz/posmy/v1/api/token](https://staging.synthesis.bz/posmy/v1/api/token)
URL POST Sales Data:
[https://staging.synthesis.bz/posmy/v1/api/SalesHourly](https://staging.synthesis.bz/posmy/v1/api/SalesHourly)
**Ken Wang** (2025-12-03):
Attached the specification from Landlord and SOW for review.
**Sherman tse** (2026-01-08):
@@Ken Wang  Can we close this ticket?
**Andrew_Au** (2026-04-16):
@@Bobby **Can we update the ticket status to 'Closed'?**

## 相關資訊

- Jira: [BE-1219](https://ctil.atlassian.net/browse/BE-1219)
- Fix Version: 未記錄
- 解決日期: 未記錄

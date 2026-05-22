---
project: BE
issue_key: BE-1219
issue_type: SOW
status: Open
tags:
- 04_data_sync
- be
- data-interface
- data_sync
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1219
created: '2025-12-03'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1219: New Sales Export Interface for Mayang Mall'
---
# BE-1219: New Sales Export Interface for Mayang Mall 

## 問題描述

New Request from Lein that new Sales Interface is required to export Hourly Sales to Tangent System (tenant sales management system of Mayang.)

The API integration will be implemented for below purpose:

 

1. Sales Hourly API 

1. retrieve the hourly sales data (24 hourly entries) and export to Tangent once per day.

2. need to export sales data for the past 7 days.

 




## Jira Comments

> **Ken Wang** (2025-12-03):
> Attached is the API Documentation POS Sales Hourly to submit and integrate via Web API. Please send hourly sales via API to the test URL  Here is the Staging phase url :    User ID:      postestapimy Password:  @APITest1234 Machine ID:  50100902   URL GET TOKEN: https://staging.synthesis.bz/posmy/v1/api/token   URL POST Sales Data:  https://staging.synthesis.bz/posmy/v1/api/SalesHourly

> **Ken Wang** (2025-12-03):
> Attached the specification from Landlord and SOW for review.

> **Sherman tse** (2026-01-08):
>   Can we close this ticket?

> **Andrew_Au** (2026-04-16):
>   Can we update the ticket status to 'Closed'?

## 相關資訊

- **Jira:** [BE-1219](https://ctil.atlassian.net/browse/BE-1219)
- **標籤:** LL_Sales_Interface
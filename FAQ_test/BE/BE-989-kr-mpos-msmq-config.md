---
tags: [faq, BE, bug]
component: "MPOS / Polling"
symptom: "KR MPOS sales from stores failing to upload to database; no MPOS memo found in sqlpcda table"
root-cause: "MSMQ Single Transaction configuration was not properly enabled for KR region (MSMQ_SingleTX config and queue enablement were missing)."
solution: "Enable MSMQ_SingleTX config for the KR region in the backend system settings."
jira: BE-989
resolved: 2024-08-30
fix-version: ""
---

# BE-989: KR MPOS Transactions Cannot Send to DB — MSMQ Configuration Missing

## 問題

KR MPOS sales from stores failing to upload to database; no MPOS memo found in sqlpcda table

## 根因

MSMQ Single Transaction configuration was not properly enabled for KR region (MSMQ_SingleTX config and queue enablement were missing).

## 解法

Enable MSMQ_SingleTX config for the KR region in the backend system settings.

## 相關資訊

- Jira: [BE-989](https://ctil.atlassian.net/browse/BE-989)
- Fix Version: 未記錄
- 解決日期: 2024-08-30

---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "ChainStorePlus APP Server"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-908
resolved: 2024-09-23
fix-version: ""
---

# BE-908: [CRM ACXIOM ] void status update + reconsolation Null

## 問題

ChainStorePlus APP Server
l   CN Near Real Time CRM API
Ø   Change selection logic for sales and sales reconsolidation.
u  Re-send voided memo with changed void status to CRM when memo is voided. crmlog table will mark the first send time only. The voided memo with send with void memo.
u  Sales reconsolidation: show 0 instead null if memo amount = 0

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-23

## 相關資訊

- Jira: [BE-908](https://ctil.atlassian.net/browse/BE-908)
- Fix Version: 未記錄
- 解決日期: 2024-09-23

---
project: BE
issue_key: BE-908
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- be
- data-interface
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-908
created: '2024-09-23'
resolved: '2024-09-23'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-908: [CRM ACXIOM ] void status update + reconsolation Null'
---
# BE-908: [CRM ACXIOM ] void status update + reconsolation Null

## 問題描述

ChainStorePlus APP Server

l   CN Near Real Time CRM API

Ø   Change selection logic for sales and sales reconsolidation.

u  Re-send voided memo with changed void status to CRM when memo is voided. crmlog table will mark the first send time only. The voided memo with send with void memo.

u  Sales reconsolidation: show 0 instead null if memo amount = 0



## 相關資訊

- **Jira:** [BE-908](https://ctil.atlassian.net/browse/BE-908)
- **解決方式:** Done
---
project: BE
title: "BE-908: [CRM ACXIOM ] void status update + reconsolation Null"
issue_key: BE-908
issue_type: Bug PRD
status: Closed
faq_score: 8.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-908"
created: 2024-09-23
resolved: 2024-09-23
resolution: Done
has_images: False
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
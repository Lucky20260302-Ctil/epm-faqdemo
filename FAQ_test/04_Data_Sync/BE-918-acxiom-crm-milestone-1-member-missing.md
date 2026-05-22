---
project: BE
title: "BE-918: [ACXIOM CRM] Milestone 1 - Member Missing"
issue_key: BE-918
issue_type: Change Request
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-918"
created: 2024-10-16
resolved: 2024-10-16
resolution: Done
has_images: False
---

# BE-918: [ACXIOM CRM] Milestone 1 - Member Missing

## 問題描述

1. CN New Real Time CRM API

l   Missing Member issue

Ø   In original design, program will get the outstanding sales and vip information by two SQL. (Program will get the member information then sales data). But we found that there are gap after program select vip and sales. The new posted sales just after member selection will miss member information.

Ø   Program enhance to get the sales data then VIP information to avoid the time gap.



## 相關資訊

- **Jira:** [BE-918](https://ctil.atlassian.net/browse/BE-918)
- **解決方式:** Done
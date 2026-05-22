---
project: FE
issue_key: FE-1541
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1541"
created: 2024-10-24
resolved: 2024-10-28
resolution: Done
has_images: False
---

# FE-1541: [Coach][CRM milestone 2] Pop up 'Member not found' when local DB & backend DB has that member but doesn't exist in CRM side

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.5
> **解決日期:** 2024-10-28
> **負責人:** Sang
> **組件:** Front End

## 問題描述

[Coach][CRM milestone 2] Pop up 'Member not found' when backend DB has that member but doesn't exist in CRM side

**Situation: POS connect with CRM api successfully**

Reproduce steps:

1. To member section

2. Search member ID that backend DB has that member but doesn't exist in CRM side

Expected result:

Pop up ‘Member not found'  & won’t display member details from backend DB

*All member information need to based on CRM side when POS connect with CRM api successfully




## Jira Comments

> **Sang** (2024-10-25):
> 

> **Sherman tse** (2024-10-28):
> Keep existing settings Close case

## 相關資訊

- **Jira:** [FE-1541](https://ctil.atlassian.net/browse/FE-1541)
- **解決方式:** Done
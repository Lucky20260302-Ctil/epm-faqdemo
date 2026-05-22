---
project: FE
issue_key: FE-1832
issue_type: Task
status: Selected for Development (migrated)
tags:
- 07_workflow_business
- faq
- fe
- printing
- workflow_business
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1832
created: '2025-12-15'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1832: PPR-62 <FE Configuration> Customer Information in Receipt'
---
# FE-1832: PPR-62 <FE Configuration> Customer Information in Receipt

## 問題描述

As aligned with COACH  last week, the following customer information will be printed on all sales receipts (including all sales receipt printing):

- Member No

- Customer Name: *First Name + one space + Last Name*

- Phone Number

- If both `Tel_1` and `Tel_2` exist, `Tel_1` will be printed.

- If only one telephone number exists, neither `Tel_1` nor `Tel_2` will be printed.



## 相關資訊

- **Jira:** [FE-1832](https://ctil.atlassian.net/browse/FE-1832)
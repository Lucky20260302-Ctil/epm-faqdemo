---
project: FE
issue_key: FE-1308
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1308
created: '2023-11-02'
resolved: '2024-03-05'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1308: Double BP redeem for member'
---
# FE-1308: Double BP redeem for member

## 問題描述

Will duplicate the redeem record for the member.

 

Re-produce procedure:

1. Sales Memo  Tab1 and Tab2 - both select Member A

2. Sales Memo Tab1 Redeem BP as Cash Disc Amt Coupon

3. sales Memo Tab1 - Commit Payment

4. Sales Memo Tab2 - Select cash payment, commit payment, BP Redeem record duplicated in SM tab2



## 相關資訊

- **Jira:** [FE-1308](https://ctil.atlassian.net/browse/FE-1308)
- **解決方式:** Done
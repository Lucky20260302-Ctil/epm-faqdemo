---
project: FE
issue_key: FE-1901
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- day-end
- faq
- fe
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1901
created: '2026-03-17'
resolved: '2026-03-25'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1901: [CS-2058] Issue_ANZ_INC3434107_Question about Day END Cash Balancing'
---
# FE-1901: [CS-2058] Issue_ANZ_INC3434107_Question about Day END Cash Balancing

## 問題描述

 Will jump 2 rows if  type "Enter" instead of 1 row in CASH Denomination

Troubleshooting:

1. DAY END> Cash Drawer Tender Count Input>CASH> CASH Denomination

2.E.g. Enter quantity of 5 cents for 5, then we tick "Enter", it jump to 20cents instead of next row (10 cents).  



## 相關資訊

- **Jira:** [FE-1901](https://ctil.atlassian.net/browse/FE-1901)
- **解決方式:** Done
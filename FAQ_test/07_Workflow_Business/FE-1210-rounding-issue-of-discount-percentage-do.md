---
project: FE
issue_key: FE-1210
issue_type: Bug QA
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
jira_url: https://ctil.atlassian.net/browse/FE-1210
created: '2023-02-01'
resolved: '2023-03-28'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1210: Rounding issue of discount percentage (dotnetprint)'
---
# FE-1210: Rounding issue of discount percentage (dotnetprint)

## 問題描述

Display different rounding of discount percentage (dotnetprint)

 

item: W005 BLK/C WMN

Selling price: 42,120

Exact discount: 16.5 %

Net amount: 35,170

 

Print out of sales memo- dotnetprint (ON): Display 17%

Print out of sales memo- dotnetprint (OFF): Display 16%

 

Ref:20230201.jpg

 

Both of frontend screen show as 17%



## 相關資訊

- **Jira:** [FE-1210](https://ctil.atlassian.net/browse/FE-1210)
- **解決方式:** Done
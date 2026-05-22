---
project: FE
issue_key: FE-1315
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
jira_url: https://ctil.atlassian.net/browse/FE-1315
created: '2023-11-20'
resolved: '2023-12-14'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1315: [EFT] Pop up ''Only one EFT payment Allow in single transaction'' when non-EFT payment method selected first, then select EFT payment'
---
# FE-1315: [EFT] Pop up "Only one EFT payment Allow in single transaction" when non-EFT payment method selected first, then select EFT payment

## 問題描述

Reproduce steps:

1. Select non-EFT payment method, e.g.: E-payment

2. Select EFT payment

3. Click on Tick

Existing result:

Pop up "Only one EFT payment Allow in single transaction" & not allow to process to further steps



## 相關資訊

- **Jira:** [FE-1315](https://ctil.atlassian.net/browse/FE-1315)
- **解決方式:** Done
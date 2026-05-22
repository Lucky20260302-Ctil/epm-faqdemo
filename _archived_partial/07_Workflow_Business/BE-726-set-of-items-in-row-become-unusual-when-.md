---
project: BE
issue_key: BE-726
issue_type: Bug QA
status: Closed
tags:
- 07_workflow_business
- backend-(web)
- be
- faq
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-726
created: '2023-03-02'
resolved: '2023-03-02'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'BE-726: Set of items in row become unusual when user add items with no color & size'
---
# BE-726: Set of items in row become unusual when user add items with no color & size

## 問題描述

Env: [https://172.16.138.55/ChainStorePlus_AIGLE/home](https://172.16.138.55/ChainStorePlus_AIGLE/home)

Reproduce steps:

1. To Purchase Order Maintenance (PO3000)

2. Make a PO & insert PO no., Supplier, 

3. Click on Manage item

4. Select items with no color & size

5. Switch button between Line Mode & Matrix Mode

Existing result:

Set of items in row become unusal when user add items with no color & size (Ref: image-2023-03-02-15-10-16-094.png)

 

Remark:

Can use PO no. TEST123 for testing

 



## 相關資訊

- **Jira:** [BE-726](https://ctil.atlassian.net/browse/BE-726)
- **解決方式:** Done
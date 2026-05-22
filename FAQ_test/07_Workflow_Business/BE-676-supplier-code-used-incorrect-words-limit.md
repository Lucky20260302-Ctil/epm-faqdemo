---
project: BE
issue_key: BE-676
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
jira_url: https://ctil.atlassian.net/browse/BE-676
created: '2022-11-07'
resolved: '2022-11-25'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'BE-676: Supplier Code used incorrect words limitation'
---
# BE-676: Supplier Code used incorrect words limitation

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

ACC: sxd                          PW: sxd

Location: Process > Purchase Order Maintenance (PO3000)

Reproduce steps:

1. To Purchase Order Maintenance (PO3000)

2. Click Create

3. To Supplier Code

4. Select Supplier Code that are over 10 words e,g.:  CRIMSON_BRANDS

Existing result:

Field of Supplier is rounded by red outline, applied Text with Max Length = 10

 

Expected result:

Words limitation of Supplier Code should be 15 words



## 相關資訊

- **Jira:** [BE-676](https://ctil.atlassian.net/browse/BE-676)
- **解決方式:** Done
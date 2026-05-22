---
project: FE
issue_key: FE-836
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- frontend
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-836
created: '2020-11-16'
resolved: '2022-08-16'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-836: Member gift redemption, incorrect bonus point balance printed on memo'
---
# FE-836: Member gift redemption, incorrect bonus point balance printed on memo

## 問題描述

1. The BP balance before redemption is 60K

2. After redemption, 10K points has been used. But BP balance printed sales memo is 40K. It is expected that 60K - 10K=50K.

3. The GVIPRGPTS is 50K which is correct

DB copied in \\172.16.183.201\localuser\support\20201116\to_sang

Thanks.



## 相關資訊

- **Jira:** [FE-836](https://ctil.atlassian.net/browse/FE-836)
- **解決方式:** Done
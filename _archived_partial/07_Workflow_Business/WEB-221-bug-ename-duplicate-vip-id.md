---
project: WEB
issue_key: WEB-221
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- ename
- faq
- web
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-221
created: '2022-05-17'
resolved: '2022-05-31'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'WEB-221: Bug - Ename duplicate VIP ID'
---
# WEB-221: Bug - Ename duplicate VIP ID

## 問題描述

COACH Jira [ARP-22]  Bug - Ename duplicate VIP ID

 

After checking, we confirmed that the issue is caused by two device in same shop click the new member function at same time (time different around 30ms).

Therefore the same VIP no are generated for both device and cause the problem.



## 相關資訊

- **Jira:** [WEB-221](https://ctil.atlassian.net/browse/WEB-221)
- **解決方式:** Done
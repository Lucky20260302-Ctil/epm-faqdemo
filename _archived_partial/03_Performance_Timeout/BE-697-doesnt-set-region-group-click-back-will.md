---
project: BE
issue_key: BE-697
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- backend-(web)
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-697
created: '2022-11-14'
resolved: '2023-03-03'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-697: Doesn''t set Region group & Click Back will get stuck in MX3003'
---
# BE-697: Doesn't set Region group & Click Back will get stuck in MX3003

## 問題描述

Env: [https://172.16.138.101/chainstoreplus](https://172.16.138.101/chainstoreplus)

Location: MX3003

Reproduce steps:

1. To Region Grouping Control Maintenance (MX3003)

2. Click "Add new group"

3. Click Back

4. Pop up "Discard changes?"  

Existing result:

 no matter Click OK/ Cancel, it will pop "Please enter group code or delete the Region group", then "Discard changes?" would appear again 

 

(Ref:ChainStorePlus _ 99 - ERM Company 99 - Google Chrome 2022-11-14 15-38-22)

*This action become a loop, users have to Click Enter by keyboard back to home page



## 相關資訊

- **Jira:** [BE-697](https://ctil.atlassian.net/browse/BE-697)
- **解決方式:** Done
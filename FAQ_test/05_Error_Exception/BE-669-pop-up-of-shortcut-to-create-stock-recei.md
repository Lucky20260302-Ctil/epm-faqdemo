---
project: BE
issue_key: BE-669
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-669
created: '2022-11-04'
resolved: '2024-04-27'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-669: Pop up of shortcut to create stock receive (rc2000) still existing after click OK in Unauthorized Access'
---
# BE-669: Pop up of shortcut to create stock receive (rc2000) still existing after click OK in Unauthorized Access  

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/rc2000](https://172.16.138.101/chainstoreplus/rc2000)

ACC: P01      PW: P01

Reproduce steps:

1. Enter into Stock Receive input against PO/DRV (rc2000)

2. Click OK in Unauthorized Access

Existing result:

Pop up of shortcut to create stock receive (rc2000) is  still existing in home page (Ref: image-2022-11-04-11-06-11-167.png)



## 相關資訊

- **Jira:** [BE-669](https://ctil.atlassian.net/browse/BE-669)
- **解決方式:** Done
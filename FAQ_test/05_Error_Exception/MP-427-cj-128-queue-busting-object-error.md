---
project: MP
issue_key: MP-427
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-427
created: '2021-05-03'
resolved: '2021-05-17'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-427: CJ #128 - Queue Busting – Object error'
---
# MP-427: CJ #128 - Queue Busting – Object error

## 問題描述

- CJ Queue Busting – Object error

- Reproduce Steps:

- Create transaction with VIP information in mpos and save to Queue Busting

- Retrieve transaction from Queue Busting in mPOS

- Add one different item and save in Queue Busting

- Retrieve transaction from Queue Busting in mPOS again >> Error popped



## 相關資訊

- **Jira:** [MP-427](https://ctil.atlassian.net/browse/MP-427)
- **解決方式:** Done
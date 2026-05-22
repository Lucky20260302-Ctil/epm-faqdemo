---
project: MP
issue_key: MP-426
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
jira_url: https://ctil.atlassian.net/browse/MP-426
created: '2021-05-03'
resolved: '2021-05-17'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-426: CJ #130 - Queue Busting – Fail to Close the order in Queue Busting after complete transaction'
---
# MP-426: CJ #130 - Queue Busting – Fail to Close the order in Queue Busting after complete transaction

## 問題描述

- CJ Queue Busting – Fail to Close the order in Queue Busting after complete transaction

- Reproduce Steps:

- J805 use MPOS to create an order in queue questing with ref "Order_A" and "Order_B"

- POS retrieve order "Order_A" and issue sales memo. >> Order_A will disappear after payment >> Normal response

- MPOS retrieve order "Order_B" and issue sales memo. >> Order_B was keep after payment << Fix in this release
 *



## 相關資訊

- **Jira:** [MP-426](https://ctil.atlassian.net/browse/MP-426)
- **解決方式:** Done
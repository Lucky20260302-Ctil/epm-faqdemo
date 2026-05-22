---
project: BE
issue_key: BE-1171
issue_type: Task
status: Closed
tags:
- 04_data_sync
- be
- data-interface
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1171
created: '2025-08-29'
resolved: '2025-09-22'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1171: [CS-1579]  LGV payment orders from PangdongLai API'
---
# BE-1171: [CS-1579]  LGV payment orders from PangdongLai API

## 問題描述

Upon request, modify the sales export interfaces to remove LGV payment amount ( sum(joupay_pay_amt_bx) where payment_code = 'LGV') in the export amount “c_amount” and “c_pay_type”.



## 相關資訊

- **Jira:** [BE-1171](https://ctil.atlassian.net/browse/BE-1171)
- **解決方式:** Done
- **標籤:** LL_Sales_Interface
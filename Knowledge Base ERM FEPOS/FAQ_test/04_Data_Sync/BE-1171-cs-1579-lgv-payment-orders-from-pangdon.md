---
project: BE
issue_key: BE-1171
issue_type: Task
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1171"
created: 2025-08-29
resolved: 2025-09-22
resolution: Done
has_images: False
---

# BE-1171: [CS-1579]  LGV payment orders from PangdongLai API

> **類型:** Task | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.5
> **解決日期:** 2025-09-22
> **負責人:** Cy Lau
> **組件:** Data Interface

## 問題描述

Upon request, modify the sales export interfaces to remove LGV payment amount ( sum(joupay_pay_amt_bx) where payment_code = 'LGV') in the export amount “c_amount” and “c_pay_type”.



## 相關資訊

- **Jira:** [BE-1171](https://ctil.atlassian.net/browse/BE-1171)
- **解決方式:** Done
- **標籤:** LL_Sales_Interface
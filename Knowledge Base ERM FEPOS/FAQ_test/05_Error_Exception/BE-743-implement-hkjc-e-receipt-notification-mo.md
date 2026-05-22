---
project: BE
issue_key: BE-743
issue_type: SOW
status: Closed
faq_score: 4.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-743"
created: 2023-05-30
resolved: 2024-04-25
resolution: Done
has_images: False
---

# BE-743: Implement HKJC e-Receipt Notification module to Coach with templates and channels

> **類型:** SOW | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 4.5
> **解決日期:** 2024-04-25
> **負責人:** Hans Wong
> **組件:** Backend (Web)

## 問題描述

Original HKJC Notification workflow description:

UI: Notification Code Maintenance (MX5004)

Related DB:

notify - Notification setting and template.

nfreq - POS request notification entries.

nfqueue - Processed request and ready to send.

 

"nfreq_status = null" means not yet proc

"nfqueue_status = null" means not yet sent

 

VS Solution: Notification

 



## 相關資訊

- **Jira:** [BE-743](https://ctil.atlassian.net/browse/BE-743)
- **解決方式:** Done
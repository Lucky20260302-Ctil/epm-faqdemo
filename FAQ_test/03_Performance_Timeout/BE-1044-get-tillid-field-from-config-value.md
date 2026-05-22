---
project: BE
issue_key: BE-1044
issue_type: Task
status: Closed
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1044"
created: 2025-04-08
resolved: 2025-06-05
resolution: Done
has_images: False
---

# BE-1044: Get tillId field from config value

> **類型:** Task | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 5.5
> **解決日期:** 2025-06-05
> **負責人:** Jett.He
> **組件:** Data Interface

## 問題描述

As Disney LL does not accept tillid with English char, we cannot export the tillid such as 'MA', 'MB' to them if they have mPOS. Therefore, please help to update to interface program as below:

 

As-Is: Get tillid value from jouinv_no

 

To-Be: 

- change program to get tillid from config file 

- add a new config for determine tillid value



## 相關資訊

- **Jira:** [BE-1044](https://ctil.atlassian.net/browse/BE-1044)
- **解決方式:** Done
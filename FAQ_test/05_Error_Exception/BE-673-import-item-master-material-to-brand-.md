---
project: BE
issue_key: BE-673
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-673"
created: 2022-11-04
resolved: 2024-04-27
resolution: Done
has_images: False
---

# BE-673: Import Item Master Material to Brand 

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **解決日期:** 2024-04-27
> **負責人:** Joy Li
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

Current BE program fail to auto create brand code

 CS2000 APP Server

- Import Data (as0003.out)

- Update “Material Code” to “Brand Code” in item master interface for Mix & Match Promotion.

- New brand code will be create automatically if not exist.

- A default supplier code ‘OC’ will assign to the new brand code.

- This customization applies to CJ only.



## 相關資訊

- **Jira:** [BE-673](https://ctil.atlassian.net/browse/BE-673)
- **解決方式:** Done
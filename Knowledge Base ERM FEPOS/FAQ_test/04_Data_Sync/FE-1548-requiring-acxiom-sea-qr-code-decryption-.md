---
project: FE
issue_key: FE-1548
issue_type: Change Request
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1548"
created: 2024-11-04
resolved: 2024-12-24
resolution: Done
has_images: False
---

# FE-1548: Requiring Acxiom SEA QR Code decryption key 

> **類型:** Change Request | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **解決日期:** 2024-12-24
> **負責人:** Sang
> **組件:** Front End

## 問題描述

As requested by Coach SEA, we need to add a configuration setting named 'crm_qr_iv_key' to the backend ‘dbconfig’ table. This setting will specify the initialization vector (IV) key for decrypting CRM QR Codes. We will adopt the EFT key retrieval method to getting the IV key from the backend database during POS startup, and the key will then store in its local database.




## Jira Comments

> **Sang** (2024-11-04):
> 

## 相關資訊

- **Jira:** [FE-1548](https://ctil.atlassian.net/browse/FE-1548)
- **解決方式:** Done
---
project: FE
issue_key: FE-1548
issue_type: Change Request
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1548
created: '2024-11-04'
resolved: '2024-12-24'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1548: Requiring Acxiom SEA QR Code decryption key'
---
# FE-1548: Requiring Acxiom SEA QR Code decryption key 

## 問題描述

As requested by Coach SEA, we need to add a configuration setting named 'crm_qr_iv_key' to the backend ‘dbconfig’ table. This setting will specify the initialization vector (IV) key for decrypting CRM QR Codes. We will adopt the EFT key retrieval method to getting the IV key from the backend database during POS startup, and the key will then store in its local database.




## Jira Comments

> **Sang** (2024-11-04):
> 

## 相關資訊

- **Jira:** [FE-1548](https://ctil.atlassian.net/browse/FE-1548)
- **解決方式:** Done
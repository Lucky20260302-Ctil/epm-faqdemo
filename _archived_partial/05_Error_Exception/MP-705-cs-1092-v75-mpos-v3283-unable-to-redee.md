---
project: MP
issue_key: MP-705
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
jira_url: https://ctil.atlassian.net/browse/MP-705
created: '2024-07-15'
resolved: '2024-08-30'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-705: [CS-1092] V75 - MPOS v3.28.3 unable to redeem Gift cert'
---
# MP-705: [CS-1092] V75 - MPOS v3.28.3 unable to redeem Gift cert

## 問題描述

Testing Data:

- Testing Version 3.28.2(20240627-1)

- OC602 Till 0 : 172.16.138.94

- Region :13 (MY)

> 📎 **image-20240715-021452.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9e806028-7d72-4248-bf86-6e2b47a1b30a)（需 Jira 登入）
check existing GC SQL in dbo.dbmas:

>> select * from TblGiCert where gicert_expiry_date >='2024-01-01' and gicert_redeem_status = '' and gicert_redeem_date is null



## 附件截圖

1. 📎 **image-20240715-021452.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9e806028-7d72-4248-bf86-6e2b47a1b30a)

## 相關資訊

- **Jira:** [MP-705](https://ctil.atlassian.net/browse/MP-705)
- **解決方式:** Done
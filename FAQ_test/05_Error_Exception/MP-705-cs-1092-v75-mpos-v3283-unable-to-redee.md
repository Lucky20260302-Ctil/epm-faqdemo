---
project: MP
title: "MP-705: [CS-1092] V75 - MPOS v3.28.3 unable to redeem Gift cert"
issue_key: MP-705
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-705"
created: 2024-07-15
resolved: 2024-08-30
resolution: Done
has_images: True
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
---
project: MP
issue_key: MP-749
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-749
created: '2025-02-26'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-749: [MPOS-78]MPOS 3.29.5  - JP region - Miss notification under tax free module if the price is lower than 5000JPY'
---
# MP-749: [MPOS-78]MPOS 3.29.5  - JP region - Miss notification under tax free module if the price is lower than 5000JPY

## 問題描述

during testing for MPOS IPA 3.29.5 20250212.1, for JP region, MPOS Miss notification under tax free module. if the price is lower than 5000JPY, should have below notification under payment page. BTW, we confirmed CS2K no such issue.

Testing info:

Testing machine IP: 172.24.253.20(J805)

any item price under 5000JPY, any member, under tax free module.

> 📎 **image-20250226-120200.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a1877e90-5f50-44ac-ac8f-031d60b30b5d)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250226-120200.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a1877e90-5f50-44ac-ac8f-031d60b30b5d)


## Jira Comments

> **Cy Lau** (2025-02-26):
>   PLEASE check if did called  IsValidTaxFree  api

> **Daniel Leung** (2025-02-27):
> Popup displayed correctly

> **Daniel Leung** (2025-02-27):
>  Can you get the MPOS log and MPOS API log?

> **Andrew_Au** (2025-03-21):
>  The ticket pending for a long time. Please update the ticket status

> **Sherman tse** (2025-05-02):
> This issue has closed in Tapestry side JIRA, with reason: Confirmed it's not the issue. The system will only check the list price, not the amount after discount.  For the details, please refer to  https://jira.tapestry.support/browse/MPOS-78 Close case

## 相關資訊

- **Jira:** [MP-749](https://ctil.atlassian.net/browse/MP-749)
- **解決方式:** Done
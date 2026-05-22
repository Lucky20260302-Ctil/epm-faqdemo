---
project: BE
issue_key: BE-858
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-858"
created: 2024-05-24
resolved: 2024-06-17
resolution: Done
has_images: False
---

# BE-858: [CS-1006] Issue_Staff member purchase issue in HKMO

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.5
> **解決日期:** 2024-06-17
> **負責人:** Sherman tse
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

Tapestry team request to exclude vip_type=E or T from the sync job for VIP data.

Program exe: \Obj\csplus_syncmember.exe

Request:

1. Add config in csplus_syncmember.exe.config

2. member sync with exclude the member type which marked in config.

3. Check if Member sync select SQL with (nolock) 




## Jira Comments

> **Joy Li** (2024-05-27):
>   Please provide ETA:

## 相關資訊

- **Jira:** [BE-858](https://ctil.atlassian.net/browse/BE-858)
- **解決方式:** Done
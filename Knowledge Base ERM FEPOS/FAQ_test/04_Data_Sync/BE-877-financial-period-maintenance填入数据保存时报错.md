---
project: BE
issue_key: BE-877
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-877"
created: 2024-07-19
resolved: 2024-08-28
resolution: Done
has_images: True
---

# BE-877: Financial Period Maintenance:填入数据，保存时报错

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2024-08-28
> **負責人:** ryan
> **組件:** Backend (Web)

## 問題描述

Reproduce steps:

1. 新建一個 Financial Year

2. 填入必要輸入的資料

3. 点击save

Incorrect result:

- 提示Please Enter Date

> 📎 **image-20240719-015917.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b460a980-ccb4-42ca-b5ac-c2bcb9366778)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240719-015917.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b460a980-ccb4-42ca-b5ac-c2bcb9366778)


## Jira Comments

> **Andy Ko** (2024-08-27):
>  currently the screen must have input in all rows. 

## 相關資訊

- **Jira:** [BE-877](https://ctil.atlassian.net/browse/BE-877)
- **解決方式:** Done
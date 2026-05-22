---
project: FE
issue_key: FE-1585
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, msmq]
jira_url: "https://ctil.atlassian.net/browse/FE-1585"
created: 2024-12-16
resolved: 
resolution: 
has_images: True
---

# FE-1585: IMX MSMQ missing sales memo

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.5
> **負責人:** Sang
> **組件:** MSMQ

## 問題描述

This shop after upgrading BE MSMQ started miss sending memos to BE, this issue is happening every day.

Below image missing memo 00001313 and sqlpcda table cant not find the memo queue 

> 📎 **image-20241216-020859.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b5e94136-106d-43b0-9359-84b6211ea6fd)（需 Jira 登入）
Log Path \\172.16.183.201\localuser\support\20241216\Sang



## 附件截圖

1. 📎 **image-20241216-020859.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b5e94136-106d-43b0-9359-84b6211ea6fd)

## 相關資訊

- **Jira:** [FE-1585](https://ctil.atlassian.net/browse/FE-1585)
---
project: FE
title: "FE-1712: [INC3010134]客户做完销售以后，db的vip表中issue date会被sales memo日期同步，实际上，issue date是不应该被sales memo的销售日期同步的。目前，issue date被同步的逻辑是什么？"
issue_key: FE-1712
issue_type: Bug DEV
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1712"
created: 2025-06-11
resolved: 2025-09-08
resolution: Done
has_images: True
---

# FE-1712: [INC3010134]客户做完销售以后，db的vip表中issue date会被sales memo日期同步，实际上，issue date是不应该被sales memo的销售日期同步的。目前，issue date被同步的逻辑是什么？

## 問題描述

以OC3000C00002005为例，6.2做了销售以后，VIP issue date就被同步成6.2了，并且在dbtmnlogd表中是没有这个被同步的记录的。

> 📎 **image-20250618-085737.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e5875808-b071-40bd-8e25-4f2662eef4f8)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250618-085737.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e5875808-b071-40bd-8e25-4f2662eef4f8)

## 相關資訊

- **Jira:** [FE-1712](https://ctil.atlassian.net/browse/FE-1712)
- **解決方式:** Done
---
project: FE
title: "FE-1604: [CS-1315] - Issue_JP_INC2775648_Rakuten outlet J148 - CS2000 failed import transaction on 12/19"
issue_key: FE-1604
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, interface]
jira_url: "https://ctil.atlassian.net/browse/FE-1604"
created: 2025-01-10
resolved: 
resolution: 
has_images: True
---

# FE-1604: [CS-1315] - Issue_JP_INC2775648_Rakuten outlet J148 - CS2000 failed import transaction on 12/19

## 問題描述

This's known issue and already happened before, as checked the interface file we can see the same transaction number:44410041-41 with different site code.this situation should be the customer selected one item from J147(Rakuten Fashion) and another item from J148(Rakuten Fashion OUTLET), then paid these 2 items together on Rakuten website,so the transaction number is unique and same.

However,  when these 2 records uploaded to cs2k, cs2k recognised the site code was mismatched, cs2k will not import the 2^nd record per system's logic. 

> 📎 **image-20250110-052626.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/799351b3-3032-47c6-a0b7-a5f31b43be0f)（需 Jira 登入）

This issue come from Email “INC2775648 Rakuten outlet J148 - CS2000 failed import transaction on 12/19“

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/217575d3-9a91-4130-b68e-e3c82238f2a9)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20250110-052626.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/799351b3-3032-47c6-a0b7-a5f31b43be0f)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/217575d3-9a91-4130-b68e-e3c82238f2a9)

## 相關資訊

- **Jira:** [FE-1604](https://ctil.atlassian.net/browse/FE-1604)
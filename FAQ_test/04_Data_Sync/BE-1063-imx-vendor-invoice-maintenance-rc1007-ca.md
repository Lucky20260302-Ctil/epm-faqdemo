---
project: BE
issue_key: BE-1063
issue_type: Bug PRD
status: DEV Done
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1063"
created: 2025-04-29
resolved: 
resolution: 
has_images: True
---

# BE-1063: IMX Vendor Invoice Maintenance (RC1007) can not follow 

> **類型:** Bug PRD | **狀態:** DEV Done
> **分類:** 資料與同步 | **FAQ 分數:** 5.0
> **負責人:** Jerry Wong
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

RC1007 wasn’t checking the program with fiscal calendar.

> 📎 **image-20250429-025155.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/28899e14-397f-4e91-89b5-8c4df8b751da)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250429-025155.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/28899e14-397f-4e91-89b5-8c4df8b751da)


## Jira Comments

> **Jerry Wong** (2025-04-29):
> Release: \\ds411\csms60\delivery\imx\rc1007.2025-04-29

> **Jerry Wong** (2025-04-29):
> Supplier and D/N should be matched with joupxh_supp and joupxh_date in joupxh. Then, the joupxh_date should be greater than the fiscald_date, check month end if fiscald date have not set

> **Jason Wu** (2025-05-02):
>  please also help to add the financial year check for these program IC5006    	Return To Supplier Validation IC5006    	Return To Supplier Validation IC5009    	Return To Supplier Posting IC5009    	Return To Supplier Posting RC1004    	Stock Receive Validation RC1004    	Stock Receive Validation RC1005    	Stock Receive Posting RC1005    	Stock Receive Posting

## 相關資訊

- **Jira:** [BE-1063](https://ctil.atlassian.net/browse/BE-1063)
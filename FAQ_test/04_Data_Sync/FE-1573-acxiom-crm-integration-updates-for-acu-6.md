---
project: FE
title: "FE-1573: [ACXIOM CRM Integration] Updates for ACU-68: UI Update for Member Profile page"
issue_key: FE-1573
issue_type: SOW
status: Closed
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1573"
created: 2024-12-02
resolved: 2024-12-05
resolution: Done
has_images: False
---

# FE-1573: [ACXIOM CRM Integration] Updates for ACU-68: UI Update for Member Profile page

## 問題描述

None


## Jira Comments

> **Joseph_Hu** (2024-12-03):
> Sorry for misunderstand, I used the account which is not in CRM so that make the ‘Purchase History’ cannot be opened. Here is the account which is provided by developer “OC135TC00000028”, and it can be opened normally.

> **Andrew_Au** (2024-12-04):
> Please kindly refer to below translation. Thank you.    POS FE UI Purchase History           English Simplified Chinese From Data Source Mapping to API field Order No 订单日期及订单号 #20240511#OC135#00033338 CustomerPurchase.order_no String 订单编号 Order Total Amount 订单总金额 4,950.00 CustomerPurcahse.amount Float 实际支付金额 Purchase Items 产品         Item Name 产品SKU Coated Canvas Signature Charlie Bucket 2_B4NQ4(1027_B4NQ4) PurchaseSku.sku_name + PurchaseSku.sku_code String 产品名称 Style 款式 1027 PurchaseSku.style String 产品样式 Color 颜色 B4NQ4 PurchaseSku.color String 产品颜色 Size 尺寸 NA PurchaseSku.size String 产品尺寸 Item Quantity 数量 2 PurchaseSku.quantity Int 数量 Item Total Amount 产品总金额 4,950 PurchaseSku.amount Float 实际支付总额       Best Regards   Steven Jiang   Asia Retail Project

> **Joseph_Hu** (2024-12-04):
>   The label need to change as the latest email from Steven, Here is what he marks as ‘ Yellow ’

> **Andrew_Au** (2024-12-04):
> Attached the last email reply from Coach. Please follow this translation modify the program again.   

> **Sherman tse** (2024-12-04):
> Just follow email to adjust the words of Simplified Chinese, edited the ui.json in purchase history release (v1.0.0) \\ds411\public\daniel\acxiom\purchase history\v1.0.0 Please copy the above path to C:\www\ERM-COACH-BE7\BEGWCRM_CN\MemberPurchase\acxiom in 172.16.138.8

> **Joy Li** (2024-12-04):
> 

> **Joy Li** (2024-12-05):
> released by    on 2024-12-05. FE v75.004.0903.0000

## 相關資訊

- **Jira:** [FE-1573](https://ctil.atlassian.net/browse/FE-1573)
- **解決方式:** Done
- **標籤:** Ticket
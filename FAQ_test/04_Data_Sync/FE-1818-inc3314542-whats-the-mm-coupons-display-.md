---
project: FE
title: "FE-1818: [INC3314542] What’s the MM coupons display logic in MPOS dayend report?"
issue_key: FE-1818
issue_type: Bug PRD
status: Open
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, report]
jira_url: "https://ctil.atlassian.net/browse/FE-1818"
created: 2025-11-25
resolved: 
resolution: 
has_images: True
---

# FE-1818: [INC3314542] What’s the MM coupons display logic in MPOS dayend report?

## 問題描述

@@Sang SOG team callout one case,V75 PRC店铺OC213 11-22 号没有MPOS销售，但是在MPOS dayend report里面却有 MM coupons的使用记录，这些MM Coupons 的记录是从哪来的呀？what’s the MM coupons display logic in dayend report?Thanks!

1.OC213 MPOS dayend report:

> 📎 **image-20251125-070426.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ad0ed9ec-1c58-4ce2-84e3-ad496b93cd7c)（需 Jira 登入）
2.OC213 till0 dayend report:

查询发现这些MM coupon 是 Till0 的memo在用，在Till0 dayend report 和 PC file 可以看到使用记录，

但为什么会显示在MPOS dayend report中（MPOS没有做销售的情况下）？

> 📎 **image-20251125-072120.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f48d67b5-aebb-4830-b82f-e3528b83de3d)（需 Jira 登入）

> 📎 **image-20251125-081323.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0864d7a0-2130-49ac-ae5d-4f9df7b338be)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251125-070426.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ad0ed9ec-1c58-4ce2-84e3-ad496b93cd7c)
2. 📎 **image-20251125-072120.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f48d67b5-aebb-4830-b82f-e3528b83de3d)
3. 📎 **image-20251125-081323.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0864d7a0-2130-49ac-ae5d-4f9df7b338be)


## Jira Comments

> **Tovi Wang** (2025-11-25):
>  22 Nov & 23 Nov FE logs for your further checking.Thanks！ CC   

> **Sang** (2025-11-25):
>  Please check Till 0 sse dbtran.mdf, any 22-Nov and 23 -Nov records in tables [invtrx file header],[invtrx file detail],[invtrx file payment] 

> **Tovi Wang** (2025-11-25):
>  Noted,Thanks!

> **Tovi Wang** (2025-11-26):
>  I checked the Till0 dbsse dbtrans.Not any 22-Nov and 23 -Nov records in tables [invtrx file header],[invtrx file detail],[invtrx file payment].Could you advice next action? 1. 2. 3.

> **Cy Lau** (2025-11-26):
> mdt = SalesSummaryByItem :  Dim strSQL As String = "select " & pFields         Dim sInvH As String = GetDBTableNameSQL("InvTrx File Header")         Dim sInvD As String = GetDBTableNameSQL("InvTrx File Detail")         strSQL &= ",sum(D.Invtrx_List_Price * D.Invtrx_Item_Qty) as Item_List_Amt,"         strSQL &= " sum(D.Invtrx_Curr_Price * D.Invtrx_Item_Qty) as Item_Curr_Amt," 'KTS 160512         strSQL &= " sum((D.Invtrx_List_Price * D.Invtrx_Item_Qty) - D.Invtrx_MixCouponRef_Net_Amt) as Item_Disc_Amt,"         strSQL &= " sum(D.Invtrx_Item_Qty) as Item_Qty,"         strSQL &= " sum(Case When INVTRX_STOCK_IND ='S' Then [Invtrx_Item_Qty] Else 0 END) as MMC_Qty,"         strSQL &= " sum(D.Invtrx_Net_Amt) as Item_Net_Amt,"         strSQL &= " sum(D.Invtrx_MixCouponRef_Net_Amt) as NetNet_Amt,"

> **Cy Lau** (2025-11-26):
> Also would it be the same issue if redo dayend ?

> **Tovi Wang** (2025-11-27):
>    I just redo 11-22 till0 dayend,Can reproduce this issue.We can see the MM coupons dispaly in MPOS dayend report.The MM coupons was used by Till0 memo.

> **Tovi Wang** (2025-11-27):
> Add more find for your reference: 我查了同一家店同一个Till,23号Till0 也有MM coupons使用记录，但是23号的MPOS dayend report中却没有MM coupons  display. It’s so strange and confused me. 1. 11-23号till0 RP file 和 MPOS RP file 2. 11-23号till0 PC file,MM coupon使用记录 3. 11-22 Till0 RP and [INVTRX FILE DETAIL]

> **Tovi Wang** (2025-11-27):
>  11月Till0 & MPOS 的PC，RP file. till0 22，23号的dbtrans for your further checking.

## 相關資訊

- **Jira:** [FE-1818](https://ctil.atlassian.net/browse/FE-1818)
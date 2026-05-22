---
tags: [faq, fe, 列印]
component: "report"
symptom: "@@Sang SOG team callout one case,V75 PRC店铺OC213 11-22 号没有MPOS销售，但是在MPOS dayend report里面却有 MM coupons"
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: FE-1818
resolved: 
fix-version: ""
---

# FE-1818: [INC3314542] What’s the MM coupons display logic in MPOS dayend report?

## 問題

@@Sang SOG team callout one case,V75 PRC店铺OC213 11-22 号没有MPOS销售，但是在MPOS dayend report里面却有 MM coupons的使用记录，这些MM Coupons 的记录是从哪来的呀？what’s the MM coupons display logic in dayend report?Thanks!
1.OC213 MPOS dayend report:
2.OC213 till0 dayend report:
查询发现这些MM coupon 是 Till0 的memo在用，在Till0 dayend report 和 PC file 可以看到使用记录，
但为什么会显示在MPOS dayend report中（MPOS没有做销售的情况下）？

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Tovi Wang** (2025-11-25):
@@Sang 22 Nov & 23 Nov FE logs for your further checking.Thanks！
CC @@Joy Li
**Sang** (2025-11-25):
@@Tovi Wang Please check Till 0 sse dbtran.mdf, any 22-Nov and 23 -Nov records in tables [invtrx file header],[invtrx file detail],[invtrx file payment]
**Tovi Wang** (2025-11-25):
@@Sang Noted,Thanks!
**Tovi Wang** (2025-11-26):
@@Sang I checked the Till0 dbsse dbtrans.Not any 22-Nov and 23 -Nov records in tables [invtrx file header],[invtrx file detail],[invtrx file payment].Could you advice next action?
1.
2.
3.
**Cy Lau** (2025-11-26):
mdt = SalesSummaryByItem :
Dim strSQL As String = "select " & pFields
Dim sInvH As String = GetDBTableNameSQL("InvTrx File Header")
Dim sInvD As String = GetDBTableNameSQL("InvTrx File Detail")
strSQL &= ",sum(D.Invtrx_List_Price * D.Invtrx_Item_Qty) as Item_List_Amt,"
strSQL &= " sum(D.Invtrx_Curr_Price * D.Invtrx_Item_Qty) as Item_Curr_Amt," 'KTS 160512
strSQL &= " sum((D.Invtrx_List_Price * D.Invtrx_Item_Qty) - D.Invtrx_MixCouponRef_Net_Amt) as Item_Disc_Amt,"
strSQL &= " sum(D.Invtrx_Item_Qty) as Item_Qty,"
strSQL &= " sum(Case When INVTRX_STOCK_IND ='S' Then [Invtrx_Item_Qty] Else 0 END) as MMC_Qty,"
strSQL &= " sum(D.Invtrx_Net_Amt) as Item_Net_Amt,"
strSQL &= " sum(D.Invtrx_MixCouponRef_Net_Amt) as NetNet_Amt,"
strSQL &= " sum(D.Invtrx_Memo_Disc_Adj) as Memo_Disc_Amt"
strSQL &= " from " & sInvH & " H inner join " & sInvD & " D"
strSQL &= " on H.Invtrx_No = D.Invtrx_No"
strSQL &= GetFilterSQL(pPara, pFilterBy)
If pGroupBy.Trim <> "" Then strSQL &= " Group by " & pGroupBy
If pOrderBy.Trim <> "" Then strSQL &= " Order by " & pOrderBy
Return strSQL
So maybe oberve at InvTrx File Header & InvTrx File Detail
**Cy Lau** (2025-11-26):
Also would it be the same issue if redo dayend ?
**Tovi Wang** (2025-11-27):
@@Cy Lau @@Sang I just redo 11-22 till0 dayend,Can reproduce this issue.We can see the MM coupons dispaly in MPOS dayend report.The MM coupons was used by Till0 memo.
**Tovi Wang** (2025-11-27):
Add more find for your reference:
我查了同一家店同一个Till,23号Till0 也有MM coupons使用记录，但是23号的MPOS dayend report中却没有MM coupons [display.](http://display.It)It’s so strange and confused me.
1.
11-23号till0 RP file 和 MPOS RP file
2.
11-23号till0 PC file,MM coupon使用记录
3.
11-22 Till0 RP and [INVTRX FILE DETAIL]
**Tovi Wang** (2025-11-27):
@@Sang 11月Till0 & MPOS 的PC，RP file.
till0 22，23号的dbtrans for your further checking.

## 相關資訊

- Jira: [FE-1818](https://ctil.atlassian.net/browse/FE-1818)
- Fix Version: 未記錄
- 解決日期: 未記錄

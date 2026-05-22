---
project: BE
title: "BE-1204: [CS-1544]Addition Fields #63,#64 for CAR"
issue_key: BE-1204
issue_type: Change Request
status: Closed
faq_score: 8.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1204"
created: 2025-11-04
resolved: 2026-02-26
resolution: Done
has_images: False
---

# BE-1204: [CS-1544]Addition Fields #63,#64 for CAR

## 問題描述

For capture young generation of customer purchase history,  they want to pass 3rd party sales transaction information from CS2K to other system.

 

Source : CS2K

Destination: CRM DB or CAR

Module Targetting : CAR Interface.

---

The sample data is accurate. The issue was identified as the number 61 in the specification being omitted, causing a shift in the sales type number. The Sales Type should be labelled as #63, and the Usage as #64.

| **#** | **Field** | **Key** | **Type** | **Length** | **Data Sample** | **Remarks** | 
| 01 | Prefix | * | CHAR | 1 | P | Always = ‘P’, ‘P’ – Sales Memo | 
| 02 | Location | * | CHAR | 8 | J101 |   | 
| 03 | Memo# | * | CHAR | 8 | 00047267 |   | 
| 04 | Date |   | DATE | 8 | 20180619 | Format YYYYMMDD | 
| 05 | Indicator |   | CHAR | 1 | I | I – Item | 
| 06 | Line# | * | NUM | 9(5) | 1 |   | 
| 07 | UPC |   | CHAR | 30 | 886382315792 |   | 
| 08 | Item |   | CHAR | 30 | F26939 |   | 
| 09 | Color |   | CHAR | 10 | SVMJ9 |   | 
| 10 | Size |   | CHAR | 10 |   |   | 
| 11 | Inseam |   | CHAR | 10 |   |   | 
| 12 | Quantity |   | NUM | 9(7) | 1 |   | 
| 13 | Sell Price |   | NUM | 9(10).99 | 7560.00 |   | 
| 14 | Item Amount |   | NUM | 9(12).99 | 7560.00 |   | 
| 15 | Item Amount (FX) |   | NUM | 9(12).99 | 7560.00 |   | 
| 16 | Item Cost |   | NUM | 9(10).99 | 0.00 |   | 
| 17 | List Price |   | NUM | 9(10).99 | 21600.00 |   | 
| 18 | Current Price |   | NUM | 9(10).99 | 21600.00 |   | 
| 19 | Item Discount Adjust |   | NUM | 9(12).99 | 0 |   | 
| 20 | Item Discount |   | NUM | 9(3).99 | 65.00 |   | 
| 21 | Sales Staff |   | CHAR | 10 | 666778 |   | 
| 22 | Cashier |   | CHAR | 10 | 100500 |   | 
| 23 | Memo Discount |   | NUM | 9(3).99 | 0.00 |   | 
| 24 | Total Amount |   | NUM | 9(12).99 | 7560.00 |   | 
| 25 | Total Amount (FX) |   | NUM | 9(12).99 | 7560.00 |   | 
| 26 | Misc. Amount |   | NUM | 9(12).99 | 0.00 |   | 
| 27 | Memo Discount Amount |   | NUM | 9(12).99 | 0.00 |   | 
| 28 | Void Flag |   | CHAR | 1 |   | Blank – Normal
‘1’ – Voided Memo
‘2’ – Void Memo | 
| 29 | Currency |   | CHAR | 3 | JPY |   | 
| 30 | Exchange Rate |   | NUM | 9(5).9(5) | 1.00000 |   | 
| 31 | Hour |   | NUM | 9(2) | 11 |   | 
| 32 | Minute |   | NUM | 9(2) | 33 |   | 
| 33 | Member No. |   | CHAR | 15 | OC632C00001005 |   | 
| 34 | Member Type |   | CHAR | 10 | A |   | 
| 35 | Nationality |   | CHAR | 10 |   |   | 
| 36 | Age Group |   | CHAR | 10 |   |   | 
| 37 | Gender |   | CHAR | 1 |   |   | 
| 38 | Reason |   | CHAR | 10 | 01 |   | 
| 39 | Price Reason |   | CHAR | 10 |   |   | 
| 40 | Deposit Location |   | CHAR | 8 |   |   | 
| 41 | Deposit No. |   | CHAR | 8 |   |   | 
| 42 | Deposit Amount |   | NUM | 9(12).99 | 0.00 |   | 
| 43 | GST Percent |   | NUM | 9(3).99 | 8.00 |   | 
| 44 | GST Item Amount |   | NUM | 9(12).99 | 560.00 |   | 
| 45 | GST Total Amount |   | NUM | 9(12).99 | 560.00 |   | 
| 46 | Void No. |   | CHAR | 8 |   |   | 
| 47 | Void Reason |   | CHAR | 10 |   |   | 
| 48 | Return Location |   | CHAR | 8 |   |   | 
| 49 | Return Memo# |   | CHAR | 8 |   |   | 
| 50 | Remarks |   | CHAR | 40 |   |   | 
| 51 | Coupon Quantity |   | NUM | 9(7) |   |   | 
| 52 | Standard Cost |   | NUM | 9(10).99 | 0.00 |   | 
| 53 | Tax Exempt |   | CHAR | 1 | N | ‘Y’ – Tax Exempt Transaction
‘N’ – Not Tax Exempt Transaction | 
| 54 | Invoice Tax Exempt Amount |   | NUM | 9(12).99 | 0.00 |   | 
| 55 | Item Tax Exempt Amount |   | NUM | 9(12).99 | 0.00 |   | 
| 56 | Form No. |   | CHAR | 10 |   |   | 
| 57 | Customer Attribute |   | CHAR | 10 |   |   | 
| 58 | Memo Attribute |   | CHAR | 1 |   |   | 
| 59 | Stock Indicator |   | CHAR | 1 | B | ‘B’ – Buy Off Stock
‘V’ – Service Item
‘S’ – Coupon M&M Item | 
| 60 | Free Gift |   | CHAR | 1 |   | Blank – Normal Item
‘Y’ – Free Gift Item | 
| 61 | Posting Date |   | DATE | 8 | 20180619 | Format YYYYMMDD
Jouinv.Jouinv_date | 
| 62 | Posting Time |   | CHAR | 8 | 120154 | Format HHMMSS
HH = Jouinv.Jouinv_hour
MM = Jouinv.Jouinv_mn
SS = hardcode as “00” | 
|   |   |   |   |   |   |   | 
| 63 | Sales Type |   | CHAR | 2 | 00 | For normal memo [sum(jouinv_item_qty) > 0] >> Sales Type = 00

For void/return memo [sum(jouinv_item_qty) < 0] >> Sales Type = 01

For exchange memo [sum(jouinv_item_qty) = 0]- Item with +ve Qty >> Sales Type = 02- Item with -ve Qty >> Sales Type = 03

 | 
| 64 | Usage |   | CHAR | 1 | 1 | Map to jouinv_memo_attr
This information is only available if the Thank You Card dialogue is enabled. Currently, only Coach Japan is enabled.
Blank – Thank You Card dialogue not enabled.
‘1’ – Self Use
‘2’ – Gift
'3' - Mix | 



## 相關資訊

- **Jira:** [BE-1204](https://ctil.atlassian.net/browse/BE-1204)
- **解決方式:** Done
---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Recent 2 days we've keep receiving below error message for Coach MY e-invoice. Transaction no is: OC"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: BE-1028
resolved: 
fix-version: ""
---

# BE-1028: [CS-1376] MY E-invoice - "OCF77-20228699" unable send to BDO

## 問題

Recent 2 days we've keep receiving below error message for Coach MY e-invoice. Transaction no is: OCF77-20228699, kindly help to check, log also attached.
[{"documentNumber":"OCF77-20228699","errors":[
{"errorCode":"E1089","errorMessage":"Incorrect Line Item excluding tax amount entered, it should be equal to the value of Subtotal - Discount + Fee / Charge Amount."}
,{"errorCode":"E1240","errorMessage":"Invalid data in Invoice line Items"}]
1.error info in log
2.OCF77-20228699 data in DB.The error if due to item_sell_price(585) > item_list_price(460) or not?Please help to double confirm and clarify.Thanks!
@@Anson Cheung

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2025-03-12):
@@Anson Cheung Please help to take a look this error message and identify the RCA.Follow logs for your further checking.Thanks!
**Anson Cheung** (2025-03-12):
@@Tovi Wang it is due to item_sell_price(460) < item_list_price(585) and the total discount amount < 0, the data will be absolute so the item_list_price + discount amount is not matching the sub total amount.
**Tovi Wang** (2025-03-12):
@@Anson Cheung Many Thanks for your help to double check.
Due to item_sell_price(585) > item_list_price(460),right?
**Tovi Wang** (2025-04-15):
Dear ALL,
Issue fixed now.Closed first.

## 相關資訊

- Jira: [BE-1028](https://ctil.atlassian.net/browse/BE-1028)
- Fix Version: 未記錄
- 解決日期: 未記錄

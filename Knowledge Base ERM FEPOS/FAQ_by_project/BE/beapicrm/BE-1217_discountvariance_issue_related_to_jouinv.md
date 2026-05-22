---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Discountvariance issue related to jouinv_exrate,jouinv_item_qty,jouinv_item_amt"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1217
resolved: 2026-05-14
fix-version: ""
---

# BE-1217: Discountvariance issue related to jouinv_exrate,jouinv_item_qty,jouinv_item_amt

## 問題

Discountvariance issue related to jouinv_exrate,jouinv_item_qty,jouinv_item_amt
KSG region, Pos V75.004.0702.0000
KSG729-00028561/00028562
00028561 is the original memo, 00028562 is the void memo.
checked in PCD file, the data is normally
but in BE, the value of the three fields are incorrect.
CC: @@Joy Li @@Tovi Wang

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-14
### Jira Comments (3 則)
**Andrew_Au** (2026-05-08):
@@pierre.shi Please update the ticket status
**pierre.shi** (2026-05-13):
@@Andrew_Au  please help to close . thanks
**Automation for Jira** (2026-05-14):
Issue has been created since
Days since: 166
Week since : 23
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [BE-1217](https://ctil.atlassian.net/browse/BE-1217)
- Fix Version: 未記錄
- 解決日期: 2026-05-14

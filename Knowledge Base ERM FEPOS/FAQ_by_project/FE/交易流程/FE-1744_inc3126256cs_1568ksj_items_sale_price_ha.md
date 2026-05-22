---
tags: [faq, fe, 交易流程]
component: "Front End v720.02"
symptom: "C309-00117534"
root-cause: "待提取"
solution: "### Jira Comments (12 則)"
jira: FE-1744
resolved: 
fix-version: ""
---

# FE-1744: [INC3126256][CS-1568]KSJ_item's sale price has variance between POS and receipt

## 問題

C309-00117534
Item SKU: KM471 001
sale price displaying on POS: 25,696 JPY(Tax in)
sale price showing on receipt: 23,361 JPY(with out Tax )
consumption tax rate: 10%
User think the sales price on receipt should be 23,360 JPY instead of 23,361 JPY, since 25,696/1.1=23,360
1.C309-00117534 in DB
2.Troubleshooting excel details for your reference.
1.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (12 則)
**Tovi Wang** (2025-08-07):
@@Joy Li @@Sang As talked in teams.Please help to double check and confirm the details calculate logic for this free tax memo.Logs will provided to you in later.Thanks!
**Sang** (2025-08-07):
@@Tovi Wang Please get Back dbtrans.sdf
**Tovi Wang** (2025-08-07):
@@Sang Dbtbk file for that day.right?
**Sang** (2025-08-07):
@@Tovi Wang Yes
**Tovi Wang** (2025-08-07):
@@Sang All FE logs & dbtbk file here.Please help to take a look in advance.Many Thanks!
**Sang** (2025-08-12):
@@Tovi Wang Attached C309 till0.zip contains 31/7/25 till 1 dbtrans.sdf (Dbtbk01.1.sdf). Please get Till 0 1/8/25 dbtrans.sdf and dbhist.sdf
**Sang** (2025-08-12):
@@Joy Li @@Tovi Wang @@Cy Lau
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
Print out:
PCD:
**Sang** (2025-08-19):
@@Tovi Wang Have u get till 0 dbtrans.sdf ?  Please get one set of mastconv also. thanks
**Tovi Wang** (2025-08-19):
@@Sang
Do we also need the C309 Dbmas?
**Sang** (2025-08-19):
@@Tovi Wang Yes. Please get either dbmas or mastconv. Thanks
**Tovi Wang** (2025-08-20):
@@Sang Dbmas here for your further checking.
**Tovi Wang** (2025-08-29):
We has calarified the details to Coach team.Closed first.

## 相關資訊

- Jira: [FE-1744](https://ctil.atlassian.net/browse/FE-1744)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "@@Sang Coach Team callout 2 CN V75 store,Tax  are missing for two CN exchange transactions. I has ap"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1688
resolved: 2025-05-30
fix-version: ""
---

# FE-1688: [CS-1429][INC2939252] Tax is missing for two CN exchange transactions

## 問題

@@Sang Coach Team callout 2 CN V75 store,Tax  are missing for two CN exchange transactions. I has appiled the data patch in DB.Please help to check the root cause and try to enhancement this section.Thanks!
OCF22-10189075 04-24
OCF85-00092495 04-22
Sample: OCF22-10189075 04-24
1.Before missing jouinv_vat_value & jouinv_gst_per value in DB.
2.
Excahnge memo: OCF22-10189075
Resource memo:OCF22-10188837
jouinv_misc_amt = '60'
3.FE POS capture for OCF22-10189075
1. 
5.NPOS log

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-30
### Jira Comments (9 則)
**Tovi Wang** (2025-05-08):
@@Sang 04-22 OCF22 log for your further checking.
CC @@Joy Li @@Cy Lau @@pierre.shi
**Tovi Wang** (2025-05-12):
@@Sang @@Cy Lau May I Know anything update please?
CC @@Joy Li @@pierre.shi
**Sang** (2025-05-13):
@Tovi Please get OCF85-00092495 04-22 DB and logs.
**Tovi Wang** (2025-05-13):
@@Sang Logs provided in bellow.
What DB?Dbtrans or Dbhist or Dbsse?Please confirm.
CC @@pierre.shi  Once Sang confirmed,Please help to got the info to Sang.Thanks!
**Sang** (2025-05-13):
@@Sang Got OCF22 db & Logs before. Please get OCF85 dbtrans & log also. Thanks
**Tovi Wang** (2025-05-13):
@@pierre.shi As Sang said,Please help to get OCF85 dbtrans & log also. Thanks!
**Tovi Wang** (2025-05-13):
@@Sang OCF85 04-22 details log here.
**Sang** (2025-05-13):
@@Tovi Wang @@Cy Lau @@Bobby Will be handle as Jira [🔗](https://ctil.atlassian.net/browse/FE-1514), calculate item Tax.  To be included in v750.04R13A
**Tovi Wang** (2025-05-16):
@@Bobby @@Cy Lau Please help to provide the ETA.Thanks!

## 相關資訊

- Jira: [FE-1688](https://ctil.atlassian.net/browse/FE-1688)
- Fix Version: 未記錄
- 解決日期: 2025-05-30

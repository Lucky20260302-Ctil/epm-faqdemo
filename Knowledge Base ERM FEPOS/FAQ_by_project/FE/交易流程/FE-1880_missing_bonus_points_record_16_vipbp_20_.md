---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "The memos KSSTPE05 - 00006958 to 00006961 are missing the bonus points (record 16) and bonus points "
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1880
resolved: 
fix-version: ""
---

# FE-1880: Missing Bonus Points record 16- vipbp & 20 - ptsanly

## 問題

The memos KSSTPE05 - 00006958 to 00006961 are missing the bonus points (record 16) and bonus points item earned (record 20).

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Bobby** (2026-02-09):
Attached pcd file for your reference.
**Bobby** (2026-02-09):
This is the manual fixed pcd file for your reference. @@Cy Lau @@Joy Li
**Sang** (2026-02-09):
@@Bobby this 2026.01.29 file indicated that pos version is 710.02R14zp, Jira indicate affect version is.v75. Please verify. Is this a new rule? Please copy dbtrans, dbhist.sdf, dbmas / mastconv and 2026.01.29 logs.
**Bobby** (2026-02-09):
@@Joy Li  please confirm the POS version of KSSTPE05 Till 0 and get the log files as per Sang request. Thanks.
**Joy Li** (2026-02-09):
@@Bobby @@Sang
Please found the attached zback folder from KSSTPE05 till 0.
Version is Ver. 7.1.0.02R14ZP  ImagineX
**Sang** (2026-02-09):
@@Joy Li Please copy dbtrans.sdf, dbhist.sdf and dbMas or mastconv also

## 相關資訊

- Jira: [FE-1880](https://ctil.atlassian.net/browse/FE-1880)
- Fix Version: 未記錄
- 解決日期: 未記錄

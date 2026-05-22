---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "RC1007 wasn’t checking the program with fiscal calendar."
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: BE-1063
resolved: 
fix-version: ""
---

# BE-1063: IMX Vendor Invoice Maintenance (RC1007) can not follow 

## 問題

RC1007 wasn’t checking the program with fiscal calendar.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Jerry Wong** (2025-04-29):
Release:
\\ds411\csms60\delivery\imx\rc1007.2025-04-29
**Jerry Wong** (2025-04-29):
Supplier and D/N should be matched with joupxh_supp and joupxh_date in joupxh. Then, the joupxh_date should be greater than the fiscald_date, check month end if fiscald date have not set
**Jason Wu** (2025-05-02):
@@Jerry Wong please also help to add the financial year check for these program
IC5006    	Return To Supplier Validation
IC5006    	Return To Supplier Validation
IC5009    	Return To Supplier Posting
IC5009    	Return To Supplier Posting
RC1004    	Stock Receive Validation
RC1004    	Stock Receive Validation
RC1005    	Stock Receive Posting
RC1005    	Stock Receive Posting

## 相關資訊

- Jira: [BE-1063](https://ctil.atlassian.net/browse/BE-1063)
- Fix Version: 未記錄
- 解決日期: 未記錄

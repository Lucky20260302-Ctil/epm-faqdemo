---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "select the valid account cntBVAcc02"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-786
resolved: 2023-09-07
fix-version: ""
---

# BE-786: invalid blockvote account show previous account obtained successfully instead of empty

## 問題

select the valid account cntBVAcc02
then back, leave the page, and select an invalid account
but the block vote account field remains cntBVAcc02 still.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-09-07
### Jira Comments (6 則)
**Hans Wong** (2023-08-02):
affected version v1.6 2023-08-02 and before
fix will be in v1.7 2023-08-03
**Hans Wong** (2023-08-03):
fix in [v1.7-2023-08-03](https://ctil-git.ctil.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-enterprise-management-system-frontend/-/releases/lands-uat-release-v1.7-2023-08-03)
[\\ds411\csms70\delivery\lands\UAT\Backend (Web)\2023-08-03]
ChainStorePlus-v1.7-2023-08-03.zip
**Sherman tse** (2023-09-01):
Testing result: fail
Env: 10.77.227.28 UAT
Fail to exceute balance adjustment with vaild BV account after entered into an invaild BV account
Reproduce steps:
1. 
2. 
3. 
Exsitng result:
-Cannot adjust balance of vaild account
-Cannot click on Create / debit button & field of amount
**Hans Wong** (2023-09-05):
commit as branch: BE-786-apply-2nd-fix
**Hans Wong** (2023-09-05):
[\\ds411\csms70\delivery\lands\UAT\Backend (Web)\2023-09-05]
fix released in ChainStorePlus-v1.7.3-2023-09-05.zip
**Sherman tse** (2023-09-07):
Verified on smo-pmssapp-u1 (.28) UAT

## 相關資訊

- Jira: [BE-786](https://ctil.atlassian.net/browse/BE-786)
- Fix Version: 未記錄
- 解決日期: 2023-09-07

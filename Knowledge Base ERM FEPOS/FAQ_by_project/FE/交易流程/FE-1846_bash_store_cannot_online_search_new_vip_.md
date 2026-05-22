---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Normally ,when a new customer became our VIP ,the CRM system will send  the customer information to "
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: FE-1846
resolved: 
fix-version: ""
---

# FE-1846: BASH Store cannot online search new VIP in v75

## 問題

Normally ,when a new customer became our VIP ,the CRM system will send  the customer information to BE DB ,then when we use POS to search the customer ,it can be found . By using below page . (I think it will maybe using webcall.bat or some other settings in vbretail.ini ,not sure . )
After update to V75 ,seems only could be found after integrate the zfile ,it means ,it will spend more time and must close and open the POS system ,it’s impact the staff operation.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Automation for Jira** (2026-01-06):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-01-06):
@@Angela Chan @@Andrew_Au @@Joy Li  Fixed in v750.05R04 - BASH, IMX, A+O, SPH
Program uploaded to \\ds411\share\POS_FE_Release_64\20260106 v750.05R04 - BASH IMX SPH AO

## 相關資訊

- Jira: [FE-1846](https://ctil.atlassian.net/browse/FE-1846)
- Fix Version: 未記錄
- 解決日期: 未記錄

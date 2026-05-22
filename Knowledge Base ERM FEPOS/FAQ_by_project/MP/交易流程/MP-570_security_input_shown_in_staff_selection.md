---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "<Security Flag>  = 'N' should not pop the security input"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-570
resolved: 2022-11-21
fix-version: ""
---

# MP-570: Security input shown in staff selection

## 問題

<Security Flag>  = 'N' should not pop the security input

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-11-21
### Jira Comments (6 則)
**Daniel Leung** (2022-10-12):
Security input will pop if the selected member is staff
**Andrew_Au** (2022-10-12):
Uploaded the seting name screenshot for your refernce.
**Cy Lau** (2022-10-13):
@@Andrew_Au there's no screenshot
**Andrew_Au** (2022-10-19):
Still show input staff screen when input the staff VIP in sales module, not same as the current testing POS settings behavior.
**Cy Lau** (2022-10-20):
FLAG :
**<span style="color:#de350b">EmployeePurchaseNeedSecurity</span>** == 'Y'
needs security :
"
<span style="color:#de350b">**SAL00011**</span>
"
**Andrew_Au** (2022-10-22):
MPOS
set EMPLOYEEPURCHASENEEDSECURITY = N , should not need authorized person to approval
POS set EMPLOYEEPURCHASENEEDSECURITY = Y, cannot enable authorized person input screen to approval

## 相關資訊

- Jira: [MP-570](https://ctil.atlassian.net/browse/MP-570)
- Fix Version: 未記錄
- 解決日期: 2022-11-21

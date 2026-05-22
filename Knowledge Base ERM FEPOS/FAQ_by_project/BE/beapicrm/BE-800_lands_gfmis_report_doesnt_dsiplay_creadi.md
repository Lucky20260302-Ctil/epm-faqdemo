---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "GFMIS report doesn't dsiplay creadit card (inserted by manual) payment method:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-800
resolved: 2023-10-09
fix-version: ""
---

# BE-800: [Lands] GFMIS report doesn't dsiplay creadit card (inserted by manual) payment method

## 問題

GFMIS report doesn't dsiplay creadit card (inserted by manual) payment method:
Highlighted part should be displayed Mastercard
Payment method of that record paid by Mastercard, the method is made by manual card, means mastercard's card details inserted by user.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-10-09
### Jira Comments (3 則)
**Hans Wong** (2023-09-07):
There are only 4 types for LANDS.
Cash, Cheque, Credit card and SVF (Wechat/Ali Pay).
The criteria is below:
```java
CASE
WHEN paytab.paytab_chg_flag='Y' THEN 'Cash' WHEN paytab.paytab_chg_flag='2' THEN 'Octopus' WHEN paytab.paytab_chg_flag='L' THEN 'Cheque'
WHEN (paytab.paytab_chg_flag='A' AND UPPER(paytab_s9000_type) IN ('VISA','MASTERCARD','JCB','AMEX','UNIONPAY'))
OR (paytab.paytab_chg_flag='C' AND UPPER(paytab_code) IN ('018','022')) THEN 'Credit card'
WHEN paytab.paytab_chg_flag='A' AND UPPER(paytab_s9000_type) IN ('ALIPAY','WECHAT PAY')
OR (paytab.paytab_chg_flag='C' AND UPPER(paytab_code) IN ('WEC')) THEN 'SVF'
END
```
@@Sherman tse
@@Andrew_Au
**Sherman tse** (2023-09-18):
Verified on QA env 172.16.138.55
**Sherman tse** (2023-10-09):
Verified on UAT env Lands

## 相關資訊

- Jira: [BE-800](https://ctil.atlassian.net/browse/BE-800)
- Fix Version: 未記錄
- 解決日期: 2023-10-09

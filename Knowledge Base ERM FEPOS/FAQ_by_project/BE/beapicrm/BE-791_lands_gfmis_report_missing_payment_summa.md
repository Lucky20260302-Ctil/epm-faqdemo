---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-791
resolved: 2023-09-01
fix-version: ""
---

# BE-791: [Lands] GFMIS report missing Payment Summary section

## 問題

Reproduce steps:
1. 
2. 
3. 
Existing result:
GFMIS report missing Payment Summary section (REF: RR_DCBBATCH_74_0001_20230821 (3).txt)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-09-01
### Jira Comments (5 則)
**Hans Wong** (2023-08-21):
@@Andrew_Au and @@Sherman tse FYI,
@@Jerry Wong will deliver this fix on 2023-Aug-23 AM.
And I will generate a release with [🔗](https://ctil.atlassian.net/browse/BE-789#icft=BE-789) and [🔗](https://ctil.atlassian.net/browse/BE-790#icft=BE-790) at PM for QA testing.
**Hans Wong** (2023-08-24):
The result is incorrect.
Still missing Payment Summary, which amount is group by Payment Method
and Allocation amount is group by Revenue Code
**Hans Wong** (2023-08-24):
Payment Summary SQL
```java
SELECT '74' AS 'Department Code', jouinv.jouinv_loc AS 'Collection Center Code', CONVERT(VARCHAR, jouinv.jouinv_date, 112) AS 'Collection Date', 'S' AS 'Source'
 , 'Payment Summary' AS 'DCB Description', ISNULL(salady.salady_emp_id,'') AS 'Preparer', '' AS 'Approver', salady.salady_contact_number AS 'Contact Number', jouinv.jouinv_curr AS 'Currency'
 , 'LND443' AS 'Machine/Form Number', jouinv.jouinv_gov_inv AS 'Receipt Number From', jouinv.jouinv_gov_inv AS 'Receipt Number To', '' AS 'Receipt Description', '' AS 'Cancelled Receipt Indicator', '' AS 'Cancellation Date', '' AS 'Cancellation Remarks', '' AS 'User Code', '' AS 'Allocation Description',(CASE WHEN paytab.paytab_chg_flag='Y' THEN 'Cash' WHEN paytab.paytab_chg_flag='2' THEN 'Octopus' WHEN paytab.paytab_chg_flag='L' THEN 'Cheque' WHEN paytab.paytab_chg_flag='A' AND paytab.paytab_s9000_type IN ('VISA','MASTER','JCB','AMEX','UnionPay') THEN 'Credit card' WHEN paytab.paytab_chg_flag='A' AND paytab.paytab_s9000_type IN ('ALIPAY','WECHAT PAY') THEN 'SVF' END) AS 'Payment Method', SUM(joupay.joupay_pay_amt_fx) AS 'Amount'
 FROM jouinv
 LEFT JOIN salady ON jouinv_salady_code = salady_code
 LEFT JOIN joupay on jouinv.jouinv_no = joupay.joupay_no and jouinv.jouinv_loc = joupay.joupay_loc
 LEFT JOIN paytab on joupay.joupay_pay_code = paytab.paytab_code
 WHERE jouinv.jouinv_loc = 'LBF' AND jouinv.jouinv_date BETWEEN '2023-06-01' and '2023-08-31' AND jouinv_salady_code = 'ANYLEE' and jouinv.jouinv_gov_inv is not null
 GROUP BY jouinv.jouinv_loc,jouinv.jouinv_date,jouinv.jouinv_gov_inv,salady.salady_emp_id, salady.salady_contact_number, jouinv.jouinv_curr, paytab.paytab_chg_flag, paytab.paytab_s9000_type
 ORDER BY jouinv.jouinv_loc
```
**Hans Wong** (2023-08-24):
Allocation SQL:
```java
SELECT '74' AS 'Department Code', jouinv.jouinv_loc AS 'Collection Center Code', CONVERT(VARCHAR, jouinv.jouinv_date, 112) AS 'Collection Date', 'S' AS 'Source'SELECT '74' AS 'Department Code', jouinv.jouinv_loc AS 'Collection Center Code', CONVERT(VARCHAR, jouinv.jouinv_date, 112) AS 'Collection Date', 'S' AS 'Source'                                , 'Allocation (Revenue Code)' AS 'DCB Description', ISNULL(salady.salady_emp_id,'') AS 'Preparer', '' AS 'Approver', salady.salady_contact_number AS 'Contact Number', jouinv.jouinv_curr AS 'Currency'                                , 'LND443' AS 'Machine/Form Number', jouinv.jouinv_gov_inv AS 'Receipt Number From', jouinv.jouinv_gov_inv AS 'Receipt Number To', '' AS 'Receipt Description', '' AS 'Cancelled Receipt Indicator', '' AS 'Cancellation Date', '' AS 'Cancellation Remarks', jouinv.jouinv_rev_code AS 'User Code', '' AS 'Allocation Description', SUM(joupay.joupay_pay_amt_fx) AS 'Amount'                                FROM jouinv                                LEFT JOIN salady                                ON jouinv_salady_code = salady_code                                LEFT JOIN joupay on jouinv.jouinv_no = joupay.joupay_no and jouinv.jouinv_loc = joupay.joupay_loc                                LEFT JOIN paytab on joupay.joupay_pay_code = paytab.paytab_code                                WHERE jouinv.jouinv_rev_code IS NOT NULL AND jouinv.jouinv_loc = 'LBF' AND jouinv.jouinv_date BETWEEN '2023-06-01' and '2023-08-31' AND jouinv_salady_code  = 'ANYLEE' and jouinv.jouinv_gov_inv is not null                                GROUP BY jouinv.jouinv_loc, jouinv.jouinv_gov_inv, jouinv.jouinv_date, salady.salady_emp_id, salady.salady_contact_number, jouinv.jouinv_curr, jouinv.jouinv_rev_code ORDER BY jouinv.jouinv_loc
```
**Sherman tse** (2023-09-01):
Verified on UAT 10.77.227.28

## 相關資訊

- Jira: [BE-791](https://ctil.atlassian.net/browse/BE-791)
- Fix Version: 未記錄
- 解決日期: 2023-09-01

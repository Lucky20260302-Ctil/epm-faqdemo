---
project: BE
title: "BE-791: [Lands] GFMIS report missing Payment Summary section"
issue_key: BE-791
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-791"
created: 2023-08-21
resolved: 2023-09-01
resolution: Done
has_images: False
---

# BE-791: [Lands] GFMIS report missing Payment Summary section

## 問題描述

Reproduce steps:

1. To GFMIS report (SE9999)

2. Select a date has transaction 

3. Export GFMIS report

Existing result:

GFMIS report missing Payment Summary section (REF: RR_DCBBATCH_74_0001_20230821 (3).txt)




## Jira Comments

> **Hans Wong** (2023-08-21):
>  and   FYI,  will deliver this fix on 2023-Aug-23 AM. And I will generate a release with   and   at PM for QA testing.    

> **Hans Wong** (2023-08-24):
> The result is incorrect. Still missing Payment Summary, which amount is group by Payment Method and Allocation amount is group by Revenue Code

> **Hans Wong** (2023-08-24):
> Payment Summary SQL   SELECT '74' AS 'Department Code', jouinv.jouinv_loc AS 'Collection Center Code', CONVERT(VARCHAR, jouinv.jouinv_date, 112) AS 'Collection Date', 'S' AS 'Source'
>  , 'Payment Summary' AS 'DCB Description', ISNULL(salady.salady_emp_id,'') AS 'Preparer', '' AS 'Approver', salady.salady_contact_number AS 'Contact Number', jouinv.jouinv_curr AS 'Currency'
>  , 'LND443' AS 'Machine/Form Number', jouinv.jouinv_gov_inv AS 'Receipt Number From', jouinv.jouinv_gov_inv AS 'Receipt Number To', '' AS 'Receipt Description', '' AS 'Cancelled Receipt Indicator', '' AS 'Cancellation Date', '' AS 'Cancellation Remarks', '' AS 'User Code', '' AS 'Allocation Description',(CASE WHEN paytab.paytab_chg_flag='Y' THEN 'Cash' WHEN paytab.paytab_chg_flag='2' THEN 'Octopus' WHEN paytab.paytab_chg

> **Hans Wong** (2023-08-24):
> Allocation SQL:   SELECT '74' AS 'Department Code', jouinv.jouinv_loc AS 'Collection Center Code', CONVERT(VARCHAR, jouinv.jouinv_date, 112) AS 'Collection Date', 'S' AS 'Source'SELECT '74' AS 'Department Code', jouinv.jouinv_loc AS 'Collection Center Code', CONVERT(VARCHAR, jouinv.jouinv_date, 112) AS 'Collection Date', 'S' AS 'Source'                                , 'Allocation (Revenue Code)' AS 'DCB Description', ISNULL(salady.salady_emp_id,'') AS 'Preparer', '' AS 'Approver', salady.salady_contact_number AS 'Contact Number', jouinv.jouinv_curr AS 'Currency'                                , 'LND443' AS 'Machine/Form Number', jouinv.jouinv_gov_inv AS 'Receipt Number From', jouinv.jouinv_gov_inv AS 'Receipt Number To', '' AS 'Receipt Description', '' AS 'Cancelled Receipt Indicator', ''

> **Sherman tse** (2023-09-01):
> Verified on UAT 10.77.227.28

## 相關資訊

- **Jira:** [BE-791](https://ctil.atlassian.net/browse/BE-791)
- **解決方式:** Done
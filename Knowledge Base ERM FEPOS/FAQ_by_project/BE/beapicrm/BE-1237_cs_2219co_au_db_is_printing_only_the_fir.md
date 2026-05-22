---
tags: [faq, be, beapicrm]
component: "Table"
symptom: "**CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines**"
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: BE-1237
resolved: 
fix-version: ""
---

# BE-1237: [CS-2219]CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines

## 問題

**CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines**
**Steps:**
1. 
2. 
3. 
4. 
5. 
6. 
7. 
Actual result: DB is printing only the first line of the jouinv_emarks field, ignoring the remaining lines Expected result: Remark field on DB should print all the lines given at the time of placing the order on CS2K.
Testing was conducted on **10.34.103.18** **OCFA218** (CO AU environment) under Memo Number: **00000261**.
1.FE POS Remark total 4 lines.
2.Sales receipt can normal display the 4 lines remarks.
3.I found that the maximum field limit for the jouinv_remarks field is 40 in BE DB jouinv table.
And in the BE jouinv table, there is only one remarks field.
4.But in FE DBSSE,there are total 8 remarks field.The maximum character limit for each field is 40.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Tovi Wang** (2026-03-20):
@@Jerry Wong @@Cy Lau Please help to take a look this case.I think maybe need to add remarks field in BE jouinv table.Please double check and confirm it.Thanks!
CC @@Joy Li @@Bobby

## 相關資訊

- Jira: [BE-1237](https://ctil.atlassian.net/browse/BE-1237)
- Fix Version: 未記錄
- 解決日期: 未記錄

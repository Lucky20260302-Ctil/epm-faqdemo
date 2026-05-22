---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "[INC3323035]POS V75 JP region, invalid ID could be registered as salesperson ID on CS2000 when makin"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1826
resolved: 2026-03-25
fix-version: ""
---

# FE-1826: [CS-1882] [INC3323035]invalid ID could be registered as salesperson ID on CS2000 when making transaction

## 問題

[INC3323035]POS V75 JP region, invalid ID could be registered as salesperson ID on CS2000 when making transaction。 this issue also occurred on other stores.
J804 till1, sales memo 10158519, the sales person should be 744382 ,but it shew 744282.
it shew 744282 in pos FE. We test this issue in product environment, can’t reproduce.
checked in dbmas-tblsalady, 744282 not existed.
can only find related info in T9 and PC file.
This issue occurred frequently from Oct 2025.
CC: @@Joy Li @@Tovi Wang

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-03-25
### Jira Comments (11 則)
**Tovi Wang** (2025-12-08):
Add 3 same ticket:
1.<u>[INC3337243](https://tapestry.service-now.com/incident.do?sys_id=acf6a4f747e9fa5898ab0694f16d437c&sysparm_record_target=incident&sysparm_record_row=3&sysparm_record_rows=7&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYnumber)</u>,J825，2025-12-07
2.<u>[INC3337254](https://tapestry.service-now.com/incident.do?sys_id=0707643b47e9fa5898ab0694f16d434e&sysparm_record_target=incident&sysparm_record_row=4&sysparm_record_rows=7&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYnumber)</u>,J801，2025-12-07
3.<u>[INC3337256](https://tapestry.service-now.com/incident.do?sys_id=d817283b47e9fa5898ab0694f16d430c&sysparm_record_target=incident&sysparm_record_row=5&sysparm_record_rows=7&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYnumber)</u>,J811，2025-12-07
@@Sang  Could you help to further checking this issue?
After we test in pro store,We can’t reproduce this issue in Pro store.But How input the invalid cashier ID by User?
CC @@Joy Li @@pierre.shi
**Sang** (2025-12-08):
@@Tovi Wang Can we find Staff code ‘744282’ in J804 Till 1 dbmas.[tblsalady] table?
**pierre.shi** (2025-12-10):
@@Sang can’t find Staff code ‘744282’ in Dbmas
**Tovi Wang** (2025-12-15):
JP Same issue ticket:
INC3347514,J808,2025-12-14
<u>[INC3346505](https://tapestry.service-now.com/incident.do?sys_id=7c9063219335b21008b9b22efaba100d&sysparm_record_target=incident&sysparm_record_row=9&sysparm_record_rows=14&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYnumber)</u>,J802,2025-12-14
<u>[INC3346509](https://tapestry.service-now.com/incident.do?sys_id=5990a3219335b21008b9b22efaba10e7&sysparm_record_target=incident&sysparm_record_row=10&sysparm_record_rows=14&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYnumber)</u>,J841,2025-12-13
@@Sang @@Cy Lau @@Joy Li JP experiences the same dayend issue almost every day,So could you help to take a look this issue first?Thanks!
**pierre.shi** (2025-12-22):
Below are the same issues.
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
**Automation for Jira** (2026-01-22):
Issue has been created since
Days since: 50
Week since : 7
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2026-03-06):
@@Sang May I know if anything update details for this issue?Which version will covered this issue?Please help to confirm.
CC @@Joy Li
**Sang** (2026-03-06):
@@Tovi Wang we just released v750.04R21. This issue will be included in next release R22. Will be ready for internal test next week
**Sang** (2026-03-12):
@@Sherman tse @@pierre.shi @@Tovi Wang
Enhancement included in v750.04R22
v750.04R22
1.
**Sang** (2026-03-24):
@@Sherman tse program uploaded to \\ds411\share\POS_FE_Release_64\20260324 Coach v750.04R22
Add Re-validate Sales Associate code / cashier code to prevent invalid ID be registered (KTS 260312 FE-1826 v750.04R22, v750.05R10)
1.
**Sherman tse** (2026-03-25):
Verified ok on qa with release:
\\ds411\share\POS_FE_Release_64\20260324 Coach v750.04R22 - 3
add log track the action of SA, Add Re-validate Sales Associate code / cashier code to prevent invalid ID be registered

## 相關資訊

- Jira: [FE-1826](https://ctil.atlassian.net/browse/FE-1826)
- Fix Version: 未記錄
- 解決日期: 2026-03-25

---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Tapestry’s Mason reports that he cannot see the User Password Policy and User Password Restrict Keyw"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: BE-1008
resolved: 
fix-version: ""
---

# BE-1008: BE v7 User Password Restricted Keyword and User Password Policy pointing to wrong DB. 

## 問題

Tapestry’s Mason reports that he cannot see the User Password Policy and User Password Restrict Keyword in Backend after migrated to v7. I have checked that they have the data in pwrestkw, pwpolicy and pwhistlg tables under csdata10_70 database. The data is migrated from v66 to v7. However, I checked the User Password Restricted Keyword (GL5000) and User Password Policy (GL5002) are referring to glpwrestkw, glpwpolicy and dbpwhistlg tables under gldata database. I suspect this function is whether work or not in BE v7. Could you check is there any BE function is accessing the tables in csdata database?
I expect these functions should refer to csdata database rather than gldata database. Because the policy or restricted keyword may not same for each region.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Bobby** (2025-02-21):
@@Jerry WongPlease check are there any programs referring to pwrestkw, pwpolicy and pwhistlg tables in ChainStorePlus Backend v7. We should have validation with these tables and policy when the user create or change his password in backend. User Password Restricted Keyword (GL5000) and User Password Policy (GL5002)  Please modify GL5002 and GL5000. Please give me an update on next Tuesday 25 Feb.
**Tovi Wang** (2025-02-21):
@@Bobby Many Thanks for your double confirm.
@@Jerry Wong Please help to prepare the BE release in advance.Thanks!
**Bobby** (2025-02-21):
Clarified with Jerry. the table pwrestkw and pwpolicy under csdata is referring to the Table > Secondary > Optional >
- 
- 
@@Tovi Wang Please inform Mason to check . We don’t need to fix it then.
**Bobby** (2025-02-21):
@@Tovi Wang Please close this ticket once you informed Mason. Thanks.
**Tovi Wang** (2025-02-21):
Replied the details to Mason.waiting mason double confirm the result.

## 相關資訊

- Jira: [BE-1008](https://ctil.atlassian.net/browse/BE-1008)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "@@Sang , please help to have a look at this case. This is a new sales staff member, BASH019, but I c"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1623
resolved: 
fix-version: ""
---

# FE-1623: IMX sales staff discount can not apply  

## 問題

@@Sang , please help to have a look at this case. This is a new sales staff member, BASH019, but I can not apply the discount even after changing the member type.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Jason Wu** (2025-02-11):
Log copied in \\172.16.183.201\localuser\support\20250210\IMX_case.zip
**Jason Wu** (2025-02-11):
**Sang** (2025-02-11):
@@Jason Wu Config set use calc staff limit bas on member type start date with pro-data (StaffYearLimitCalcByProRata='Y'), and the staff (Member No. BASH019) have not define member type start date. Please define BASH019 Member type start date.
**Jason Wu** (2025-02-11):
Thank you, will check with user.
**Andrew_Au** (2025-02-24):
@@Jason Wu  Please update the ticket status
**Ken Wang** (2025-02-25):
The ticket pending for a long time. Please update the ticket status.
**Andrew_Au** (2025-03-21):
@@Jason Wu The ticket pending for a long time. Please update the ticket status

## 相關資訊

- Jira: [FE-1623](https://ctil.atlassian.net/browse/FE-1623)
- Fix Version: 未記錄
- 解決日期: 未記錄

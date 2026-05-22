---
tags: [faq, fe, 系統服務]
component: "Install_Package"
symptom: "encountering printing issue after upgrade to v75.004.1100.0008."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1669
resolved: 2026-05-05
fix-version: ""
---

# FE-1669: [CS-1389]J429 printing issue after upgrade to v75.004.1100.0008

## 問題

encountering printing issue after upgrade to v75.004.1100.0008.
Previous ADK saved Devices would be inherted to [OPOS.net](http://OPOS.net)
# After checking record, ADK270JR4 should be given out on 25/12/2012 and ADK270ER5 on 25/11/2017 which would be UPOS 1.13.
# ADK280ER8, UPOS 1.14, should be given out since 26/11/2019.
# From 1.13 or previous , ModelName is not included in the configurations :
# Solutions :
Using DeviceName for matching ModelName if ModelName does not exist,
The configurations from OPSON :

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-05
### Jira Comments (4 則)
**Cy Lau** (2025-04-11):
@@Sherman tse  Please prepare a clean machine (without ADK / [OPOS.net](http://OPOS.net) installed)
install ADK270ER5 (UPOS 1.13) then set TM30 and TM88 printer
then install latest v75 via installation package to see if the device configurable inherited by OPOS.net
**Sherman tse** (2025-04-15):
The  Configuration.xml retrieve setting from ADK270 (UPOS 1.13)
Testing data: TM-T88IV
Test case attached
**Andrew_Au** (2025-08-28):
@@Sherman tse  The pending for a long time. Please update the ticket status.
**Automation for Jira** (2026-05-05):
Issue has been created since
Days since: 388
Week since : 55
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1669](https://ctil.atlassian.net/browse/FE-1669)
- Fix Version: 未記錄
- 解決日期: 2026-05-05

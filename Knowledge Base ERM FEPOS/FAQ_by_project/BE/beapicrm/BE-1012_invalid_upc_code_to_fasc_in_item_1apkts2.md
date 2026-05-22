---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "HKJC RTM reported that HKJC_FASC.exe gen_link1_skumaster interface has sent an invalid size to FASC."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1012
resolved: 2025-03-21
fix-version: ""
---

# BE-1012: Invalid UPC Code to FASC in Item 1APKTS25KDM001 Mem Bdg K-Tee plain

## 問題

HKJC RTM reported that HKJC_FASC.exe gen_link1_skumaster interface has sent an invalid size to FASC.
This is the output file HSRTM_ITEMMASTER. The item 1APKTS25KDM001 sizes is invalid and I suspect they are carried forward from last created item and somehow updated into “edisku” table. The correct size category should be “KDS” instead of “SML”.
I found the user was created 1APLTS25KDM002 which size category is SML, and then 1APKTS25DM001 which size category is KDS. However, it inserted the SML sizes to “edisku” table. So that the HSRTM_ITEMMASTER interface exported the wrong size to FASC. I believe the user may create these items continuously without quit the maintenance and cause this problem. Please try to reproduce it and fix the problem.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-21
### Jira Comments (3 則)
**Bobby** (2025-02-27):
@@Jerry Wong Please try to reproduce the case first and list out the procedure by this week.
**Andrew_Au** (2025-03-21):
@@Jerry Wong The ticket pending for a long time. Please update the ticket status
**Bobby** (2025-03-21):
We have already identified the root cause. Jerry has fixed the Item Master Maintenance. I have already delivered to HKJC for testing. So this ticket can be closed.

## 相關資訊

- Jira: [BE-1012](https://ctil.atlassian.net/browse/BE-1012)
- Fix Version: 未記錄
- 解決日期: 2025-03-21

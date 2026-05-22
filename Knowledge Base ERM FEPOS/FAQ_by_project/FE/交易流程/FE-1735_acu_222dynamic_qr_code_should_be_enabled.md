---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Dynamic QR Code should be disabled for other regions: HK/MO/TW/SG/MY/KR.,"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1735
resolved: 2025-07-31
fix-version: ""
---

# FE-1735: [ACU-222]Dynamic QR Code should be enabled for MLC only

## 問題

Dynamic QR Code should be disabled for other regions: HK/MO/TW/SG/MY/KR.,

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-31
### Jira Comments (6 則)
**Joy Li** (2025-07-24):
Copy from Sang message:
1. 
'Y'- Validate ACXIOM Member QR Code token (Coach CN InternalCompanyCode=11 must set 'Y')
**Daniel Leung** (2025-07-24):
MPOS API uploaded to \\ds411\share\POS_MPOS_Release\3.30.x\3.30.3-20250724.1  @@Joy Li @@Tovi Wang @@Sherman tse
**Joy Li** (2025-07-24):
@@Daniel Leung Sherman, could you please arrange the testing for MPOS API
**Joy Li** (2025-07-31):
released package to TP on 2025-07-31
FE: 75.004.1307.0000
MPOS 3.30.4
**Automation for Jira** (2025-07-31):
Issue has been created since
Days since: 6
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2025-07-31):
Verified on QA
Test case attached

## 相關資訊

- Jira: [FE-1735](https://ctil.atlassian.net/browse/FE-1735)
- Fix Version: 未記錄
- 解決日期: 2025-07-31

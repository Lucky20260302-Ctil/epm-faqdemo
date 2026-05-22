---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "KSJ MPOS v3.29.6. Employee Member able to select but when go to payment page, it will show below err"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-783
resolved: 2025-07-04
fix-version: ""
---

# MP-783: [MPOS-104]KSJ MPOS - v3.29.6 IPA employee purchase unavailable

## 問題

KSJ MPOS v3.29.6. Employee Member able to select but when go to payment page, it will show below error( same error message as [MPOS-101](https://jira.tapestry.support/browse/MPOS-101)):
Testing info:
Testing machine IP: 172.24.253.69(C309) - connect to apawiqwposweb01, UI log uploaded.
IPA Version: v3.29.6
API Version: COACH_MPOSWebAPI_R3.29.5f
Testing Employee vip no: 205655

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-04
### Jira Comments (4 則)
**Tovi Wang** (2025-06-30):
@@Joy Li @@Daniel Leung MPOS log and UI log uploaded in attachments.
**Daniel Leung** (2025-06-30):
Seems a bug in MPOS. Hot fix version in [🔗](https://ios.ctil.com/mpos/PreCoach/)  - 3.29.6-20250630.1 @@Joy Li @@Tovi Wang
**Sherman tse** (2025-07-03):
Excuted a regression test with ipa version: 3.29.6-20250703.1
**Joy Li** (2025-07-04):
The issue is included in MPOS IPA 3.29.6-20250703.1 which released on 2025-07-04.

## 相關資訊

- Jira: [MP-783](https://ctil.atlassian.net/browse/MP-783)
- Fix Version: 未記錄
- 解決日期: 2025-07-04

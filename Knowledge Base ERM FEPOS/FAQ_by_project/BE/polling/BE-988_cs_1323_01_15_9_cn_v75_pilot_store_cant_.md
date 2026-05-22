---
tags: [faq, be, polling]
component: "polling"
symptom: "SOG call out 01-15 CN pilot store can’t upload sales to BE."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-988
resolved: 2025-02-21
fix-version: ""
---

# BE-988: [CS-1323] - 01-15 9 CN V75 pilot store can't upload ACP data file to BE- RIN01442452

## 問題

SOG call out 01-15 CN pilot store can’t upload sales to BE.
troubleshooting:
1.Check cs2kconnect.ini config is correct.cs2k log NOT have error and can normal find ACP data file.
2.Check sqlpcdossa & sqlpcdossb table,Just only find OC185,OC182,OC270 3 store’s acp file upload to BE.
3.Check polling log also NOT have error and can find OC185 ACP file.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-21
### Jira Comments (5 則)
**Tovi Wang** (2025-01-16):
@@Cy Lau Xconfig for your double check.
**Tovi Wang** (2025-01-16):
@@Cy Lau polling & posting exe for your reference
**Tovi Wang** (2025-01-16):
**Tovi Wang** (2025-01-17):
@@Cy Lau 01-16 OSSB logs for your reference.
**Sherman tse** (2025-02-21):
Side effect of the OSS issue, verified on ticket [🔗](https://ctil.atlassian.net/browse/BE-1004)
Close the ticket

## 相關資訊

- Jira: [BE-988](https://ctil.atlassian.net/browse/BE-988)
- Fix Version: 未記錄
- 解決日期: 2025-02-21

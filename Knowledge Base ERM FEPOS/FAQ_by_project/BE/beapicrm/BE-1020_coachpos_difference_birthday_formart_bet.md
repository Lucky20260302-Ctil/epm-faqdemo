---
tags: [faq, be, beapicrm]
component: "MPOS"
symptom: "[Coach][POS] Difference birthday formart between HK and CN"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1020
resolved: 2025-04-29
fix-version: ""
---

# BE-1020: [Coach][POS] Difference birthday formart between HK and CN

## 問題

[Coach][POS] Difference birthday formart between HK and CN
HK: July
CN: 2021/07/06
Please help to confirm which Birthday format is correct & help to check if the birthday formart affected by config, thanks
Testing data: 13761555153 from CRM member

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-04-29
### Jira Comments (2 則)
**Sang** (2025-03-04):
@@Sherman tsedepend on  tblconfig.ShowFullBirthday.  ‘Y' - Show full birthday ‘yyyy/MM/dd’; 'N’ show birthday Month only
**Sherman tse** (2025-04-29):
FE can show birthbay month only by setting config.
Close case

## 相關資訊

- Jira: [BE-1020](https://ctil.atlassian.net/browse/BE-1020)
- Fix Version: 未記錄
- 解決日期: 2025-04-29

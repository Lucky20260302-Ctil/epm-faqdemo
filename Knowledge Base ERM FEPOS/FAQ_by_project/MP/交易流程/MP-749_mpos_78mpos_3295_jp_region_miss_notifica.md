---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "during testing for MPOS IPA 3.29.5 20250212.1, for JP region, MPOS Miss notification under tax free "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-749
resolved: 2025-05-02
fix-version: ""
---

# MP-749: [MPOS-78]MPOS 3.29.5  - JP region - Miss notification under tax free module if the price is lower than 5000JPY

## 問題

during testing for MPOS IPA 3.29.5 20250212.1, for JP region, MPOS Miss notification under tax free module. if the price is lower than 5000JPY, should have below notification under payment page. BTW, we confirmed CS2K no such issue.
Testing info:
Testing machine IP: 172.24.253.20(J805)
any item price under 5000JPY, any member, under tax free module.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (5 則)
**Cy Lau** (2025-02-26):
@@Daniel Leung  PLEASE check if did called 
***IsValidTaxFree*** api
**Daniel Leung** (2025-02-27):
Popup displayed correctly
**Daniel Leung** (2025-02-27):
@@Tovi Wang Can you get the MPOS log and MPOS API log?
**Andrew_Au** (2025-03-21):
@@Daniel Leung The ticket pending for a long time. Please update the ticket status
**Sherman tse** (2025-05-02):
This issue has closed in Tapestry side JIRA, with reason:
Confirmed it's not the issue. The system will only check the list price, not the amount after discount.
For the details, please refer to [https://jira.tapestry.support/browse/MPOS-78](https://jira.tapestry.support/browse/MPOS-78)
Close case

## 相關資訊

- Jira: [MP-749](https://ctil.atlassian.net/browse/MP-749)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

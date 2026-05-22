---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "Q1 , does the listing have the indicator ?(As I rmb , nope ?)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-738
resolved: 2025-06-05
fix-version: ""
---

# MP-738: [MPOS-68] MPOS_3.29.4-20241204.1 Didn't show Line bind indicator(For JP Region)

## 問題

Q1 , does the listing have the indicator ?(As I rmb , nope ?)
Q2 Details page 100% sure missed - owing to MPOS itself or API ?

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-06-05
### Jira Comments (10 則)
**Cy Lau** (2024-12-13):
Investigation on 13-Dec
**Cy Lau** (2024-12-13):
\\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20241212.1b1
release note :
1.
**Cy Lau** (2024-12-13):
Testing Data :
DB : .8
@@Daniel Leung 
@@Sherman tse 
@@Jason Wu
**Daniel Leung** (2024-12-16):
new ipa on Pre-Coach : 3.29.5-20241216.1:
-bug fix: passing correct parameter to member detail to trigger getMembers api
**Daniel Leung** (2024-12-16):
With new API and IPA, Line Bind label can be displayed.
**Cy Lau** (2024-12-17):
Recap for Release:
MPOS API - 3.29.5-20241212.1b1 :
\\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20241212.1b1
release note :
1. 
---
MPOS - 3.29.5-20241216.1:
[🔗](https://ios.ctil.com/mpos/precoach/) 
release note :
Member Details Page:
-bug fix: passing correct parameter to member detail to trigger getMembers api
**Andrew_Au** (2025-02-21):
@@Sherman tse  Please update the ticket status
**Andrew_Au** (2025-02-21):
@@Sherman tse Please update the ticket status
**Sherman tse** (2025-02-21):
Verfied on QA
test case attached
**Andrew_Au** (2025-02-21):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [MP-738](https://ctil.atlassian.net/browse/MP-738)
- Fix Version: 未記錄
- 解決日期: 2025-06-05

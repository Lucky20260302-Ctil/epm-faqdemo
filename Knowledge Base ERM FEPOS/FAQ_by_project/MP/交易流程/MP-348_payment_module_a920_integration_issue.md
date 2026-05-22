---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "# 1. Missing time remain in all sessions"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-348
resolved: 2021-07-20
fix-version: ""
---

# MP-348: Payment Module - A920 Integration issue

## 問題

# 1. Missing time remain in all sessions
Sample screen:
For example after wipe credit issue memo card screen, void memo screen etc.
# 2. A920 cancel order handling
A920 click back button to cancel order processing, app will display [error 400 ?????????]
**
# 3. A920 ordering timeout display
A920 keep waiting without further action, app display [error 400 ??????]
# 4.    Not support Issue memo with Multi-ECR Payment
# Issue sales memo with two ECR Payments, but combine into one
1) ** Input one 500 ECR Payment on 4480 sales memo
2) Payment remain amount 3980 and confirm
3) But two ECR Payments auto combine into one ECR Payments
(Refer screen for two or more ECR Payments)
# 5.    ECR Void Result layout
The wording “Result” split to two rows to display

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-07-20

## 相關資訊

- Jira: [MP-348](https://ctil.atlassian.net/browse/MP-348)
- Fix Version: 未記錄
- 解決日期: 2021-07-20

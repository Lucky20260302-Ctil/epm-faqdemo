---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "When issuing a return memo, the option to print QR code will appear IF there is an original sales me"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-534
resolved: 2024-07-10
fix-version: ""
---

# MP-534: Print QR Code option appears when issuing return memo

## 問題

When issuing a return memo, the option to print QR code will appear IF there is an original sales memo inputted. It doesn't matter if the original sales memo has QR code on it or not.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-07-10
### Jira Comments (2 則)
**Cy Lau** (2022-06-23):
bug fix version is on
[https://ios.ctil.com/mpos/dev/](https://ios.ctil.com/mpos/dev/)
version:
v3.18.0-20220623.1
if return goods  - amt < 0 , it will not ask about the QR printing
**Andy Ko** (2022-06-27):
Hi @@Cy Lau , noted. Do you also have the update for Android as well? Thanks!

## 相關資訊

- Jira: [MP-534](https://ctil.atlassian.net/browse/MP-534)
- Fix Version: 未記錄
- 解決日期: 2024-07-10

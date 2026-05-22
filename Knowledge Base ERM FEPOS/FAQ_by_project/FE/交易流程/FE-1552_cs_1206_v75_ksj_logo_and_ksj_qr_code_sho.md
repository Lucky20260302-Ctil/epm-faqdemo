---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "V75"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1552
resolved: 2024-11-29
fix-version: ""
---

# FE-1552: [CS-1206] V75 - KSJ logo and KSJ QR code showing up in receipt

## 問題

V75
testing PC: 172.16.138.34
Test step: create one normal sales and print the receipt After printing, find there is no KSJ logo on the top of the receipt, there is no QR code on the bottom of the receipt, only can show the tax number, and the format is not correct.
v75 screen
should be:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-29
### Jira Comments (4 則)
**Sang** (2024-11-12):
use 172.16.138.34 db can show logo and qr code.  Please note that only 'Customer copy' need toJoy print Logo and QR code.
**Andy Ko** (2024-11-14):
tested TM-m30 printer on 172.16.138.34 VM. Printout was correct and included QR code and header logo.
**Joy Li** (2024-11-29):
FE-V750.04R09B (v75.004.0902.0000) is released 2024-11-21 By Joy
**Joy Li** (2024-11-29):
FE-V750.04R09B-2 (v75.004.0902.0002) is released 2024-11-29 By Joy

## 相關資訊

- Jira: [FE-1552](https://ctil.atlassian.net/browse/FE-1552)
- Fix Version: 未記錄
- 解決日期: 2024-11-29

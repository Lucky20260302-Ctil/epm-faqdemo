---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "To improve store productivity, Steven request to remove below pop up screen and make it default to p"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1709
resolved: 2025-06-25
fix-version: ""
---

# FE-1709: [CS-1450]New request_CN_Remove Einvoice pop up window

## 問題

To improve store productivity, Steven request to remove below pop up screen and make it default to printer einvoice qr code in receipt.
please kindly have a look whether it can be managed by xconfig level change or need program level change.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-06-25
### Jira Comments (5 則)
**Tovi Wang** (2025-06-04):
@@Sang @@Cy Lau As talked in teams.Please help to take a look Steven’s request.Please help to prepare the Xconfig for defaut printing CN E-invoice.Thanks!
CC @@Joy Li @@Bobby
**Tovi Wang** (2025-06-04):
@@Cy Lau Coach team只是想有一个Xconfig来control 下面这个弹窗，就是不弹出下面这个弹窗，默认打印CN E-invoice.
Enable E-invoice → Yes
Popout follow info --->NO
**Sang** (2025-06-05):
@@Tovi Wang @@Cy Lau @@Bobby @@Joy Li need program level change, Please confirm
**Sherman tse** (2025-06-23):
Verified on QA
test case attached
**Joy Li** (2025-06-25):
released to TP on 2025-06-25 with CS2000Patch_75.004.1303.0000.exe

## 相關資訊

- Jira: [FE-1709](https://ctil.atlassian.net/browse/FE-1709)
- Fix Version: 未記錄
- 解決日期: 2025-06-25

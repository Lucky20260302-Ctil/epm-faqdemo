---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "When we are doing the store visit, we hear about the request from store that they don't want to have"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-781
resolved: 2025-07-17
fix-version: ""
---

# MP-781: [MPOS][CS-1463] New Request for Reprinting receipt

## 問題

When we are doing the store visit, we hear about the request from store that they don't want to have both store and customer receipt for reprinting from outlet.
but for retail, we need to have both store and customer in receipt.
for TMU, we'd like to have 3 options by xconfig as only store receipt, only customer receipt and both store and customer receipt.
The enhancement would be happened for TMU and Re-printing functions only
*This reprint enhancement cover all Coach execpt CoachJP

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-17
### Jira Comments (4 則)
**Cy Lau** (2025-06-30):
@@Daniel Leung  
the patch has been applied to 3.29.x
svn://sanyosvn.ctil.com/svn/SvnPepository/branches/mPOS WebAPI/3.29.X
#1 Please do the unit test and build for release
#2 Apply the patch to 3.30.x
**Sherman tse** (2025-07-16):
Verified on QA
test case attached  
MPOS-IPA- 3.30.3 -20250703.1
\\ds411\share\POS_MPOS_Release\3.30.x\3.30.3-20250709.1
**Joy Li** (2025-07-17):
@@Ken Wang  is released on 2025-07-16
**Joy Li** (2025-07-30):
Prepare Local IIS package to TP and release on 2025-07-30.

## 相關資訊

- Jira: [MP-781](https://ctil.atlassian.net/browse/MP-781)
- Fix Version: 未記錄
- 解決日期: 2025-07-17

---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "For JP Local IIS, no matter we enable the e-receipt or not, after we void sales memo, it should prin"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-754
resolved: 2025-10-09
fix-version: ""
---

# MP-754: [MPOS-81] MPOS 3.29.5 - JP Local IIS, invalid pop-up window for Void function

## 問題

For JP Local IIS, no matter we enable the e-receipt or not, after we void sales memo, it should print out directly, should not pop-up below window, kindly help to check. I've attached Cloud IIS Recording(No such issue) & Local IIS Recording for your ref..
IPA: MPOS v3.29.5 20250212.1
API: WebAPI_v30.0029.0500.zip
Testing machine: 172.24.253.16(J406) - **Local IIS**
Troubleshooting:
1.double checked Dbtrans config NOT found relates xconfig.
2.Double checked Till0 DBsse tblconfig NOT found relates xconfig.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-10-09
### Jira Comments (10 則)
**Tovi Wang** (2025-03-05):
@@Daniel Leung 首先我先确认一个问题哈。Coach JP store（Local IIS）启用Ereceipt后，Void 小票是不弹出下面这个提示的嘛？有没有Xconfig来控制呀？
根据Coach team反馈说启用后，正常的MPOS销售是会弹出下面这个提示的，但是Viod memo时不应该弹出这个提示，而是应该直接print out小票。Please help to clarify.Thanks!
CC @@Bobby @@Cy Lau
**Daniel Leung** (2025-03-05):
@@Tovi Wang Please check printReceiptFlow in dbCoachLocal.db. 
set to 0(default) will display printing popup
set to 1 will print then send eReceipt
**Tovi Wang** (2025-03-05):
Update a new found:
我刚才在QA POS 前台测了，创建正常销售单时，是会弹出Ereceipt提示，Void memo时是直接打印小票不会弹出Ereceipt提示。
**Tovi Wang** (2025-03-05):
**Daniel Leung** (2025-03-06):
@@Tovi Wang  Hot fix version uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)  - 3.29.5-20250305.1
**Tovi Wang** (2025-03-06):
@@Daniel Leung Many Thanks!
@@Bobby @@Jason Wu Please help to passed the hot fix to QAQC testing.Thanks!
**Sherman tse** (2025-03-17):
Verified on QA with 3.30.2-20250314.1
Test Case attached
**Tovi Wang** (2025-03-20):
1.Go to mpos api server
2.Open iis
1. 
1. 
1.
**Andrew_Au** (2025-09-30):
@@Tovi Wang  Please update the status
**Tovi Wang** (2025-10-09):
Fixed,Please closed.

## 相關資訊

- Jira: [MP-754](https://ctil.atlassian.net/browse/MP-754)
- Fix Version: 未記錄
- 解決日期: 2025-10-09

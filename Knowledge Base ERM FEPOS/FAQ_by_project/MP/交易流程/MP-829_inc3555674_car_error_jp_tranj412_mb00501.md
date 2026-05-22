---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "The correct total amount should be ‘27500' instead of '33000’ for memo J412-MB005013 on2026-04-23.Th"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: MP-829
resolved: 
fix-version: ""
---

# MP-829: INC3555674 - CAR Error - JP-tran#J412-MB005013 Sum of item does not equal the payment sum 04/23

## 問題

The correct total amount should be ‘27500' instead of '33000’ for memo J412-MB005013 on2026-04-23.The Coupon LPB001D 5500 amount NOT synced to the sales memo.
1.
2.FE POS:
3.DB data for the sales memo:
4.
ALL Local IIS
POS version 75.004.1404.0000
MPOS version:3.30.3

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Tovi Wang** (2026-04-24):
**Tovi Wang** (2026-04-27):
1.INC3559714,Same issue J361-MC002080
**Joy Li** (2026-04-27):
@@Tovi Wang Please also provide the logs from local IIS up to **Retdata6** (local IIS writes logs to Retdata6).
@@Daniel Leung The issue is suspected to be caused by the member not being found during the payment process. As a result, the coupon may disappear during payment. Could you please compare the V75 source with MPOS?
cc @@Cy Lau
**Automation for Jira** (2026-04-27):
Issue has been created since
Days since: 3
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Daniel Leung** (2026-04-27):
@@Tovi Wang Can you also get MPOS UI log ? only found MPOS api log in your uploaded file
**Tovi Wang** (2026-04-27):
@@Joy Li @@Daniel Leung Retdata6 log here for your further checking.
**Tovi Wang** (2026-04-27):
@@Daniel Leung I had let SOG team help to upload the MPOS UI log.
**Tovi Wang** (2026-04-28):
@@Daniel Leung J412 all MPOS UI log here.Please further checking.
**Daniel Leung** (2026-04-28):
@@Tovi Wang No `MB005013` or any MB Till found in UI logs. Please upload MB till for further checking
**Tovi Wang** (2026-05-21):
Same issue INC3597075 happend again.Waiting SOG team upload MPOS UI logs.
J412 - MG001445 on 2026-05-20

## 相關資訊

- Jira: [MP-829](https://ctil.atlassian.net/browse/MP-829)
- Fix Version: 未記錄
- 解決日期: 未記錄

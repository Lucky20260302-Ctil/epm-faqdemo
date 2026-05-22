---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Dear ALL,"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1684
resolved: 
fix-version: ""
---

# FE-1684: [CS-1419] 75 - not able to select CDP coupon during deposit settlement

## 問題

Dear ALL,
Testing QA : OCQA1-0        10.33.248.4
1.deposit memo: 00000584  created on 2025-04-29.
With CDP coupon phone no:15008476947
Member NO: OCQA1TC00000091
2.选择"F1-结算"，跳到payment 界面后不会自动弹出 CDP coupon.
3.选择 “F2-修改”，跳到deposit主界面，点击“支付”;
4.点击“支付”button，跳到payment界面后，这时会自动弹出 “您要选择电子优惠券吗？”
5.点击“确认”后，可以看到并且选择会员优惠券。
6.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2025-04-29):
@@Anson Cheung
I can reproduce this issue in QA.Please help to further checking and enhance this section.
CC @@Joy Li @@Cy Lau
**Tovi Wang** (2025-04-29):
Web22 QA CRMBEAPI log here
**Sang** (2025-04-30):
@@Tovi Wang @@Cy Lau Need to enhance program, will be included in next release v750.04R12B.
**Tovi Wang** (2025-05-15):
@@Sherman tse @@Joy Li @@Sang  If we tested & passed this issue before released?Yoyo said the issue still in POS version **75.004.1300.0000,Could you help to double check and confirm?Thanks!**
Tel no:18201702697
**Tovi Wang** (2025-08-29):
Confirmed this issue is fixed in QA by new release V75.004.1300.0000.

## 相關資訊

- Jira: [FE-1684](https://ctil.atlassian.net/browse/FE-1684)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "WECHAT Coupon -$100 counted as 2 time causing the incorrect GST amount"
root-cause: "待提取"
solution: "### Jira Comments (22 則)"
jira: FE-1620
resolved: 
fix-version: ""
---

# FE-1620: [CS-1082] Issue_CN_INC2579616_Tax variance for OC183 – 10008908 (incorrect VAT & GST amount)

## 問題

WECHAT Coupon -$100 counted as 2 time causing the incorrect GST amount
OC183- 10008908
Found log & data in \\172.16.183.201\localuser\support\^^DiscountVariance_2024\
POS Version Ver. 7.2.0.02R23E

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (22 則)
**Sherman tse** (2025-02-03):
I will try to reproduce the issue in our qa env later
**Tovi Wang** (2025-02-05):
@@Sherman tse  Many Thanks for your support.
**Tovi Wang** (2025-02-06):
@@Sang Could you help to take a look this VAT & TAX issue if can be covered in R10?Thanks!
**pierre.shi** (2025-02-06):
Hi Teams, this issue occurred again:OC131-00023592.
**Sang** (2025-02-11):
@@pierre.shi I can’t re-produce OC183 – 10008908 case. Regarding OC131-00023592, please get all logs from OC131. thanks
**Sang** (2025-02-11):
@@pierre.shi @@Cy Lau @@Sherman tse only one E-coupon found in db. But from NPOS log,  seems same coupon have  been applied two time.  @@pierre.shi Regarding OC131-00023592, please get all logs, dbtrans.sdf and dbmas or mastconv.dat also.
**pierre.shi** (2025-02-12):
Hi @@Sang  logs have been uploaded as attachment.
**Sang** (2025-02-14):
@@pierre.shi please help to get one set of mastconv files to build dbmas. Thx
**pierre.shi** (2025-02-14):
Hi @@Sang dbmas has been uploaded as attachment.
**Sang** (2025-02-17):
@@pierre.shi where is dbmas ?
**pierre.shi** (2025-02-17):
Hi @@Sang I have re-uploaded the dbmas again, maybe not successfully upload last time.
**Sang** (2025-02-20):
@@pierre.shi Can’t find dbmas in attachment. Please upload again.
**pierre.shi** (2025-02-24):
Hi @@Sang  dbmas has been uploaded.
please follow onedrive path:[20250224-OC131dbmas](https://ctil00046-my.sharepoint.com/:f:/g/personal/jason_wu_ctil00046_onmicrosoft_com/ElXByiB0rEhKvnyt-69eznkBYC9xhbgYXPvhVSfVFWvZJw?e=VCG2NH)
**Ken Wang** (2025-02-25):
The ticket pending for a long time. Please update the ticket status
**Tovi Wang** (2025-03-03):
@@Sang  Could you got the Dbmas now?Let me know the update.Because same issue still happenning.Thanks!
**Andrew_Au** (2025-03-21):
@@Tovi Wang @@pierre.shi  The ticket pending for a long time. Please update the ticket status
**Tovi Wang** (2025-03-21):
@@Sang May I know anything update please?
CC @@Bobby @@Cy Lau
**Sang** (2025-05-15):
@@Tovi Wang can’t re-produce in v7202.02R23 and v750.04R13
cc @@Bobby @@Cy Lau
**Tovi Wang** (2025-05-16):
@@Sang So how do we replied to Coach team?Thanks!
CC @@Joy Li @@Bobby @@Cy Lau
**Tovi Wang** (2025-05-30):
Dear ALL,
Because can’t reproduce  in v7202.02R23 and v750.04R13，We will keep monitoring this issue with Coach team.
Ticket hold on!
**Andrew_Au** (2025-08-28):
@@Tovi Wang @@Joy Li The ticket hold for a long time. Could you confirm the ticket current status.
**Tovi Wang** (2025-08-29):
Coach Team Testing is passed, but not deployed to PRD yet,Closed first.

## 相關資訊

- Jira: [FE-1620](https://ctil.atlassian.net/browse/FE-1620)
- Fix Version: 未記錄
- 解決日期: 未記錄

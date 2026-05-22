---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Store user has some problem with mpos"
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: MP-753
resolved: 
fix-version: ""
---

# MP-753: [RIN01454411]JP - J355  - Mpos : when user enter sales staff/cashier information, the mpos always keep loading

## 問題

Store user has some problem with mpos
Symptom:
1. 
Software Version:
IIS: Cloud
IIS Version: 72.0225.0004
MPOS Version: 3.25.1
Troubleshooting:
A. user said the issue often appear on all mpos and they need to reboot the mpos and register the information again.
B. guide user to turn off/on the SDAS01 but issue still.
C. other function like scan the sku or search customer is ok.
1. ,MPOS logs for your further checking.
2.Issue Vedio from store.
3.@@Daniel Leung @@Cy Lau From UI log &,I can see that there are some time no log.Could you help to double check why there are keep loading when user enter staff code&cashier code?What’s the details logic of enter staff code&cashier code?the code info come from Till0 dbsse?Please help to clarify.Thanks!

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Tovi Wang** (2025-03-07):
@@Daniel Leung @@Bobby
这个是03-06的最新录屏。03-06的MPOS log正在copy.
目前J355店铺call上来2个问题：
一:   2月18日：用户在输入账号之后长时间loading。
二：3月6日：用户在输入账号之后MPOS仍然要求店铺再次输入账号，多次尝试输入账号后还是提示没有输入账号（参考下图）。请帮忙calarify输入staff code/Cashier code背后的逻辑以及root cause?Thanks!
**Bobby** (2025-03-07):
@@Daniel Leung @@Cy Lau Uploaded screen capture for your reference.
**Bobby** (2025-03-07):
**Bobby** (2025-03-07):
@@Tovi Wang ,, Explained to Daniel. He will follow up this case after he finished his on-hand urgent cases.
**Tovi Wang** (2025-03-07):
@bobby @@Daniel Leung Many Thanks!waiting for your new found.
CC: @@pierre.shi FYI.
**Tovi Wang** (2025-03-11):
@@Daniel Leung @@Bobby May I know anything update?Thanks!
**Daniel Leung** (2025-03-11):
@@Tovi Wang I suspect it is a network issue. UI refreshed before receiving staff data. 
Can you try the following step to test:
Test A:
1. input sales staff
2. wait until sales label appear
Test B:
1. 
2. 
Test B should trigger this issue and Test A will not.
Please let me know the result. Thank you
**Tovi Wang** (2025-03-12):
[dbMas].[dbo].[TblSalady]
**Tovi Wang** (2025-03-18):
It is caused by Network issue.Can be closed first.

## 相關資訊

- Jira: [MP-753](https://ctil.atlassian.net/browse/MP-753)
- Fix Version: 未記錄
- 解決日期: 未記錄

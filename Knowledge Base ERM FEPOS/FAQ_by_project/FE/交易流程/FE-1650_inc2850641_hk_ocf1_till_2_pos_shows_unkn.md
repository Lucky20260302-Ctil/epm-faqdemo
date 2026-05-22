---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Till 2 POS shows 'unknown error' when scanning alipay QR code,other tills is normal for the same sto"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1650
resolved: 
fix-version: ""
---

# FE-1650: [INC2850641] HK OCF1 Till 2 POS shows "unknown error" when scanning alipay QR code

## 問題

Till 2 POS shows "unknown error" when scanning alipay QR code,other tills is normal for the same store.
Store user has some problem with
Symptom:
1. 
Device & Network Information:
PC name: 2

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Tovi Wang** (2025-03-14):
@@Sang @@Cy Lau Payment log & T9 log for your further checking,Please help to check the RCA and workaround.Thanks!
CC @@Sherman tse @@pierre.shi
**Sang** (2025-03-17):
@@Tovi Wang @@Cy Lau
Error Return from EFT API[11/03/2025 14:58:20 -4933]: [20250311 02:58:20]  : Request-Result:
[11/03/2025 14:58:20 -4933]: [20250311 02:58:20]  : Request-ResponseCode:-98
[11/03/2025 14:58:20 -4943]: [20250311 02:58:20]  : Request-ResponseMsg:Unknown error (不知名錯誤)
Try to find last success EFT Ali/Wechat payment on Till 2.
**Tovi Wang** (2025-03-17):
@@Sang Alipay 在 till2没有成功过，我查了DB Till2 没有Alipay 的销售。
从下面的jietu可以确认error是来自EFT API?right?如果是这样，我让Coach去找ALipay side查下为什么会return error给我们？Please advice.Thanks!
**Sang** (2025-03-17):
如till 2未曾有eft Alipay or  wechat 收款記錄，可能eft config 或eft 機有問題，請coach 找eft的人來檢查吧
Get Outlook for iOS<[https://aka.ms/o0ukef](https://aka.ms/o0ukef)>
**Tovi Wang** (2025-03-17):
@@Sang  Many Thanks for your double confirm.Updated the details to coach team.waiting their result.
**Tovi Wang** (2025-04-15):
Dear Team,
The root cause is program can't access/edit the registry file, and needs to revise the permissions.This issue has been solved, it is working after adding follow permissions.
Please follow the quick guide below, and then try again. Thanks.
1. 
1. 
1. 
1. 
1. 
1.

## 相關資訊

- Jira: [FE-1650](https://ctil.atlassian.net/browse/FE-1650)
- Fix Version: 未記錄
- 解決日期: 未記錄

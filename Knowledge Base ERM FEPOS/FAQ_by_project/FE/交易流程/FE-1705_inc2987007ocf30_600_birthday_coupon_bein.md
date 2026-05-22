---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "@@Sang @@Anson Cheung  As talked in teams."
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: FE-1705
resolved: 
fix-version: ""
---

# FE-1705: [INC2987007]OCF30 600 birthday coupon being used but not affecting

## 問題

@@Sang @@Anson Cheung  As talked in teams.
Coach callout one redeem CDP coupon issue.
Details as follow:
When user inputting 600 birthday coupon and ready to check out, POS crashed memo not being made yet, but the coupon count as used on customer's end.After POS crashed, no error pops out.
Member info:
何小姐
member number: OCF300C00028105
phone number: 13250128864
time of this transaction: 20250521 14:57
memo number: OCF30 30020278
1. 
查询T9 log 发现在 20250521 14:44:49 coupon no 1517459124381499081 已经被成功核销了。
但是POS在这个时候好像突然闪退了并且没有error,
紧接着店铺在 20250521 14:45:23 又restart CSPLUS 重新录入销售。发现此会员的CDP coupon已经被核销了。这个case大家有什么建议嘛？is it a normal workflow?How to avoid same issue happend again?Thanks!
CC @@Joy Li @@Cy Lau
[20250521 14:43:09 -4683]: doECoupon()
[20250521 14:43:09 -4683]: Member coupon is found: 1
[20250521 14:43:11 -3565]: Process_Payemnt_Type - Start : CSH - 现金 : Avail V.  Memory : 140731703.599
[20250521 14:43:11 -3574]: Process_Payemnt_Type - End : CSH - 现金 : Avail V.  Memory : 140731703.599
[20250521 14:44:42 -7523]: Process_Payemnt_Type - Start : CC - 银行卡 : Avail V.  Memory : 140731706.687
[20250521 14:44:44 -2692]: Process_Payemnt_Type - End : CC - 银行卡 : Avail V.  Memory : 140731700.388
[20250521 14:44:49 -3838]:  Online redeem CDP Discount coupon 1517459124381499081 - success
**[20250521 14:44:49 -3946]: doCommit**
**[20250521 14:45:23 -0693]: doBootstrap.Start**
[20250521 14:45:23 -5536]: DeveloperMode Init
[20250521 14:45:23 -5556]: PCD Init
[20250521 14:45:23 -5576]: Cashier Init
[20250521 14:45:23 -5586]: POSInfo Init
[20250521 14:45:23 -5606]: SystemDateFormatChecking
[20250521 14:45:23 -5616]: System Date Format : dd/MM/yyyy
[20250521 14:45:23 -5616]: SystemDateFormatChecking
[20250521 14:45:23 -7323]: INI Init
[20250521 14:45:23 -7353]: CreateNetFormObject.Start()
[20250521 14:45:23 -7593]: CreateNetFormObject.End()
[20250521 14:45:23 -7603]: Clean Temp Files
[20250521 14:45:23 -7623]: Data House Keeping
[20250521 14:45:23 -7792]: CSPLUS.Start
[20250521 14:45:23 -7792]: Ver. 7.5.0.04R11A
[20250521 14:45:23 -8060]: doLoading.Start

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Tovi Wang** (2025-05-27):
FE log for your further checking
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi Please update the ticket status
**Tovi Wang** (2025-06-07):
@@Andrew_Au Waiting dev team further checking.Please arrange resource to check this one.Thanks!
**Sang** (2025-06-09):
@@Tovi Wang POS在这个时候好像突然闪退 - Please check did window re-start at that moment in window event log?
**Sang** (2025-06-09):
@Tovi @@Cy Lau refer to <u>**SOW of COACH China CDP Coupon Integration**</u> (Jira FE-1174)
**Tovi Wang** (2025-06-09):
@@Sang 根据店铺反馈window没有re-start，需要远程到店铺验证下这一点。
**Cy Lau** (2025-06-09):
@@Tovi Wang  two issues we needa work on
1. 
2. 
Thanks
**Tovi Wang** (2025-06-10):
@@Cy Lau 刚才远程查看了OCF30 Till3 2025-05-21 的windows Event log.2025-05-21 windows system没有关机。下面截图供您参考：
1.Event id:6006(正常关机)
2.Event id:6008(异常关机)
3.Event id:41(系统以外关闭)
4.Event id:1074(计划重启/关机)
5.OCF30 till3 T9 log
**Tovi Wang** (2025-08-28):
这种情况属于偶发情况(在结账的时候POS闪退导致coupon被使用但交易未完成)，所以只需让店铺后续完成交易即可。
可以向店铺提议先使用手改价格或者可以参考同样情况INC2989194给店铺提供具体的报备方法。

## 相關資訊

- Jira: [FE-1705](https://ctil.atlassian.net/browse/FE-1705)
- Fix Version: 未記錄
- 解決日期: 未記錄

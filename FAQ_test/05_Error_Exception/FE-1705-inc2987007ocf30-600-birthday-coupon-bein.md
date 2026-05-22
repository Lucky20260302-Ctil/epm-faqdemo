---
project: FE
title: "FE-1705: [INC2987007]OCF30 600 birthday coupon being used but not affecting"
issue_key: FE-1705
issue_type: Bug QA
status: Closed
faq_score: 9.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1705"
created: 2025-05-27
resolved: 
resolution: 
has_images: True
---

# FE-1705: [INC2987007]OCF30 600 birthday coupon being used but not affecting

## 問題描述

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

> 📎 **image-20250527-040022.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/16eb2af5-8f65-4795-99df-11d7d4ebfe39)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250527-040022.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/16eb2af5-8f65-4795-99df-11d7d4ebfe39)

## 相關資訊

- **Jira:** [FE-1705](https://ctil.atlassian.net/browse/FE-1705)
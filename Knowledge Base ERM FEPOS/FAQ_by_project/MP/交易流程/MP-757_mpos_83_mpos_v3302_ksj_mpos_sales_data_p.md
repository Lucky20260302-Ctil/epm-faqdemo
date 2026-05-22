---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Hi [CY Lau](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Lau_Ching_Yeung%40ctil.com) ["
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-757
resolved: 2025-05-02
fix-version: ""
---

# MP-757: [MPOS-83] MPOS v3.30.2 - KSJ MPOS Sales Data Posting Error

## 問題

Hi [CY Lau](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Lau_Ching_Yeung%40ctil.com) [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) , for MPOS v3.30.2, except normal sales data(without coupon) able to post, rest kind of data will have below posting error. Kindly help to check.
Testing machine ip: 172.24.253.69(C309)
MPOS API is connect to apawiqwposweb01
MB000023 - Normal sales with MM Coupon( the coupon we verified it able to post with CS2K Transaction), unable to post.
MB000024 - Return sales, unable to post.
MB000025 - Exchange sales, unable to post.
MB000026 - Tax Free sales, unable to post.
MB000027 - Void sales, original sales memo is MB000023, unable to post.
**MB000028 - Normal sales without coupon, able to post.**
Posting error:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (13 則)
**Tovi Wang** (2025-03-17):
@@Cy Lau @@Daniel Leung  Log for your further chec king.
**Cy Lau** (2025-03-17):
From the log, the transactions are all uploaded via MSMQ
So it isn’t uploading issue, neither polling.
[Posting]
And I need the posting log , @@Tovi Wang  IC8006 ? , IC8034 ?
the IC8004 logs have no clues on that.
**Tovi Wang** (2025-03-18):
@@Cy Lau  IC8006 log here for your further checking.Not found IC8034.
**Cy Lau** (2025-03-19):
@@Tovi Wang  , it should be 250314 log for IC8006 , please copy it ASAP for investigation
**Tovi Wang** (2025-03-19):
@@Cy Lau 我把03-13，03-14号所有KS IC8006 log都copy下来了。please furhter checking.
**Tovi Wang** (2025-03-20):
@@Cy Lau As talked in teams.Follow logs for your further checking.Thanks!
**Cy Lau** (2025-03-25):
MB000023 PCD was in wrong format
**Cy Lau** (2025-03-25):
MB000025 PCD was also
**Cy Lau** (2025-03-25):
for 26 vs 28
There is no difference
@@Daniel Leung  @@Sherman tse  would you mind doing the case of :
MB000023 - Normal sales with MM Coupon( the coupon we verified it able to post with CS2K Transaction), unable to post.
MB000024 - Return sales, unable to post.
MB000025 - Exchange sales, unable to post.
MB000026 - Tax Free sales, unable to post.
MB000027 - Void sales, original sales memo is MB000023, unable to post.
**MB000028 - Normal sales without coupon, able to post.**
@@Jerry Wong  Please help to provide the information of pcdtmn_inv_tax…. is in which line (for those errors)
**Cy Lau** (2025-03-25):
Please help to conduct with KSJ env
maybe need help from tovi to check the version of BEDB of KSJ
**Daniel Leung** (2025-03-26):
sales JSON from MPOS seems no structure different after compare with Copilot
**Tovi Wang** (2025-04-07):
@@Cy Lau Posting log NOT found the MPOS memo records and also NOT have error.Please double check.If need Anything other info please ping me.Thanks!
ACP2025040210242465.C309_M Start Processing                                                                                                                                                             
ACP2025040210242808.C309_M Start Processing                                                                                                                                                             
ACP2025040209452586.C309_M Start Processing                                                                                                                                                             
ACP2025040209452767.C309_M Start Processing                                                                                                                                                             
ACP2025040210271809.C309_M Start Processing                                                                                                                                                             
ACP2025040210271978.C309_M Start Processing                                                                                                                                                             
ACP2025040210532134.C309_M Start Processing                                                                                                                                                             
ACP2025040210532304.C309_M Start Processing
**Sherman tse** (2025-05-02):
Issue has closed in Tapestry jira
please find: [https://jira.tapestry.support/browse/MPOS-83](https://jira.tapestry.support/browse/MPOS-83) for details
close case

## 相關資訊

- Jira: [MP-757](https://ctil.atlassian.net/browse/MP-757)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

---
project: FE
title: "FE-1930: [CS-2632]How to enable Signout button in CS2000 POS FE"
issue_key: FE-1930
issue_type: Bug PRD
status: DEV Done
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1930"
created: 2026-04-16
resolved: 
resolution: 
has_images: True
---

# FE-1930: [CS-2632]How to enable Signout button in CS2000 POS FE

## 問題描述



@@Sang 请教一个小问题哈。CS2000 POS前台有一个 SignOut button是哪个xconfig来control的呀？

> 📎 **image-20260416-041640.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0f6ba8e3-7f86-425e-a55c-338b42eae188)（需 Jira 登入）
下面2个xconfig都enable,但还是没有sign Out button.

ENABLESIGNINOUT                 Y

Syscon_Sign_Out_Pass_Need       Y

> 📎 **image-20260416-041727.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c627d7c8-ec3f-4a96-a617-b9591a88e919)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260416-041640.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0f6ba8e3-7f86-425e-a55c-338b42eae188)
2. 📎 **image-20260416-041727.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c627d7c8-ec3f-4a96-a617-b9591a88e919)


## Jira Comments

> **Automation for Jira** (2026-04-20):
> Issue has been created since Days since: 3 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Tovi Wang** (2026-04-20):
>  PRC region.Dbtrans here,Please help to check.  

> **Tovi Wang** (2026-04-20):
>  这个是CN Pro的测试机，有sign out 和log out button.Dbtrans for your reference.Thanks! 1. 2.BE  UI  role setting.

> **Sang** (2026-04-20):
>  This bug will be fixed in next release (v750.04R25)

> **Sang** (2026-04-20):
>  OC9990 and OCT910 has different CashierControl setting,  This bug triggered when EnableSignInOut='Y' and CashierControl='N'

> **Tovi Wang** (2026-04-20):
>  Noted. I can reproduce it in OC9990 PC.  Please help to arrange this bug released ETA.Thanks! Reproduce steps: 1.Setting EnableSignInOut='Y' and CashierControl='N'. 2.Then signout button and logout butong disapeared. Changed before: Changed after:

> **Sang** (2026-04-20):
>   Fixed in v750.05R25 Enable Sign-Out Button Fixed (tblconfig.EnableSIgnInOut='Y' and CashierControl='N') (KTS 260420 FE-1930 v750.04R25, v750.05R12)

> **Tovi Wang** (2026-04-20):
>    Please help to arrange the testing and released ETA.Thanks!

> **Sang** (2026-04-22):
>    Program uploaded to  \\ds411\share\POS_FE_Release_64\20260422 Coach v750.04R25

## 相關資訊

- **Jira:** [FE-1930](https://ctil.atlassian.net/browse/FE-1930)
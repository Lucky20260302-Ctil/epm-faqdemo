---
project: FE
title: "FE-1768: [BASH] Print out issue: Gift receipt, Transfer"
issue_key: FE-1768
issue_type: Bug QA
status: Deployment
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1768"
created: 2025-10-06
resolved: 
resolution: 
has_images: True
---

# FE-1768: [BASH] Print out issue: Gift receipt, Transfer

## 問題描述

[BASH] Print out issue: Gift receipt, Transfer

1. Gift receipt: Display AO logo

> 📎 **image-20251006-054606.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/af5f4565-2094-4272-aab6-2a9aa531ab49)（需 Jira 登入）
2. Transfer:  for Page 1/1, need to use Chinese language

> 📎 **image-20251006-054643.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9cb7fbdf-1291-408e-9e13-632aafbe2b98)（需 Jira 登入）
3. Need to confirm if the below highlighted words can be set by config

> 📎 **image-20251006-054835.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4e0e279f-6229-4e23-b40d-02bc59b0a215)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251006-054606.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/af5f4565-2094-4272-aab6-2a9aa531ab49)
2. 📎 **image-20251006-054643.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9cb7fbdf-1291-408e-9e13-632aafbe2b98)
3. 📎 **image-20251006-054835.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4e0e279f-6229-4e23-b40d-02bc59b0a215)


## Jira Comments

> **Automation for Jira** (2025-10-06):
> Issue has been created since Days since: 0 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2025-10-06):
>    2. BASH_TransferOutMemo.Rpt Revised.

> **Sang** (2025-10-06):
>   Need to confirm if the below highlighted words can be set by config - Confirm can not set by Config.

> **Sang** (2025-10-06):
>   Revised program and Rpt files uploaded to \\ds411\share\POS_FE_Release_64\20251006 BASH v750.05 Beta Process consolidated day end before sub till complete day end, POS fail to alert missing till message fixed, add log (KTS 251006 FE-1766 v750.04R14D, v750.05) [20251006 12:10:35 -0511]: The day-end file cannot be found from the following sub-tills, tills number are [ 1 ]. Do you want to continue with consolidated report? Enhance BASH_GiftReceipt.rpt and BSAH_TransferOutMemo.rpt  (KTS 251006 FE-1768 v750.04R14D, v750.05)

> **Sherman tse** (2025-10-08):
> Verified case 1 & 2 on QA 172.16.138.4 1.  2. 

## 相關資訊

- **Jira:** [FE-1768](https://ctil.atlassian.net/browse/FE-1768)
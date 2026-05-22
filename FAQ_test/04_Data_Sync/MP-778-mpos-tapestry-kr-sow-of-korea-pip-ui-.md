---
project: MP
issue_key: MP-778
issue_type: SOW
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-778
created: '2025-06-02'
resolved: '2026-05-07'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-778: mPOS - Tapestry KR- SOW of Korea PIP UI Masking Enhancements'
---
# MP-778: mPOS - Tapestry KR- SOW of Korea PIP UI Masking Enhancements

## 問題描述

**Member Enquiry**

- **I**nformation about **Member Name, Mobile No., Home No. and Email Address **will be masked on the Member Enquiry list based on the corresponding configuration settings.

- The customer detail page is not required to apply masking after selecting the specific customer.

Suggest setting:

**vip_mask_enable = Y**

**vip_mask_rule =  -4**

> 📎 **image-20250602-093913.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/23f6bd39-0270-4d4d-80ad-6c2ad2c52633)（需 Jira 登入）

> 📎 **image-20250602-094051.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/76782cf0-3096-45d8-9679-e66d06356c69)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250602-093913.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/23f6bd39-0270-4d4d-80ad-6c2ad2c52633)
2. 📎 **image-20250602-094051.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/76782cf0-3096-45d8-9679-e66d06356c69)


## Jira Comments

> **Cy Lau** (2025-06-02):
>   Please check with the mPOS & mPOS API to identify if the source of member of korea would be the POS_API as the only source. If so then it would be enhancement in POS_API

> **Daniel Leung** (2025-06-16):
> KR-PIP version uploaded to    - 3.29.5-20250616.1 getMembers

> **Cy Lau** (2025-08-05):
> additional Payload to [BEGW]->BEAPI :  either post or get {  “source“ : “POS/MPOS“, ”mode” : “list/details“, ”salady” : “YWONG“, “module“ : “Sales“ } additional Payload BEAPI->[BEGW]->FEPOS / MPOS { “masked“ : true {vip object with masking handle} }

> **Cy Lau** (2025-08-05):
> MPOS MPOSAPI  

> **Daniel Leung** (2025-08-25):
> API : 3.30.5-20250826.1 IPA :  3.30.5-20250826.1  

> **Sherman tse** (2026-01-08):
> Relesed

> **Automation for Jira** (2026-01-08):
> Issue has been created since Days since: 219 Week since : 31 Issue due date difference Days since :  Weeks since: 

> **Andrew_Au** (2026-04-16):
>     Can we change the status to close

## 相關資訊

- **Jira:** [MP-778](https://ctil.atlassian.net/browse/MP-778)
- **解決方式:** Done
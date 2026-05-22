---
project: MP
issue_key: MP-727
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-727
created: '2024-11-21'
resolved: '2025-03-20'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-727: [MPOS-66] MPOS - Bonus point showing incorrect of MPOS member display page'
---
# MP-727: [MPOS-66] MPOS - Bonus point showing incorrect of MPOS member display page   

## 問題描述

as per we talked today, kindly help to check how to enhance bonus point display on both CS2K & MPOS.

1. MPOS whether could display as CS2K, have separate bonus point details.

2. Description could more clear for CS2K page.

> 📎 **image-20241121-054953.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/be1218d3-f7cb-45a9-8a50-16eb673f5799)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241121-054953.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/be1218d3-f7cb-45a9-8a50-16eb673f5799)


## Jira Comments

> **Joy Li** (2024-11-21):
> Tapestry want to show 10224 one. Or other method to display?

> **Cy Lau** (2024-11-27):
> Dev team has reviewed on that, additional API and Page is needed Est. would be given out later.

> **Cy Lau** (2024-11-27):
>      Please review the following mock-up BP:

> **Joy Li** (2024-11-28):
> Confirmed with Bobby. We will use display B

> **Cy Lau** (2024-11-28):
> MPOs API will provide the Bonus Points info via BPData field in Member object .Affected API: GetMembers

> **Cy Lau** (2024-12-01):
> \\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20241201.1b1 Release notes: Add tblconfig.crm_qr_iv_key - Online retrieve from BE DB table [dbconfig], use as iv in Coach QR Code Decryption process  Adding BPData to Memmber Object for MPOS Showing BP Program file Description Affect Module / API clsMemberQRCode, clsDataCenter DBMaintance_SysConfig Add tblconfig.crm_qr_iv_key - Online retrieve from BE DB table [dbconfig], use as iv in Coach QR Code Decryption process (KTS 241031 jira FE-1545/1548, v750.04R0x,V750.04R09, v750.05) MemberQRCode Member/QR Repository.cs Shareed.cs Member.cs At Member Object, add field “BPData“ If BPData is nothing , it would return null as value GetMembers

> **Cy Lau** (2024-12-01):
>  Please estimate the delivery schedule of this 

> **Joy Li** (2024-12-04):
>  Data is prepared below.

> **Cy Lau** (2024-12-09):
>    MPOS enhancement :  add redmGrpAlertMsg for the description 

> **Cy Lau** (2024-12-10):
> Enable condition for the BonusPointsData Enquiry: MemberOnLineRedeem = Y / D OR MMC_BP = Y OR MMC_BP_ALERT = Y  

> **Andrew_Au** (2025-02-24):
>  I close the ticket ?

## 相關資訊

- **Jira:** [MP-727](https://ctil.atlassian.net/browse/MP-727)
- **解決方式:** Done
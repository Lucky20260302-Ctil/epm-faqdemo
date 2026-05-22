---
project: BE
issue_key: BE-605
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- be
- data_sync
- faq
- master
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-605
created: '2022-06-09'
resolved: '2022-06-13'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-605: Re-save Item Master action leads to Onsales Price Data clear up'
---
# BE-605: Re-save Item Master action leads to Onsales Price Data clear up 

## 問題描述

<u>**Basic Information**</u>
Ticket: RIN00998495
Region: Coach PRC
SKU: 5476
Incident Date: 2022-06-04

**<u>Scenario</u>**
After re-saving Item in Item Master, the Onsales price page of related Item will show as empty. 

**<u>Reproduce Steps</u>**
1. In APABIQWPOSAPP21 (QA environment)
2. In Additional On Sales Price Information (MF2003), it shows some data which has not been expired.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/84ad23c4-f46d-48e9-a78c-83ece794f895)（需 Jira 登入）
 
3. Item Master Maintenance (MF0001), Re-save Item ‘1006’

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2ed07f3d-9e2f-4d31-b78c-df2f6fe60ac8)（需 Jira 登入）
 
4. Back to Additional On Sales Price Information (MF2003), All data of Item ‘1006’ are showing empty. 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1a8edb7e-6a82-447b-a824-191374d43118)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/84ad23c4-f46d-48e9-a78c-83ece794f895)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2ed07f3d-9e2f-4d31-b78c-df2f6fe60ac8)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1a8edb7e-6a82-447b-a824-191374d43118)

## 相關資訊

- **Jira:** [BE-605](https://ctil.atlassian.net/browse/BE-605)
- **解決方式:** Done
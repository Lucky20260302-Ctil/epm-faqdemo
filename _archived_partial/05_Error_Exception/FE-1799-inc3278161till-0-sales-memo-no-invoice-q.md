---
project: FE
issue_key: FE-1799
issue_type: Bug DEV
status: Selected for Development (migrated)
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v750.01r01a
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1799
created: '2025-11-06'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1799: [INC3278161]Till 0 sales memo no invoice QR code'
---
# FE-1799: [INC3278161]Till 0 sales memo no invoice QR code

## 問題描述

PRC OC231 POSv75

Till 0 all sales memo no invoice QR code.

checked the value of invtrx_prt_einv in dbhist.sdf/jouinvh of memo ‘00026484' is ‘N’, updated to Y, still can’t print qrcode.

 

> 📎 **image-20251106-013508.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2a77ba97-f5f9-4935-a463-2dc4e0a0f3e4)（需 Jira 登入）
compare the dbtrans from OC231till0 and the dbtrans from OC134till0 which can print qrcode normally. have 2 diff about Qrcode and updated, but still failed to print.

> 📎 **image-20251106-014705.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/187e3758-08e4-44cb-997b-aed76224ba53)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0f08773a-a8b1-4e85-923b-d6e83d3070c3)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e1035f99-29d5-40a5-b8a6-a5f01fa5dfb6)（需 Jira 登入）
all the logs on OC231 till0 has been uploaded, please help to check.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3974aeaf-65fa-409e-87b3-1aa4e6fc8798)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20251106-013508.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2a77ba97-f5f9-4935-a463-2dc4e0a0f3e4)
2. 📎 **image-20251106-014705.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/187e3758-08e4-44cb-997b-aed76224ba53)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0f08773a-a8b1-4e85-923b-d6e83d3070c3)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e1035f99-29d5-40a5-b8a6-a5f01fa5dfb6)
5. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3974aeaf-65fa-409e-87b3-1aa4e6fc8798)

## 相關資訊

- **Jira:** [FE-1799](https://ctil.atlassian.net/browse/FE-1799)
---
project: MP
issue_key: MP-348
issue_type: Bug DEV
status: Closed
tags:
- 03_performance_timeout
- faq
- mp
- mpos
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-348
created: '2021-01-15'
resolved: '2021-07-20'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: stub
title: 'MP-348: Payment Module - A920 Integration issue'
---
# MP-348: Payment Module - A920 Integration issue

## 問題描述

### 1. Missing time remain in all sessions

 

Sample screen:

  

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0995c064-3cb5-4bd2-9f9e-0bbbbbf6b443)（需 Jira 登入）
For example after wipe credit issue memo card screen, void memo screen etc.

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/76f38640-0204-4546-a230-d80b9119bff0)（需 Jira 登入）
 

### 2. A920 cancel order handling

 

A920 click back button to cancel order processing, app will display [error 400 ?????????]

 

  

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1e6a9ceb-e2bb-4977-b9f6-1877425cc4fa)（需 Jira 登入）
 ** 

### 3. A920 ordering timeout display

 

 

A920 keep waiting without further action, app display [error 400 ??????]

 

  

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cdedf5ba-6a0f-48d1-9bad-2c37fb239f15)（需 Jira 登入）
 

 

 

 

### 4.    Not support Issue memo with Multi-ECR Payment

 

### Issue sales memo with two ECR Payments, but combine into one

 

1) ** Input one 500 ECR Payment on 4480 sales memo

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/dac25ea9-a3d2-4298-9779-64aa01a89e90)（需 Jira 登入）
 

2) Payment remain amount 3980 and confirm

 

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/09110860-8fca-401b-be68-d909f9f95607)（需 Jira 登入）
 

 3) But two ECR Payments auto combine into one ECR Payments

 

  

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ab0fa9e3-3ce8-4e49-add3-f7b3ab21a892)（需 Jira 登入）
 

(Refer screen for two or more ECR Payments)

 

  

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4d4ba8ad-53a3-4d90-8710-2c072698516c)（需 Jira 登入）
 

### 5.    ECR Void Result layout

 

The wording “Result” split to two rows to display

 

  

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/225f0b6f-2a01-44f5-97ae-ddad4bc50553)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0995c064-3cb5-4bd2-9f9e-0bbbbbf6b443)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/76f38640-0204-4546-a230-d80b9119bff0)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1e6a9ceb-e2bb-4977-b9f6-1877425cc4fa)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cdedf5ba-6a0f-48d1-9bad-2c37fb239f15)
5. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/dac25ea9-a3d2-4298-9779-64aa01a89e90)
6. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/09110860-8fca-401b-be68-d909f9f95607)
7. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ab0fa9e3-3ce8-4e49-add3-f7b3ab21a892)
8. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4d4ba8ad-53a3-4d90-8710-2c072698516c)
9. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/225f0b6f-2a01-44f5-97ae-ddad4bc50553)

## 相關資訊

- **Jira:** [MP-348](https://ctil.atlassian.net/browse/MP-348)
- **解決方式:** Done
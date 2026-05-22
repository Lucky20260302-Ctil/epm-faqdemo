---
project: FE
title: "FE-1546: [Coach][CRM milestone 2] Fail to pop up member creation screen after scan a new wechat QR code"
issue_key: FE-1546
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1546"
created: 2024-11-01
resolved: 2024-11-08
resolution: Done
has_images: True
---

# FE-1546: [Coach][CRM milestone 2] Fail to pop up member creation screen after scan a new wechat QR code

## 問題描述

Reproduce steps:

1. Open member section

2. insert QR code string

Existing result:

Fail to pop up member creation screen after scan a new wechat QR code

> 📎 **image-20241101-084227.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e9f0bb95-bebb-44a0-830f-1caa4a22dda5)（需 Jira 登入）
New QR string:

YVhaQWRYTmxaRFIwWVhCemRISjVQUT09cThjUmFBSEZwa3dpV2EzZmdaWmpkNWNXREpWY1NCMWs3RUp0VVNteDIwRGdXWkFLRFF1d3RHQ3RFWHc2c1dsT3RYbW5UcCtJQjJYdUZFNEJpcWlYWFJZTktXQ0JLUU5Nbm1SK0E3TTNEQXByR2xjekFDUUxlenBjdlJJYlNiTis=

Old QR string:

YVhaQWRYTmxaRFIwWVhCemRISjVQUT09djJFYmppRDdxaE5pczBnK21RdGJHSzlyejB6V3lBK09oc0RsM0hLODdUUVZydFFwUmNFUXpjSDcwYjIwMnUvUXJVMElrcUFhN2xuRUErQWxHTHpkSUpyRzZBWHBkMXR6VGxmbU9EWWF6U1ZoN2ZDSDBkT2JzYXdLNUd6QWRGU2dqeEhkSjRHdENxMFc2dEVsL2JWTTVBPT0=

DBmas & DBtrans:

\\172.16.183.201\localuser\support\20241101\Sang

VM IP:

172.16.138.131

.\sxd

Yan20201104@



## 附件截圖

1. 📎 **image-20241101-084227.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e9f0bb95-bebb-44a0-830f-1caa4a22dda5)

## 相關資訊

- **Jira:** [FE-1546](https://ctil.atlassian.net/browse/FE-1546)
- **解決方式:** Done
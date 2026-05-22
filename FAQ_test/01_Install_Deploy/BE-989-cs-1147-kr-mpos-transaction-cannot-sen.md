---
project: BE
issue_key: BE-989
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, be, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/BE-989"
created: 2025-01-20
resolved: 
resolution: 
has_images: True
---

# BE-989: [CS-1147] - KR MPOS transaction cannot send to DB

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 7.0
> **負責人:** Cy Lau
> **組件:** MPOS

## 問題描述

1.

KR MPOS sales can’t upload to DB.The issue happend in Pro.

Temp workaround: Repost the PCD file can fixed 

New sample memo:

2025-01-19 OCF50-MA000029       
2025-01-19 OCF50 -MA000030       

> 📎 **image-20250121-033113.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/98c8dd07-6c5e-4ecc-a17f-e83a4ca0f0cb)（需 Jira 登入）
2.

Also NOT found the MPOS memo in sqlpcda table.

> 📎 **image-20250122-062543.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a4a2ca2c-7b76-40f1-a014-e2441f887378)（需 Jira 登入）
3.

 The Coach testing machine 10.33.248.10 has upgraded to V75.Waiting Queenie teasting in this QA PC,then feedback the result to us.

QA POS version:75.004.0702

QA MPOS version:3.29.X



## 附件截圖

1. 📎 **image-20250121-033113.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/98c8dd07-6c5e-4ecc-a17f-e83a4ca0f0cb)
2. 📎 **image-20250122-062543.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a4a2ca2c-7b76-40f1-a014-e2441f887378)

## 相關資訊

- **Jira:** [BE-989](https://ctil.atlassian.net/browse/BE-989)
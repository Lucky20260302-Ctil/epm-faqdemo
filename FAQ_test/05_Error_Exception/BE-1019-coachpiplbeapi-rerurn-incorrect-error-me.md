---
project: BE
title: "BE-1019: [Coach][PIPL][BEAPI] Rerurn incorrect error message to POS when insert incorrect email/ member id/ mobile no"
issue_key: BE-1019
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1019"
created: 2025-03-03
resolved: 2025-03-03
resolution: Done
has_images: True
---

# BE-1019: [Coach][PIPL][BEAPI] Rerurn incorrect error message to POS when insert incorrect email/ member id/ mobile no

## 問題描述

[Coach][PIPL][BEAPI] Return incorrect error message to POS when insert incorrect email/ member id/ mobile no

Input data:

> 📎 **image-20250303-095417.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d358ce19-705c-4a34-9dc4-07eb30370543)（需 Jira 登入）
Return:

> 📎 **image-20250303-095501.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4068b5b6-f930-4dbb-9c40-9276b2f2144a)（需 Jira 登入）
Expected result:

Should return “Member not found“error message to POS when insert incorrect email/ member id/ mobile no



## 附件截圖

1. 📎 **image-20250303-095417.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d358ce19-705c-4a34-9dc4-07eb30370543)
2. 📎 **image-20250303-095501.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4068b5b6-f930-4dbb-9c40-9276b2f2144a)

## 相關資訊

- **Jira:** [BE-1019](https://ctil.atlassian.net/browse/BE-1019)
- **解決方式:** Done
---
project: MP
issue_key: MP-635
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-635"
created: 2023-02-14
resolved: 2023-02-14
resolution: Done
has_images: False
---

# MP-635: Fail to add new member when inserted email address

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 7.0
> **解決日期:** 2023-02-14
> **負責人:** Daniel Leung
> **組件:** MPOS

## 問題描述

Reproduce steps:

1. Go to create new member

2. Insert essential info, including email (not reg before) e.g.: [sherman@gmail.com](mailto:abc@gmail.com)

Existing result:

Fail to add new member & pop up error: [999] This email has been registered (reg: image-2023-02-14-16-14-07-369.png)



## 相關資訊

- **Jira:** [MP-635](https://ctil.atlassian.net/browse/MP-635)
- **解決方式:** Done
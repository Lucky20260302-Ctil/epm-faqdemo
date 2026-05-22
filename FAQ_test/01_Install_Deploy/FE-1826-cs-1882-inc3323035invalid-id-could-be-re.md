---
project: FE
title: "FE-1826: [CS-1882] [INC3323035]invalid ID could be registered as salesperson ID on CS2000 when making transaction"
issue_key: FE-1826
issue_type: Bug DEV
status: Closed
faq_score: 6.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1826"
created: 2025-12-03
resolved: 2026-03-25
resolution: Done
has_images: True
---

# FE-1826: [CS-1882] [INC3323035]invalid ID could be registered as salesperson ID on CS2000 when making transaction

## 問題描述

[INC3323035]POS V75 JP region, invalid ID could be registered as salesperson ID on CS2000 when making transaction。 this issue also occurred on other stores.

J804 till1, sales memo 10158519, the sales person should be 744382 ,but it shew 744282.

it shew 744282 in pos FE. We test this issue in product environment, can’t reproduce.

> 📎 **image-20251203-075803.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3aec1635-f88c-45af-8f3b-34424f51ef92)（需 Jira 登入）
checked in dbmas-tblsalady, 744282 not existed.

> 📎 **image-20251203-031318.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/88d16aab-da44-43a1-b684-6a639d35d7dc)（需 Jira 登入）
can only find related info in T9 and PC file.

> 📎 **image-20251203-032046.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/10123ae8-ab0d-4f84-9f5e-28a6160b61d1)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7a408a15-7752-4da4-8f51-ceb36c3ee5d6)（需 Jira 登入）
This issue occurred frequently from Oct 2025.

> 📎 **image-20251204-015245.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1e214056-ebaa-4684-964e-900d88df37ba)（需 Jira 登入）

> 📎 **image-20251204-015335.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/570df40d-061a-45b4-b192-cbca9632344b)（需 Jira 登入）
CC: @@Joy Li @@Tovi Wang 



## 附件截圖

1. 📎 **image-20251203-075803.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3aec1635-f88c-45af-8f3b-34424f51ef92)
2. 📎 **image-20251203-031318.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/88d16aab-da44-43a1-b684-6a639d35d7dc)
3. 📎 **image-20251203-032046.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/10123ae8-ab0d-4f84-9f5e-28a6160b61d1)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7a408a15-7752-4da4-8f51-ceb36c3ee5d6)
5. 📎 **image-20251204-015245.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1e214056-ebaa-4684-964e-900d88df37ba)
6. 📎 **image-20251204-015335.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/570df40d-061a-45b4-b192-cbca9632344b)

## 相關資訊

- **Jira:** [FE-1826](https://ctil.atlassian.net/browse/FE-1826)
- **解決方式:** Done
---
project: FE
issue_key: FE-1648
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1648
created: '2025-03-13'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1648: [ACU-119]Always 0 for each field on member profile page while querying CN member with exit_permit=1 on HK POS FE'
---
# FE-1648: [ACU-119]Always 0 for each field on member profile page while querying CN member with exit_permit=1 on HK POS FE

## 問題描述

QA CN POS: 10.33.248.4

QA HK POS:  10.33.248.2

Reproduce steps:

1. Create sales transaction for CN member OCQA1TC00000077 (19921610075) with exit_permit=1 on CN POS FE.

2. Query CN member with mobile '19921610075' on CN POS FE,.Click Profile button,the member information is normal display.

> 📎 **image-20250313-022823.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3f846a12-880f-43c9-8b3f-10fecacc1eb5)（需 Jira 登入）
3.Query CN member with mobile '19921610075' on HK POS FE, the member information will be displayed as bellow:

> 📎 **image-20250313-023124.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/204d8f06-f749-4c6b-8612-2e1c2b47c42e)（需 Jira 登入）
4.But Click Profile button, There is always 0 for each field.@@Anson Cheung  Is this expected display or bug?Please clarify.Thanks!

> 📎 **image-20250313-023159.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e98bc0b1-fa72-48df-8a2f-fe5e5de99160)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250313-022823.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3f846a12-880f-43c9-8b3f-10fecacc1eb5)
2. 📎 **image-20250313-023124.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/204d8f06-f749-4c6b-8612-2e1c2b47c42e)
3. 📎 **image-20250313-023159.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e98bc0b1-fa72-48df-8a2f-fe5e5de99160)

## 相關資訊

- **Jira:** [FE-1648](https://ctil.atlassian.net/browse/FE-1648)
- **解決方式:** Done
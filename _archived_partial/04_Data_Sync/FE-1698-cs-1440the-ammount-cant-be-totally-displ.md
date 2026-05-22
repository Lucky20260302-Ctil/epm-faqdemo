---
project: FE
issue_key: FE-1698
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- printing
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1698
created: '2025-05-20'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1698: [CS-1440]The ammount can''t be totally displayed as bellow:'
---
# FE-1698: [CS-1440]The ammount can't be totally displayed as bellow:

## 問題描述

@@Cy Lau @@Sang  As talked in teams.

CC @@Joy Li 

1.the ammount can't be totally displayed as bellow:

> 📎 **image-20250520-073637.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/aa54112d-8ba4-413a-8125-a88a442b5eb3)（需 Jira 登入）
2.Preview page also have this issue.

> 📎 **image-20250520-073729.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e1f7b6a1-96cc-4713-bb25-c6cb5ed39846)（需 Jira 登入）
3.

a.TMU_PRINTER_REC_LINE_CHAR setting is 40 now

b.PRINTCHARSETCODE setting is KO now.

c.CHARSETCODE setting also is KO.

Troubleshooting:

 1.Whether TMU_PRINTER_REC_LINE_CHAR setting is 42 or 48，but issue still.



## 附件截圖

1. 📎 **image-20250520-073637.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/aa54112d-8ba4-413a-8125-a88a442b5eb3)
2. 📎 **image-20250520-073729.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e1f7b6a1-96cc-4713-bb25-c6cb5ed39846)

## 相關資訊

- **Jira:** [FE-1698](https://ctil.atlassian.net/browse/FE-1698)
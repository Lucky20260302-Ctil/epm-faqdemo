---
project: BE
issue_key: BE-878
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- backend-(web)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-878
created: '2024-07-19'
resolved: '2024-08-22'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
---
# BE-878: Location Grouping Control ：存在重复数据时，点击Validate按钮，两个提示语直接死循环

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2024-08-22
> **負責人:** Jerry Wong
> **組件:** Backend (Web)

## 問題描述

Reproduce steps:

1. 新建两组一摸一样数据

2. 填入必要輸入的資料

3. 点击Validate

Incorrect result:

- 提示Save successful，提示Duplicate Code，陷入死循环，系统无法进行其他操作

> 📎 **image-20240719-064226.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0d32a450-5acc-4147-a0fc-04df22eac907)（需 Jira 登入）

> 📎 **image-20240719-064254.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3411498f-1280-40ea-8b7e-89f9e3b31be6)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240719-064226.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0d32a450-5acc-4147-a0fc-04df22eac907)
2. 📎 **image-20240719-064254.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3411498f-1280-40ea-8b7e-89f9e3b31be6)

## 相關資訊

- **Jira:** [BE-878](https://ctil.atlassian.net/browse/BE-878)
- **解決方式:** Done
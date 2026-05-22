---
project: BE
issue_key: BE-1149
issue_type: Bug DEV
status: Closed
tags:
- 05_error_exception
- be
- error_exception
- faq
- table
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1149
created: '2025-07-15'
resolved: '2025-10-09'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
# BE-1149: [INC3083299]pwhistlg表pwhistlg_password字段NULL值

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.0
> **解決日期:** 2025-10-09
> **負責人:** Joy Li
> **組件:** Table

## 問題描述

PRC region,OCF502 ,BE保存staff451853 账号的密码报DBNULL错，检查pwhistlg表pwhistlg_password字段NULL值，显示键值数据来源是MF0007. BE策略是不允许空值保存的.

> 📎 **image-20250715-060229.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5035298c-bc38-4de1-b3b6-8fa028300cc4)（需 Jira 登入）

> 📎 **image-20250715-060247.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8d5ffd8f-6b96-44d8-b175-41a1f22e9b6a)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250715-060229.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5035298c-bc38-4de1-b3b6-8fa028300cc4)
2. 📎 **image-20250715-060247.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8d5ffd8f-6b96-44d8-b175-41a1f22e9b6a)

## 相關資訊

- **Jira:** [BE-1149](https://ctil.atlassian.net/browse/BE-1149)
- **解決方式:** Done
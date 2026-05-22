---
project: BE
issue_key: BE-869
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-869
created: '2024-07-03'
resolved: '2024-07-18'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
# BE-869: Primary_Sales Staff： 在Contact Number输入’12345678‘，点击save报错

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2024-07-18
> **負責人:** ryan
> **組件:** Backend (Web)

## 問題描述

Reproduce steps:

1. 新建一個 Primary-Sales Staff

2. 填入必要輸入的資料

3. 在page1下Contact Number输入’12345678‘

4. 点击save

Incorrect result:

- 提示save failed

> 📎 **image-20240703-091240.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ddd982d8-40bc-4b98-8cb6-e02bad341077)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240703-091240.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ddd982d8-40bc-4b98-8cb6-e02bad341077)

## 相關資訊

- **Jira:** [BE-869](https://ctil.atlassian.net/browse/BE-869)
- **解決方式:** Done
---
project: BE
issue_key: BE-330
issue_type: Bug DEV
status: Closed
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-330"
created: 2020-11-03
resolved: 2022-06-15
resolution: Done
has_images: True
---

# BE-330: Data concurrency handling

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.5
> **解決日期:** 2022-06-15
> **負責人:** howard
> **組件:** Backend (Web)

## 問題描述

Client A and Client B open same module in edit mode e.g. (MF1005)

Client A save record successfully.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/799ab9e2-7d67-4b8c-98e9-d6f816fb7015)（需 Jira 登入）
After long period of time, Client B save record display error.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f0be7737-d8f4-4b13-a9f8-1ba606f60ec2)（需 Jira 登入）
Already handle data concurrency, please try again (8/9/2021)



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/799ab9e2-7d67-4b8c-98e9-d6f816fb7015)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f0be7737-d8f4-4b13-a9f8-1ba606f60ec2)

## 相關資訊

- **Jira:** [BE-330](https://ctil.atlassian.net/browse/BE-330)
- **解決方式:** Done
---
project: BE
title: "BE-1193: [PPR-22] - ANZ POS - AU 20 Web sales import error - Exchange rate not found"
issue_key: BE-1193
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1193"
created: 2025-10-29
resolved: 
resolution: 
has_images: True
---

# BE-1193: [PPR-22] - ANZ POS - AU 20 Web sales import error - Exchange rate not found

## 問題描述

Coach QA team callout when import follow ecom sales file,then pop out 'Exchange rate not found’ error ,can you check below error?

I used the same format before to import, it was inserted successfully.

but this time it is not working.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c664625c-d888-48ec-a50a-42b8ca9ac65a)（需 Jira 登入）

Troubleshooting:

1.2025-10-23 有一个正常导入的文件，没有error.

> 📎 **image-20251029-084549.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/66d8e0db-cf03-44c6-9ce7-985bbe56e979)（需 Jira 登入）
2.之前可以正常导入的文件

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/18897641-16a1-464b-8e7e-e766107863d4)（需 Jira 登入）
3.现在重新导入之前正常导入的文件，也是有同样的error

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7204a9cd-aa78-4dd2-a060-8eaec7ec0f2c)（需 Jira 登入）
[4.AU](http://4.AU) 20 region AU paytab is 'AUD'

> 📎 **image-20251029-085423.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b6a6b5ff-23f3-4e6a-9506-603d19f2d5cb)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c664625c-d888-48ec-a50a-42b8ca9ac65a)
2. 📎 **image-20251029-084549.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/66d8e0db-cf03-44c6-9ce7-985bbe56e979)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/18897641-16a1-464b-8e7e-e766107863d4)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7204a9cd-aa78-4dd2-a060-8eaec7ec0f2c)
5. 📎 **image-20251029-085423.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b6a6b5ff-23f3-4e6a-9506-603d19f2d5cb)

## 相關資訊

- **Jira:** [BE-1193](https://ctil.atlassian.net/browse/BE-1193)
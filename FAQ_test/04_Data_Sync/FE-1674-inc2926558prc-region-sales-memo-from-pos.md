---
project: FE
issue_key: FE-1674
issue_type: Bug DEV
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1674"
created: 2025-04-22
resolved: 2025-06-05
resolution: Done
has_images: True
---

# FE-1674: [INC2926558]PRC region sales memo from POSV75has different format with that from POSv72

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.5
> **解決日期:** 2025-06-05
> **負責人:** Sang
> **組件:** Front End v750.01R01A

## 問題描述

V75的sales memo中，下图1‘2’3，3个地方在V75中哪些config来控制的？对应文本内容是在哪里修改的？

图中1处v72中可见，在V75中不见了

图中2处V75和V72的格式不一样，并且丢失了部分内容

图中3处，V75有，但是V72中是没有的。

> 📎 **333.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/957d29e0-b356-4346-aa36-56f19432ae80)（需 Jira 登入）


## 附件截圖

1. 📎 **333.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/957d29e0-b356-4346-aa36-56f19432ae80)


## Jira Comments

> **Sang** (2025-04-22):
>  Please get dbtrans.sdf

> **pierre.shi** (2025-04-22):
>  Hi, dbtrans has been uploaded.

> **Sang** (2025-04-22):
>   v75 Print out  1 - tblLocMsg Footer (Ex)

> **pierre.shi** (2025-04-22):
>  Hi Sang, 位置2，现在显示不全， 这个config我之前找到了，并修改了对应格式。因为单行显示不全，我在‘详细检查商品’后加了一个回车分行，但是打印效果还是没变。

> **Sang** (2025-04-22):
>  Create a new sales memo, and check the result

> **pierre.shi** (2025-04-22):
>  ok。thanks

> **Andrew_Au** (2025-06-05):
>    Please update the ticket status

> **pierre.shi** (2025-06-05):
> Hi    please help to close this ticket.

## 相關資訊

- **Jira:** [FE-1674](https://ctil.atlassian.net/browse/FE-1674)
- **解決方式:** Done
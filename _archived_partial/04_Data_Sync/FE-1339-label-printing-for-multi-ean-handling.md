---
project: FE
issue_key: FE-1339
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
jira_url: https://ctil.atlassian.net/browse/FE-1339
created: '2024-01-23'
resolved: '2024-11-29'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1339: Label Printing for multi EAN handling'
---
# FE-1339: Label Printing for multi EAN handling

## 問題描述

<u>COACH CS-856: Issue_Main UPC code issue</u>

Testing FE DB: 172.16.138.180

ItmEan_Item_No = '80125'and ItmEan_Item_Col='FLI' and ItmEan_Item_Size = 'S'  >> have 2 EAN

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/033c1310-82f9-45de-a414-e244d7e0b193)（需 Jira 登入）
Label printing only get and print the smallest EAN. COACH reported that the last update EAS should be print >> 884830134087 in item 80125-FI-S should be print.

Could you please help?

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b9be2803-887f-4bf0-876d-c152e80e2fbe)（需 Jira 登入）
 

 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/033c1310-82f9-45de-a414-e244d7e0b193)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b9be2803-887f-4bf0-876d-c152e80e2fbe)


## Jira Comments

> **Andrew_Au** (2024-11-29):
>   Can we change the status to Close

> **Joy Li** (2024-11-29):
> released in V75.0004.0301.0000 please close   

## 相關資訊

- **Jira:** [FE-1339](https://ctil.atlassian.net/browse/FE-1339)
- **解決方式:** Done
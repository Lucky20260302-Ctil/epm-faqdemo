---
project: FE
title: "FE-1668: [INC2905589]failed to finish consolidation,  it popped up error: Database not exist."
issue_key: FE-1668
issue_type: Bug DEV
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1668"
created: 2025-04-10
resolved: 2025-06-05
resolution: Done
has_images: True
---

# FE-1668: [INC2905589]failed to finish consolidation,  it popped up error: Database not exist.

## 問題描述

PRC region, POS V75, while doing dayend, it popped up error: Database not exist.

PC and RP file has been generated but no RC file.

no dayend report and  consolidation report printed.

checked in logs, it only showed :Database not exist. in T9 logs.

> 📎 **0409.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a71c71e9-0078-4f29-9b23-c2bf8ca1df41)（需 Jira 登入）

> 📎 **0408.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7f5b40c7-485b-44ff-8337-772b3ec57568)（需 Jira 登入）
on the next day ,can finish consolidation without any error.

This issue occurred on 8th and 9th April. 



## 附件截圖

1. 📎 **0409.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a71c71e9-0078-4f29-9b23-c2bf8ca1df41)
2. 📎 **0408.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7f5b40c7-485b-44ff-8337-772b3ec57568)

## 相關資訊

- **Jira:** [FE-1668](https://ctil.atlassian.net/browse/FE-1668)
- **解決方式:** Done
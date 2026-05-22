---
project: BE
issue_key: BE-329
issue_type: Bug DEV
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-329"
created: 2020-11-02
resolved: 2021-01-15
resolution: Done
has_images: True
---

# BE-329: Searching with first keyword shows duplicate results

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **解決日期:** 2021-01-15
> **負責人:** howard
> **組件:** Backend (Web)

## 問題描述

<u>Case 1</u>

Search first keyword using "exchange", it return duplicated results start from the wording "exchange".   

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3a012ffe-9613-47d1-a3a3-f9ac8c8d3bb6)（需 Jira 登入）
<u>Case 2</u>

Search keyword using "TAX" , the duplicated results only appear start from the first wording "TAX",  compared other results e.g. VAT **TAX** Rate (MX2000) is display once at normal.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cb683a0e-ee33-42b9-b63c-22e6e59dab04)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3a012ffe-9613-47d1-a3a3-f9ac8c8d3bb6)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cb683a0e-ee33-42b9-b63c-22e6e59dab04)

## 相關資訊

- **Jira:** [BE-329](https://ctil.atlassian.net/browse/BE-329)
- **解決方式:** Done
---
project: BE
issue_key: BE-1038
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1038"
created: 2025-03-27
resolved: 2025-03-27
resolution: Done
has_images: True
---

# BE-1038: [API] ponumber如果入了invalid value會timeout

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **解決日期:** 2025-03-27
> **負責人:** jordan.wang
> **組件:** API

## 問題描述

Update PO: /api/v1/pos/

`"poNumber": "2025032566ABC"`

Ponumber 入了一個DB沒有的value, 會導致return timeout

> 📎 **image-20250327-081648.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ca83fbd3-13d9-4c72-be2e-2c9869b0a6d6)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250327-081648.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ca83fbd3-13d9-4c72-be2e-2c9869b0a6d6)

## 相關資訊

- **Jira:** [BE-1038](https://ctil.atlassian.net/browse/BE-1038)
- **解決方式:** Done
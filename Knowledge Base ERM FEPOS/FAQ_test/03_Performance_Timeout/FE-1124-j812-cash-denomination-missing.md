---
project: FE
issue_key: FE-1124
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1124"
created: 2022-06-21
resolved: 2022-06-29
resolution: Done
has_images: True
---

# FE-1124: J812 Cash Denomination missing

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.5
> **解決日期:** 2022-06-29
> **負責人:** Joy Li
> **組件:** Front End

## 問題描述

Email: Please follow up on INC1814512

 Reproduce step:

1. Input Cash Denomination then click F1 confirm

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7b215a39-e8df-4fa3-9314-9f10973bf01c)（需 Jira 登入）
2. Back to Cash Drawer Tender Count Input and re-enter cash denomination.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e658b088-d651-4880-a76d-fec9fffb994f)（需 Jira 登入）
3. Click F10 Cancel without any change.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/13c3e962-e053-4c3a-abc5-afacfec08e61)（需 Jira 登入）
4. Then finish the day end process. The cash denomination will missing.



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7b215a39-e8df-4fa3-9314-9f10973bf01c)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e658b088-d651-4880-a76d-fec9fffb994f)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/13c3e962-e053-4c3a-abc5-afacfec08e61)

## 相關資訊

- **Jira:** [FE-1124](https://ctil.atlassian.net/browse/FE-1124)
- **解決方式:** Done
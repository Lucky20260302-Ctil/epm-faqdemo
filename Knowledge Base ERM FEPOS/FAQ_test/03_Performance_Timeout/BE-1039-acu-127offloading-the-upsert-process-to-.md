---
project: BE
issue_key: BE-1039
issue_type: Improvement
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1039"
created: 2025-03-28
resolved: 2025-10-06
resolution: Done
has_images: True
---

# BE-1039: [ACU-127]Offloading the Upsert Process to a Separate Async Service

> **類型:** Improvement | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **解決日期:** 2025-10-06
> **負責人:** Sherman tse
> **組件:** API

## 問題描述

- Improvement: This change will significantly enhance performance. Isolated debugging sessions have shown that removing the process can save 6 seconds out of approximately 10 seconds.

- Pros: The member search operation will no longer depend on the upsert process.

- Cons: The caching version may not align with the search results due to asynchronous updates.

- ETA: To be confirmed.(Drafting the new flow with new modules)

- Temporary Solution: V1.07.08+ - Configuration to disable ACIXOM member upsert.

Offloading the member upsert would be considered as Sync-Member-Upsert and Async-Member-Upsert as diagram:

> 📎 **image-20250327-172712.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/91982fa3-538e-4766-a787-bdcd13339e2c)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250327-172712.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/91982fa3-538e-4766-a787-bdcd13339e2c)

## 相關資訊

- **Jira:** [BE-1039](https://ctil.atlassian.net/browse/BE-1039)
- **解決方式:** Done
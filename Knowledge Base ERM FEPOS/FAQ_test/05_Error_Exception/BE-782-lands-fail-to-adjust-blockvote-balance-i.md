---
project: BE
issue_key: BE-782
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-782"
created: 2023-07-20
resolved: 2023-08-14
resolution: Done
has_images: True
---

# BE-782: [Lands] Fail to adjust BlockVote balance in BV0001

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-08-14
> **負責人:** Sherman tse
> **組件:** Backend (Web)

## 問題描述

Env: [https://smo-pmssapp-u1/ChainStorePlus/bv0001](https://smo-pmssapp-u1/ChainStorePlus/bv0001)

Reproduce steps:

1. Select one of the BV acc in BV0001

2. Try to adjust the balance

Existing result:

Pop up an error (as below picture) & fail to adjust the balance

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/af23baec-d259-4dcf-825d-f967cd4c77db)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/af23baec-d259-4dcf-825d-f967cd4c77db)

## 相關資訊

- **Jira:** [BE-782](https://ctil.atlassian.net/browse/BE-782)
- **解決方式:** Done
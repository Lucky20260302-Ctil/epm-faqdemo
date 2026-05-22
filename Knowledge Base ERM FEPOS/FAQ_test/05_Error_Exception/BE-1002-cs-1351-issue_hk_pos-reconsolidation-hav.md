---
project: BE
issue_key: BE-1002
issue_type: Bug PRD
status: Closed
faq_score: 9.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1002"
created: 2025-02-13
resolved: 2025-05-02
resolution: Done
has_images: True
---

# BE-1002: CS-1351 Issue_HK_POS reconsolidation have discrepancy

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 9.5
> **解決日期:** 2025-05-02
> **負責人:** Anson Cheung
> **組件:** Data Interface

## 問題描述

we found there is 61 records failed to send sales data from CS2000 to Acxiom

pls see below record.

error is coming from VIP synchronization.

pls help check RCA and solution.

1.For sample 

vip no :OCF12H00230077

sales memo:OCF1-20285439

Date: 2025-02-11

CRM log can found the error.

> 📎 **image-20250214-033039.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3b69ebe2-0ed7-4327-8af4-fd3d77c6bd0e)（需 Jira 登入）
2.CRMlog message:

fail to send member in member sync process: OCF12H00230077

@@Anson Cheung Could you help to take a look this error?If anything other log please ping me.Thanks!

> 📎 **image-20250214-032622.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/653ec53b-ad79-463e-97cc-86eb66afa36e)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250214-033039.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3b69ebe2-0ed7-4327-8af4-fd3d77c6bd0e)
2. 📎 **image-20250214-032622.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/653ec53b-ad79-463e-97cc-86eb66afa36e)

## 相關資訊

- **Jira:** [BE-1002](https://ctil.atlassian.net/browse/BE-1002)
- **解決方式:** Done
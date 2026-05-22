---
project: BE
issue_key: BE-665
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-665"
created: 2022-11-01
resolved: 2023-01-06
resolution: Done
has_images: True
---

# BE-665: Pop up an api error after click Columns in Vendor Delivery Note

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.0
> **解決日期:** 2023-01-06
> **負責人:** Jerry Wong
> **組件:** Backend (Web)

## 問題描述

env: [https://172.16.138.55/ChainStorePlus_AIGLE/rc2001](https://172.16.138.55/ChainStorePlus_AIGLE/rc2001)

Location: 

Process > Stock receive > Vendor delivery note maintenance

Reproduce steps:

1. To Vendor delivery note maintenance

2. Click into one of the records

3. Click Item information tab

4. click Columns: Color / Size / inseam

Existing result:

Pop up an Api error: API Error [Request ID : 2022110110371419] (2022110110371035 Retry )

Object reference not set to an instance of an object.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d39b55a7-fc7f-4537-a669-caeb2920eab1)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d39b55a7-fc7f-4537-a669-caeb2920eab1)

## 相關資訊

- **Jira:** [BE-665](https://ctil.atlassian.net/browse/BE-665)
- **解決方式:** Done
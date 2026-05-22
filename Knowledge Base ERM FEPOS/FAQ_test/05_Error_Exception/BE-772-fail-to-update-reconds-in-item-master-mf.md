---
project: BE
issue_key: BE-772
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-772"
created: 2023-06-21
resolved: 2023-07-27
resolution: Done
has_images: True
---

# BE-772: Fail to update reconds in Item Master (MF0001)

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-07-27
> **負責人:** Jerry Wong
> **組件:** Backend (Web)

## 問題描述

Reproduce steps:

1. Go to Item Master (MF0001)

2. Select one of the item 

3. Edit that item & add Year (5. Attributes II) for the item

4. Click on Save

Existing result:

Pop up an error: Fail to save record (Related screenshot as below)

Testing Env: [https://172.16.138.55/ChainStorePlus_LandsD_QA](https://172.16.138.55/ChainStorePlus_LandsD_QA)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4c673e36-3689-492a-9241-b4d0d5a098db)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4c673e36-3689-492a-9241-b4d0d5a098db)

## 相關資訊

- **Jira:** [BE-772](https://ctil.atlassian.net/browse/BE-772)
- **解決方式:** Done
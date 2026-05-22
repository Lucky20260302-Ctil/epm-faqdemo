---
project: BE
issue_key: BE-1012
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1012"
created: 2025-02-27
resolved: 2025-03-21
resolution: Done
has_images: True
---

# BE-1012: Invalid UPC Code to FASC in Item 1APKTS25KDM001 Mem Bdg K-Tee plain

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2025-03-21
> **負責人:** Jerry Wong
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

HKJC RTM reported that HKJC_FASC.exe gen_link1_skumaster interface has sent an invalid size to FASC.

 

> 📎 **image-20250227-055449.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b8a3abc6-07aa-471a-a87b-53c7f20ab780)（需 Jira 登入）
This is the output file HSRTM_ITEMMASTER. The item 1APKTS25KDM001 sizes is invalid and I suspect they are carried forward from last created item and somehow updated into “edisku” table. The correct size category should be “KDS” instead of “SML”.

> 📎 **image-20250227-055520.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8b4ba361-7d64-4ecf-9c71-f293a67ccc21)（需 Jira 登入）

> 📎 **image-20250227-055611.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0f3b2335-e8c2-4aa8-80b8-74d570bea24e)（需 Jira 登入）

> 📎 **image-20250227-055627.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cbae17fd-2318-43d9-b4ec-f9184456bcb6)（需 Jira 登入）
I found the user was created 1APLTS25KDM002 which size category is SML, and then 1APKTS25DM001 which size category is KDS. However, it inserted the SML sizes to “edisku” table. So that the HSRTM_ITEMMASTER interface exported the wrong size to FASC. I believe the user may create these items continuously without quit the maintenance and cause this problem. Please try to reproduce it and fix the problem.

> 📎 **image-20250227-055738.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b823fe6b-3295-4820-b5a9-612f0eaf3868)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250227-055449.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b8a3abc6-07aa-471a-a87b-53c7f20ab780)
2. 📎 **image-20250227-055520.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8b4ba361-7d64-4ecf-9c71-f293a67ccc21)
3. 📎 **image-20250227-055611.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0f3b2335-e8c2-4aa8-80b8-74d570bea24e)
4. 📎 **image-20250227-055627.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cbae17fd-2318-43d9-b4ec-f9184456bcb6)
5. 📎 **image-20250227-055738.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b823fe6b-3295-4820-b5a9-612f0eaf3868)

## 相關資訊

- **Jira:** [BE-1012](https://ctil.atlassian.net/browse/BE-1012)
- **解決方式:** Done
- **標籤:** UPC
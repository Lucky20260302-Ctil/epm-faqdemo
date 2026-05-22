---
project: FE
issue_key: FE-1817
issue_type: Bug PRD
status: HOLD
faq_score: 8.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, frontend]
jira_url: "https://ctil.atlassian.net/browse/FE-1817"
created: 2025-11-25
resolved: 
resolution: 
has_images: True
---

# FE-1817: [INC3310467] KR new V72 store OC872 till1 keep missing RP file

> **類型:** Bug PRD | **狀態:** HOLD
> **分類:** 錯誤與異常 | **FAQ 分數:** 8.5
> **負責人:** Sang
> **組件:** Frontend

## 問題描述

SOG callout KR new V72 store OC872 till1 keep missing RP file.Till0 is normal.

I remote to Till1 and rollback 2025-11-24 dayend.Nothing error pop out when I rollback dayend.

@@Sang Could you help to take a look this case and double check the till1 FE log if any other something wrong?If anything xconfig to control the RP file generated?

CC @@Joy Li @@pierre.shi 

1.

> 📎 **image-20251125-035052.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9d4eb70f-152c-4316-a23e-27e5ee6795eb)（需 Jira 登入）
2.Checked the T9 log find follow error:

[24/11/2025 19:59:29 -5238]: 2025-11-24 19:59:29-Prepare_Print_DayEnd_Info_DO - Start :
[24/11/2025 19:59:31 -2827]: 2025-11-24 19:59:31-Prepare_Print_DayEnd_Info_DO - End
[24/11/2025 19:59:31 -3127]: 2025-11-24 19:59:31-Init_PrintFunc_DO Failure :Automation error
ClassFactory cannot supply requested class
[24/11/2025 19:59:31 -3137]: 2025-11-24 19:59:31-After Print Dayend - DO

> 📎 **image-20251125-040455.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2d8c100c-b64d-4a35-8e89-0caef9cb5a7a)（需 Jira 登入）

> 📎 **image-20251125-040544.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/764a66ce-b622-4dc3-9cd5-4757d8b0c18d)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251125-035052.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9d4eb70f-152c-4316-a23e-27e5ee6795eb)
2. 📎 **image-20251125-040455.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2d8c100c-b64d-4a35-8e89-0caef9cb5a7a)
3. 📎 **image-20251125-040544.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/764a66ce-b622-4dc3-9cd5-4757d8b0c18d)

## 相關資訊

- **Jira:** [FE-1817](https://ctil.atlassian.net/browse/FE-1817)
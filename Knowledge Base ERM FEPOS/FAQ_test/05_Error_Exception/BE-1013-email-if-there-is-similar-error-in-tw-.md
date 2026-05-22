---
project: BE
issue_key: BE-1013
issue_type: Bug PRD
status: Closed
faq_score: 9.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1013"
created: 2025-02-27
resolved: 2025-05-21
resolution: Done
has_images: True
---

# BE-1013: email - If there is similar error in TW (vip number does not match the customer)

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 9.0
> **解決日期:** 2025-05-21
> **負責人:** Anson Cheung
> **組件:** Data Interface

## 問題描述

@@Bobby @@Anson Cheung @@Cy Lau TW也有电话号码不一致的情况，导致会员同步到CRM失败，重发仍然失败。

Tovi:TW 之前失败的会员已经重传，但是还有部分会员重传也失败。请看下下面会员重传仍然被拒的原因。OCF841T00008010

ACX: OCF841T00008010 CRM 侧手机号为 0971250730 ，接口传过来的手机号是 0938811730

> 📎 **image-20250227-133115.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c5b1975f-508f-4bbb-85fb-7c950ca1e72e)（需 Jira 登入）
1.member OCF841T00008010 issue data:2020-11-11,DB Tel no 0938811730 .                             

> 📎 **image-20250227-133556.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d617a363-a324-46b3-ab73-7456308bbe2e)（需 Jira 登入）
2.dbtmnlogd table for your reference.

> 📎 **image-20250227-134234.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8d2bc5e1-3e11-4e0a-aa12-9187227c0993)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250227-133115.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c5b1975f-508f-4bbb-85fb-7c950ca1e72e)
2. 📎 **image-20250227-133556.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d617a363-a324-46b3-ab73-7456308bbe2e)
3. 📎 **image-20250227-134234.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8d2bc5e1-3e11-4e0a-aa12-9187227c0993)

## 相關資訊

- **Jira:** [BE-1013](https://ctil.atlassian.net/browse/BE-1013)
- **解決方式:** Done
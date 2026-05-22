---
project: MP
issue_key: MP-757
issue_type: Bug PRD
status: Closed
faq_score: 10.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, mp, performance_timeout, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-757"
created: 2025-03-17
resolved: 2025-05-02
resolution: Done
has_images: True
---

# MP-757: [MPOS-83] MPOS v3.30.2 - KSJ MPOS Sales Data Posting Error

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 10.0
> **解決日期:** 2025-05-02
> **負責人:** Daniel Leung
> **組件:** MPOS

## 問題描述

Hi [CY Lau](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Lau_Ching_Yeung%40ctil.com) [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) , for MPOS v3.30.2, except normal sales data(without coupon) able to post, rest kind of data will have below posting error. Kindly help to check.

Testing machine ip: 172.24.253.69(C309)

MPOS API is connect to apawiqwposweb01

MB000023 - Normal sales with MM Coupon( the coupon we verified it able to post with CS2K Transaction), unable to post.

MB000024 - Return sales, unable to post.

MB000025 - Exchange sales, unable to post.

MB000026 - Tax Free sales, unable to post.

MB000027 - Void sales, original sales memo is MB000023, unable to post.

**MB000028 - Normal sales without coupon, able to post.**

> 📎 **image-20250317-032435.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6f7c4a1d-88a4-4f06-a71d-4a9ccac52d28)（需 Jira 登入）
Posting error:

> 📎 **image-20250317-032510.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/45b0d5bd-8c2f-45a8-9039-3b862d1267bb)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250317-032435.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6f7c4a1d-88a4-4f06-a71d-4a9ccac52d28)
2. 📎 **image-20250317-032510.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/45b0d5bd-8c2f-45a8-9039-3b862d1267bb)

## 相關資訊

- **Jira:** [MP-757](https://ctil.atlassian.net/browse/MP-757)
- **解決方式:** Done
---
project: MP
issue_key: MP-455
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-455"
created: 2021-06-16
resolved: 2021-07-20
resolution: Done
has_images: True
---

# MP-455: E-coupon selection screen issue

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2021-07-20
> **負責人:** Kelly Ng
> **組件:** MPOS

## 問題描述

1.) Scan barcode eCoupon no. to redeem, display message.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b9898e00-b17b-49b1-b625-02823e6cddb0)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/34cb41c6-d1c2-4aef-b287-3d12235ac48f)（需 Jira 登入）
 

2.) If the eCoupon has been redeemed, it will no message return in MPOS.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/306bd8b4-4153-4746-bbd1-f270c563a66d)（需 Jira 登入）
(Compared: it will prompt the error message in FE POS)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/08cfb8e1-933c-4cd3-9d50-c799b5cb72ce)（需 Jira 登入）
 

3) If the eCoupon is not existed, it will no message return in MPOS.

(Compared: it will prompt the error message in FE POS)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/16ac5c7c-3978-46d7-ae54-4b4d78ff7a0c)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b9898e00-b17b-49b1-b625-02823e6cddb0)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/34cb41c6-d1c2-4aef-b287-3d12235ac48f)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/306bd8b4-4153-4746-bbd1-f270c563a66d)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/08cfb8e1-933c-4cd3-9d50-c799b5cb72ce)
5. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/16ac5c7c-3978-46d7-ae54-4b4d78ff7a0c)

## 相關資訊

- **Jira:** [MP-455](https://ctil.atlassian.net/browse/MP-455)
- **解決方式:** Done
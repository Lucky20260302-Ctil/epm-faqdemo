---
project: FE
issue_key: FE-1684
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1684"
created: 2025-04-29
resolved: 
resolution: 
has_images: True
---

# FE-1684: [CS-1419] 75 - not able to select CDP coupon during deposit settlement

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.0
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Dear ALL,

Testing QA : OCQA1-0        10.33.248.4

 

1.deposit memo: 00000584  created on 2025-04-29.

With CDP coupon phone no:15008476947

Member NO: OCQA1TC00000091

> 📎 **image-20250429-083551.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3b532fc0-340e-4e79-899d-186f92727268)（需 Jira 登入）
2.选择"F1-结算"，跳到payment 界面后不会自动弹出 CDP coupon.

> 📎 **image-20250429-083632.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4dfc7f16-8355-40f0-b50d-74db26a09a8d)（需 Jira 登入）

> 📎 **image-20250429-083659.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b926ca55-90d2-48c8-86aa-8d39e8277a89)（需 Jira 登入）
3.选择 “F2-修改”，跳到deposit主界面，点击“支付”;

> 📎 **image-20250429-083916.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/09b4b96e-e1d3-42f7-949c-20711203569a)（需 Jira 登入）

> 📎 **image-20250429-084008.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a4192132-cc85-429f-984a-15588b2900bd)（需 Jira 登入）

4.点击“支付”button，跳到payment界面后，这时会自动弹出 “您要选择电子优惠券吗？”

> 📎 **image-20250429-084148.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c122264d-96c4-495a-9e9e-f230f7d534b7)（需 Jira 登入）
5.点击“确认”后，可以看到并且选择会员优惠券。

> 📎 **image-20250429-084219.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d18abe2c-33b6-4484-997d-5cba4514e308)（需 Jira 登入）

> 📎 **image-20250429-084849.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/32bf6f3d-69bd-4f47-8df0-2551a448173b)（需 Jira 登入）
6.

> 📎 **image-20250429-084949.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e69f157c-f2ea-4ebd-b466-b976f40b3d44)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250429-083551.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3b532fc0-340e-4e79-899d-186f92727268)
2. 📎 **image-20250429-083632.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4dfc7f16-8355-40f0-b50d-74db26a09a8d)
3. 📎 **image-20250429-083659.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b926ca55-90d2-48c8-86aa-8d39e8277a89)
4. 📎 **image-20250429-083916.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/09b4b96e-e1d3-42f7-949c-20711203569a)
5. 📎 **image-20250429-084008.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a4192132-cc85-429f-984a-15588b2900bd)
6. 📎 **image-20250429-084148.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c122264d-96c4-495a-9e9e-f230f7d534b7)
7. 📎 **image-20250429-084219.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d18abe2c-33b6-4484-997d-5cba4514e308)
8. 📎 **image-20250429-084849.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/32bf6f3d-69bd-4f47-8df0-2551a448173b)
9. 📎 **image-20250429-084949.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e69f157c-f2ea-4ebd-b466-b976f40b3d44)

## 相關資訊

- **Jira:** [FE-1684](https://ctil.atlassian.net/browse/FE-1684)
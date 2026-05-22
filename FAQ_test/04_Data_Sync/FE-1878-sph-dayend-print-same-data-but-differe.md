---
project: FE
title: "FE-1878: [SPH] Dayend Print - Same Data but different printout in V72 & V75"
issue_key: FE-1878
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, day-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1878"
created: 2026-02-04
resolved: 2026-02-11
resolution: Done
has_images: True
---

# FE-1878: [SPH] Dayend Print - Same Data but different printout in V72 & V75

## 問題描述

Here is the different printout

v75:

> 📎 **image-20260205-041504.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/16bab45e-1d8b-4475-9066-6bbe1ead9ef2)（需 Jira 登入）

> 📎 **image-20260205-041641.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9b874a1a-9cb3-4704-b5f5-39c32639182f)（需 Jira 登入）

> 📎 **image-20260205-041808.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/12ab9f78-504e-481b-986a-4a5ba4beea44)（需 Jira 登入）

> 📎 **image-20260205-055356.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b866cd1d-9979-4220-80b8-dcbf2e6151fb)（需 Jira 登入）

> 📎 **image-20260205-055507.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9a664977-c6cc-4d79-a5d4-9c26c7811f8b)（需 Jira 登入）

> 📎 **image-20260205-055609.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/045ab831-94d9-482a-8775-67287dafaf71)（需 Jira 登入）

v72

> 📎 **image-20260205-060111.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/27402f8b-c468-48be-9070-aae4b12cbda9)（需 Jira 登入）

> 📎 **image-20260205-060126.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/298172d6-9fa6-48bb-b098-e919b8c9d08b)（需 Jira 登入）

> 📎 **image-20260205-060200.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/96dce862-2b92-4fbd-ae1c-892b53d38ae0)（需 Jira 登入）

> 📎 **image-20260205-060217.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3499faf5-065e-432f-ae54-cebe3d444cf6)（需 Jira 登入）

> 📎 **image-20260205-060420.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/de04005e-c88e-49ce-bfd0-872993a32d29)（需 Jira 登入）

> 📎 **image-20260205-060430.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/860b8ac2-a211-4714-87ff-4cc7d50c0d25)（需 Jira 登入）

> 📎 **image-20260205-060444.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bf20c235-3fb1-4420-8421-d6082ecaf207)（需 Jira 登入）

The point is 

1. The report of **v75 till all display 5000**.

> 📎 **image-20260205-061608.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1e219722-1a30-4f1f-aa14-9d492f9621d0)（需 Jira 登入）

> 📎 **image-20260205-061835.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c8822597-ebda-4f19-bdb1-955737927bdf)（需 Jira 登入）

And

2.The report of **v75 till all display 0% gift cert**.

> 📎 **image-20260205-061715.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1e3b4639-6b95-4d88-8b78-c4d144f78b7d)（需 Jira 登入）

> 📎 **image-20260205-061740.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/28ed2d89-6a47-4403-9a99-646c911c2f94)（需 Jira 登入）

Here is the Retdata6 after dayend:

\\172.16.183.201\localuser\sportshouse\Temp\72afterdayend.zip



## 附件截圖

1. 📎 **image-20260205-041504.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/16bab45e-1d8b-4475-9066-6bbe1ead9ef2)
2. 📎 **image-20260205-041641.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9b874a1a-9cb3-4704-b5f5-39c32639182f)
3. 📎 **image-20260205-041808.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/12ab9f78-504e-481b-986a-4a5ba4beea44)
4. 📎 **image-20260205-055356.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b866cd1d-9979-4220-80b8-dcbf2e6151fb)
5. 📎 **image-20260205-055507.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9a664977-c6cc-4d79-a5d4-9c26c7811f8b)
6. 📎 **image-20260205-055609.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/045ab831-94d9-482a-8775-67287dafaf71)
7. 📎 **image-20260205-060111.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/27402f8b-c468-48be-9070-aae4b12cbda9)
8. 📎 **image-20260205-060126.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/298172d6-9fa6-48bb-b098-e919b8c9d08b)
9. 📎 **image-20260205-060200.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/96dce862-2b92-4fbd-ae1c-892b53d38ae0)
10. 📎 **image-20260205-060217.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3499faf5-065e-432f-ae54-cebe3d444cf6)
11. 📎 **image-20260205-060420.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/de04005e-c88e-49ce-bfd0-872993a32d29)
12. 📎 **image-20260205-060430.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/860b8ac2-a211-4714-87ff-4cc7d50c0d25)
13. 📎 **image-20260205-060444.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bf20c235-3fb1-4420-8421-d6082ecaf207)
14. 📎 **image-20260205-061608.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1e219722-1a30-4f1f-aa14-9d492f9621d0)
15. 📎 **image-20260205-061835.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c8822597-ebda-4f19-bdb1-955737927bdf)
16. 📎 **image-20260205-061715.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1e3b4639-6b95-4d88-8b78-c4d144f78b7d)
17. 📎 **image-20260205-061740.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/28ed2d89-6a47-4403-9a99-646c911c2f94)


## Jira Comments

> **Sang** (2026-02-05):
>  V75 is 3-Jan report, v72 is 2-Jan report. Please verify

> **Sang** (2026-02-05):
>  Revised program uploaded to \\ds411\share\POS_FE_Release_64\20260205 v750.05R07 - SPH

> **Joseph_Hu** (2026-02-05):
> Fixed After revised V75: till all display normally

> **Automation for Jira** (2026-02-05):
> Issue has been created since Days since: 1 Week since : 0 Issue due date difference Days since :  Weeks since: 

## 相關資訊

- **Jira:** [FE-1878](https://ctil.atlassian.net/browse/FE-1878)
- **解決方式:** Done
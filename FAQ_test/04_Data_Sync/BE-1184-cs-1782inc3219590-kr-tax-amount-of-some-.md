---
project: BE
issue_key: BE-1184
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1184"
created: 2025-09-29
resolved: 
resolution: 
has_images: True
---

# BE-1184: [CS-1782][INC3219590] KR Tax amount of some transactions in OC858 & OC818 are wrong

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **負責人:** Sang
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

@@sang_ko @@Jerry Wong 

Coach team call out that KR store some transactions missing jouinv_vat_amt value on 2025-08-31.

INC3219590,KR incorrect Tax issue on 2025-08-31

1.OC858 - 00012341

> 📎 **image-20250929-060028.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/aea91204-f914-4b89-997f-0dbe76d5e525)（需 Jira 登入）

> 📎 **image-20250929-060100.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2e3fe183-52d7-43d3-827c-d0759c2f9fe2)（需 Jira 登入）
2.OC818-00022437

> 📎 **image-20250929-060127.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0d04113d-b9af-4df5-a553-574a8f790f35)（需 Jira 登入）

> 📎 **image-20250929-060148.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/92e19e5d-4025-4a73-82b6-fa38e9090265)（需 Jira 登入）
3.OC818-00022438

> 📎 **image-20250929-060538.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9bddf743-0255-4de3-b7a8-122b1ee35189)（需 Jira 登入）

> 📎 **image-20250929-060619.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/caa9f8cf-64b9-40fa-aa28-e08ec32fe760)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250929-060028.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/aea91204-f914-4b89-997f-0dbe76d5e525)
2. 📎 **image-20250929-060100.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2e3fe183-52d7-43d3-827c-d0759c2f9fe2)
3. 📎 **image-20250929-060127.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0d04113d-b9af-4df5-a553-574a8f790f35)
4. 📎 **image-20250929-060148.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/92e19e5d-4025-4a73-82b6-fa38e9090265)
5. 📎 **image-20250929-060538.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9bddf743-0255-4de3-b7a8-122b1ee35189)
6. 📎 **image-20250929-060619.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/caa9f8cf-64b9-40fa-aa28-e08ec32fe760)


## Jira Comments

> **Tovi Wang** (2025-09-29):
>    Previously, CN had a tax issue (Jira FE-1514) that was already included in V75. Please check the log below to confirm if KR's tax issue will also be included in V75? Could you help check the RCA of KR tax issue and provide a long term workaround?Thanks! CC   FYI. FE logs:  .  

> **Tovi Wang** (2025-09-30):
>  May I know anything update for this one?Because Coach team are asking me the RCA.Thanks!

> **Automation for Jira** (2025-10-09):
> Issue has been created since Days since: 9 Week since : 1 Issue due date difference Days since :  Weeks since: 

> **Sang** (2025-10-09):
>   OC818-00022438 was created on 2025-8-31. Please re-get dbtrans.sdf and all 8-31 logs

> **Sang** (2025-10-09):
>   OC858-00012341 was created on 2025-8-31. Please re-get 8-31 dbtrans.sdf and all logs

> **Tovi Wang** (2025-10-15):
>    08-31 log已经提供，因为08-31 dbtrans 已被覆盖，所以已经无法copy.

> **Sang** (2025-10-15):
>  Copy dbhist.sdf instead of dbtran.sdf

> **Tovi Wang** (2025-10-22):
>    As talked in teams.Since OC858 & OC818 all are V72 version.Let us keep monitoring the Tax issue in V75 with Coach team.I has explained the deatils to Coach team.Hold on this ticket first.

> **Andrew_Au** (2026-05-05):
>     Should I change the ticket status to close? please confirm.

> **Tovi Wang** (2026-05-07):
> Not call out in V75.Can be closed.

## 相關資訊

- **Jira:** [BE-1184](https://ctil.atlassian.net/browse/BE-1184)
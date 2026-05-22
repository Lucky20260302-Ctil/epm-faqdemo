---
project: BE
issue_key: BE-856
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-856"
created: 2024-05-20
resolved: 2024-10-16
resolution: Done
has_images: True
---

# BE-856: Coach interface change member iyy,idd,imm[CS-845]

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **解決日期:** 2024-10-16
> **負責人:** Jason Wu
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

please reference the below image, after the BE interface updates below file it auto update member iyy,imm,idd values to “0' even though the interface file is blank.

Attached the excel(member that got changed the iyy,imm,idd value) and the interface file for your referance.

> 📎 **image-20240520-035155.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cad64f5f-0948-4813-9ba3-acd28ba05c9c)（需 Jira 登入）

> 📎 **image-20240520-035232.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a4808fc5-c946-4022-aa01-78f1ea9276ed)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240520-035155.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cad64f5f-0948-4813-9ba3-acd28ba05c9c)
2. 📎 **image-20240520-035232.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a4808fc5-c946-4022-aa01-78f1ea9276ed)

## 相關資訊

- **Jira:** [BE-856](https://ctil.atlassian.net/browse/BE-856)
- **解決方式:** Done
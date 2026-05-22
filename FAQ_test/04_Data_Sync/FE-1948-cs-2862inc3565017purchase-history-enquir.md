---
project: FE
issue_key: FE-1948
issue_type: Bug PRD
status: Open
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, frontend]
jira_url: "https://ctil.atlassian.net/browse/FE-1948"
created: 2026-05-11
resolved: 
resolution: 
has_images: True
---

# FE-1948: [CS-2862][INC3565017]Purchase History enquire only display last 5 transaction 

> **類型:** Bug PRD | **狀態:** Open
> **分類:** 資料與同步 | **FAQ 分數:** 7.0
> **負責人:** Joy Li
> **組件:** Frontend

## 問題描述

Email Subject: TW Members info in CS2K are not synced with CRM 

Symptom:
For example, customer owns 10 transactions in 2025/06/30-2026/04/17, but Purchase History enquire only able to view the last 5 transaction
想詢問筆數上限是五單，是有辦法優化的嗎? 因為現在的呈現狀態不是分成很多頁，但一頁5筆，而是不管選擇什麼區間，都只會顯示間最新的5筆，這樣對於前線來說查詢極為不便

舉例：假如有位顧客於2025/06/30-2026/04/17整年總共消費了10單，但SA事先並無法得知，所以用這個區間去查詢的時候，就永遠只會顯示最後的那5單，會需要不斷來回調整時間區段

1.

Member code: OC7170T00016428
Member phone: 0932345204

search time:2026-04-26 16:18:25

> 📎 **image-20260511-073119.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/501b9b1d-7a43-4705-84af-d3dac6e8c8db)（需 Jira 登入）
2.Member code: OC7170T00016428 have

> 📎 **image-20260511-074832.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c34f2091-9222-424a-a61d-e284a7663b3e)（需 Jira 登入）
3.request info

> 📎 **image-20260511-075226.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/932a68ef-b7b5-434e-8b78-9f72be087e08)（需 Jira 登入）
4.response info

> 📎 **image-20260511-075256.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/83faa095-44ed-4815-9d5c-79c78dc485bd)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260511-073119.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/501b9b1d-7a43-4705-84af-d3dac6e8c8db)
2. 📎 **image-20260511-074832.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c34f2091-9222-424a-a61d-e284a7663b3e)
3. 📎 **image-20260511-075226.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/932a68ef-b7b5-434e-8b78-9f72be087e08)
4. 📎 **image-20260511-075256.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/83faa095-44ed-4815-9d5c-79c78dc485bd)


## Jira Comments

> **Tovi Wang** (2026-05-11):
>  API log here for your further checking.

> **Tovi Wang** (2026-05-21):
> Hi    As talked in before.Please double check and confirm this issue if need to program enhancemnet. In the Purchase History page.I had confirmed There are all NOT 'Next Page' button on both of PRC & TW region.

## 相關資訊

- **Jira:** [FE-1948](https://ctil.atlassian.net/browse/FE-1948)
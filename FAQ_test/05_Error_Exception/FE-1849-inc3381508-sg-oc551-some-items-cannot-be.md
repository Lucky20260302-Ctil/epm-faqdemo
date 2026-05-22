---
project: FE
issue_key: FE-1849
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, frontend]
jira_url: "https://ctil.atlassian.net/browse/FE-1849"
created: 2026-01-09
resolved: 
resolution: 
has_images: True
---

# FE-1849: [INC3381508] SG OC551 Some items cannot be printed from POS system

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **負責人:** Sang
> **組件:** Frontend

## 問題描述

**Mastconv Data: \\ds411\share\JIRA\FE-1849\mastconv_SG_20260111.zip**

dbtrans Data:  [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d5caa8c2-e7e3-4041-9326-6ce9b9356eba) 

Symptom:
Some items cannot be found and printed from POS system.

Troubleshooting:
1.The items able to find in Sales Page, but cannot find in label printing page.
2.User provided the list.
3.Resaved all issue items on BE,Issue still.

Device information:
Till 2

Issue items:
CCC23 B4MPL
CCM57 B4MPL
CCU00 B4MPL
CCX06 B4/N4
CCX07 B4MPL
CDG71 B4S0M
CDZ64 B4MPL
CR652 B4MPL
CU044 B4MPL
CW616 B4MPL
CCC42 B4/N4

1.Search by item CCC23,But NOT found the bar code 196395963683 in search result page.

@@Sang @@Cy Lau Could you help to further checking and find the RCA?

CC @@Joy Li @@pierre.shi 

> 📎 **1.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0a8ec89f-4b23-4412-8bb2-de478d59a11b)（需 Jira 登入）
2.We can find the item searching by bar code 196395963683.

> 📎 **2.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e4059c1c-d064-4cd4-a5a8-ff39844739d9)（需 Jira 登入）
3.The items able to find in Sales Page

> 📎 **3.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2e13fbc6-82d8-4dd1-9210-a8266b3abcb9)（需 Jira 登入）


## 附件截圖

1. 📎 **1.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0a8ec89f-4b23-4412-8bb2-de478d59a11b)
2. 📎 **2.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e4059c1c-d064-4cd4-a5a8-ff39844739d9)
3. 📎 **3.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2e13fbc6-82d8-4dd1-9210-a8266b3abcb9)

## 相關資訊

- **Jira:** [FE-1849](https://ctil.atlassian.net/browse/FE-1849)
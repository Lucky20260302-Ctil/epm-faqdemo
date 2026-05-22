---
project: FE
title: "FE-1820: [INC3317824] MY OC600 dayend issue"
issue_key: FE-1820
issue_type: Bug PRD
status: Open
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, day-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1820"
created: 2025-11-26
resolved: 
resolution: 
has_images: True
---

# FE-1820: [INC3317824] MY OC600 dayend issue

## 問題描述

MY 最近频繁有dayend issue,检查发现是会员名字有特殊字符导致posting的时候有报错

1.

> 📎 **image-20251126-063448.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8a9c696b-1c7c-48fc-985e-fe25682842b5)（需 Jira 登入）

2.

34		OC600WM00556051	??? ‘	M	--	1982	OC600	20251125	18909718203	18209718203	???	‘			20251125	C	20261125		19820402		--									

> 📎 **image-20251126-063419.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/757f3df9-10d8-4262-89fd-f24d125ec834)（需 Jira 登入）
3.FE capture:

> 📎 **image-20251128-015021.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a5510f98-8e28-418a-b023-ee5daa1e71ff)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251126-063448.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8a9c696b-1c7c-48fc-985e-fe25682842b5)
2. 📎 **image-20251126-063419.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/757f3df9-10d8-4262-89fd-f24d125ec834)
3. 📎 **image-20251128-015021.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a5510f98-8e28-418a-b023-ee5daa1e71ff)

## 相關資訊

- **Jira:** [FE-1820](https://ctil.atlassian.net/browse/FE-1820)
---
project: MP
title: "MP-794: [INC3143602]2 SKU Color Not Found on Barcode print"
issue_key: MP-794
issue_type: Bug DEV
status: Test in Progress
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, frontend]
jira_url: "https://ctil.atlassian.net/browse/MP-794"
created: 2025-08-19
resolved: 
resolution: 
has_images: True
---

# MP-794: [INC3143602]2 SKU Color Not Found on Barcode print

## 問題描述

[INC3143602]SG region,OC554 POS v75,2 SKU Color Not Found on Barcode print

CY200 B4/N4
CI032 B4/N4

 can be found in DB and BE, but FE still cannot find these color

> 📎 **image-20250819-111647.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/afaea124-5bcc-46e3-819d-3df6ce58737f)（需 Jira 登入）
OCF61till1 can use normally, compare the two item in dbmas, it looks like the same.

> 📎 **image-20250819-111810.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ee653688-95f6-4eb5-a6f1-9439f7ebbc05)（需 Jira 登入）

> 📎 **image-20250819-111846.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/01b3df87-9312-4adb-8e74-58a1d3bc8c5c)（需 Jira 登入）
I remoted to store and check the two item in barcode print mode and can’t find

> 📎 **image-20250819-112028.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/368683da-e528-4878-9eba-a41b570b2526)（需 Jira 登入）

> 📎 **image-20250819-112103.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/38dc80a6-1311-456f-97ac-ee5ad7378018)（需 Jira 登入）
below are the logs:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/872b98ef-4b4e-4f5b-9099-68c92419202b)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20250819-111647.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/afaea124-5bcc-46e3-819d-3df6ce58737f)
2. 📎 **image-20250819-111810.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ee653688-95f6-4eb5-a6f1-9439f7ebbc05)
3. 📎 **image-20250819-111846.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/01b3df87-9312-4adb-8e74-58a1d3bc8c5c)
4. 📎 **image-20250819-112028.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/368683da-e528-4878-9eba-a41b570b2526)
5. 📎 **image-20250819-112103.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/38dc80a6-1311-456f-97ac-ee5ad7378018)
6. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/872b98ef-4b4e-4f5b-9099-68c92419202b)

## 相關資訊

- **Jira:** [MP-794](https://ctil.atlassian.net/browse/MP-794)
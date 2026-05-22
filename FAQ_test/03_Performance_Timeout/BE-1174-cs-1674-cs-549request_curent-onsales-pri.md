---
project: BE
title: "BE-1174: [CS-1674] [CS-549]Request_Curent onsales price logic is not able to match business requirement"
issue_key: BE-1174
issue_type: Task
status: Closed
faq_score: 4.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1174"
created: 2025-09-12
resolved: 
resolution: 
has_images: True
---

# BE-1174: [CS-1674] [CS-549]Request_Curent onsales price logic is not able to match business requirement

## 問題描述

Issue Detail:

 

In CS2000, once onsales price is expired, it will insert a new onsale price same as retail price to DB.

 

take 77840 B4P1Y in MY region as example

> 📎 **image-20250912-034417.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/261c4ddf-672c-450a-9b71-fcf92bd4dc32)（需 Jira 登入）
 on 20220123 this item had an event and had 50% off at that day.  after it, CS2000 will insert a new onsale price "520.00" to DB and make sure onsale price is same as retail price, so the price was correct on CS2000 Frontend.

but this logic will have issue if retail price is changed.

in this case 77840 B4P1Y retail price has been changed from 520 to 550 in 2025. but SAP will only push new retail price to CS2000. Since there is a existing onsale price "520.00" in CS2000, the price on CS2000 FE will be "520.00" not the "550.00"



## 附件截圖

1. 📎 **image-20250912-034417.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/261c4ddf-672c-450a-9b71-fcf92bd4dc32)

## 相關資訊

- **Jira:** [BE-1174](https://ctil.atlassian.net/browse/BE-1174)
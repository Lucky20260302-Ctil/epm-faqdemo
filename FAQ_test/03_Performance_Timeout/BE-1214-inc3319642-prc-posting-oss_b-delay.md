---
project: BE
title: "BE-1214: [INC3319642] PRC Posting OSS_B delay"
issue_key: BE-1214
issue_type: Bug PRD
status: Selected for Development (migrated)
faq_score: 9.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1214"
created: 2025-11-27
resolved: 
resolution: 
has_images: True
---

# BE-1214: [INC3319642] PRC Posting OSS_B delay

## 問題描述

1.

2025-11-27 09:25:52 SOG callout OSS_B delay issue.

use csdata11_70
select top 100 * from pstlog with (nolock) where pstlog_date = '2025-11-27' and pstlog_node = 'OSS_B'
order by pstlog_date desc, pstlog_time DESC

 select * from sqlpcdossb
---update sqlpcdossb set sqlpcd_post = 'E'  
where sqlpcd_post_ref like 'acp20251127091928.OCF85___0%'                                                                                                                          

> 📎 **image-20251128-054654.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c21f5697-0a66-41b2-bc1e-9739b1f5e813)（需 Jira 登入）
2.Checked pstlog table found that the issue caused by stuck file acp20251127091928.OCF85___0 with follow error:

83	20251127	091003	OCF85	0	z25112606	27	 Load Data Failure
已成功与服务器建立连接，但是在登录前的握手期间发生错误。 (provider: Shared Memory Provider, error: 0 - 管道已结束。)	
I also can find follow error in PCDBAK file.@@Sang Please help to further checking the RCA.

CC @@Joy Li @@pierre.shi 

> 📎 **image-20251128-054820.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ff31b9ae-e22c-4181-916c-a73d778e82c2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251128-054654.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c21f5697-0a66-41b2-bc1e-9739b1f5e813)
2. 📎 **image-20251128-054820.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ff31b9ae-e22c-4181-916c-a73d778e82c2)

## 相關資訊

- **Jira:** [BE-1214](https://ctil.atlassian.net/browse/BE-1214)
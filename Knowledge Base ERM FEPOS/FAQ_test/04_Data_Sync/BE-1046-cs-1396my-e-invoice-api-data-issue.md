---
project: BE
issue_key: BE-1046
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1046"
created: 2025-04-08
resolved: 2026-05-05
resolution: Done
has_images: True
---

# BE-1046: [CS-1396]MY E-Invoice API data issue

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.5
> **解決日期:** 2026-05-05
> **負責人:** Anson Cheung
> **組件:** Data Interface

## 問題描述

Coach team callout BDO receive incomplete sales amt data for bellow 2 sales memo.

After checked the log,I just only find the first item sales data in log,But missing the second item sales data.Please help to double check and confirm the RCA?Thanks!

1. 

OCF77-20229270 2025-03-18

OCF79-10119181 2025-03-20

> 📎 **image-20250407-083329.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/56a4c121-b26f-4fea-918f-d9e32298080e)（需 Jira 登入）
2.OCF77-20229270 2025-03-18

> 📎 **image-20250407-084231.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1b109532-f0a9-4aef-b07f-3c8c997122c1)（需 Jira 登入）

> 📎 **image-20250407-084905.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/67b84273-11dc-4402-96b0-c0668b687b31)（需 Jira 登入）
3.OCF79-10119181 2025-03-20

> 📎 **image-20250407-084309.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fefe1247-38b8-476d-860d-df27dd542694)（需 Jira 登入）

> 📎 **image-20250407-084925.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0b153441-8b1b-433a-a173-cddc4ebd4e2f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250407-083329.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/56a4c121-b26f-4fea-918f-d9e32298080e)
2. 📎 **image-20250407-084231.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1b109532-f0a9-4aef-b07f-3c8c997122c1)
3. 📎 **image-20250407-084905.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/67b84273-11dc-4402-96b0-c0668b687b31)
4. 📎 **image-20250407-084309.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fefe1247-38b8-476d-860d-df27dd542694)
5. 📎 **image-20250407-084925.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0b153441-8b1b-433a-a173-cddc4ebd4e2f)


## Jira Comments

> **Tovi Wang** (2025-04-08):
>   I remember there are interface enhance in Jira   and the enhancement is already deployed to PRD.Could you help to double check and confirm if it is the same RCA with before?Log for your reference.Thanks!  

> **Anson Cheung** (2025-04-09):
>  This case has same cause with   . By config, program scans the memo not within 10 mins, but the posting is done after 18 mins. I suggest setting the  scanDelayMin  config to 20.

> **Tovi Wang** (2025-04-09):
>  Many Thanks for your double confirm.Can I directly updating the  scanDelayMin  config to 20 in AWS app server after Coach team approved it?

> **Anson Cheung** (2025-04-09):
>  yes

> **Tovi Wang** (2025-04-10):
> Sorry  ,I have one more question.第一个 item 和第二个 item posting到DB的时间几乎一致，相差不到1秒。以这个sample来看，scanning job是从什么时候开始到什么时候结束呀？Coach Team 担心即使把 scanDelayMin  setting改到20，如果后面有的单子30分钟之后才posting到DB,会不会可能又发生类似的issue?谢谢！

> **Anson Cheung** (2025-04-10):
>   scanning time is around 19:35 - 19:36. Note that the log time is 19:36:03.9085 doesn't mean all the records within this time always be scanned, there may be a latency.  And yes, if the posting time is posted at 30 min after the jouinv create time, same issue will be occurred. You may discuss with Coach team to arrange a appropriate delay time.

> **Automation for Jira** (2026-05-05):
> Issue has been created since Days since: 391 Week since : 55 Issue due date difference Days since :  Weeks since: 

## 相關資訊

- **Jira:** [BE-1046](https://ctil.atlassian.net/browse/BE-1046)
- **解決方式:** Done
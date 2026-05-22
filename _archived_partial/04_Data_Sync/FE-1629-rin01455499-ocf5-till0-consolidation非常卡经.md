---
project: FE
issue_key: FE-1629
issue_type: Bug DEV
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end-v720.02
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1629
created: '2025-02-24'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
---
# FE-1629: [RIN01455499] OCF5 till0 consolidation非常卡，经常要10+分钟，且长时间处于无响应状态

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.0
> **負責人:** Ken Wang
> **組件:** Front End v720.02

## 問題描述

[RIN01455499] OCF5 till0 consolidation非常卡，经常要10+分钟，且长时间处于无响应状态.

OCF5: pos v72

测试时间点1： 2025-02-21在15:19左右做19号的consolidation

测试时间点2和3：16:30和16:48左右分别做19号及20号的consolidation

检查日志没什么报错，但是有长时间卡顿

> 📎 **111.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3f81cbed-d89d-443e-be98-a6aa127ed34e)（需 Jira 登入）

> 📎 **222.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d6b082a9-c487-46ac-accb-8fc8e8caf190)（需 Jira 登入）
且前台会长时间出现无响应状态

> 📎 **consolidation.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/447af71e-7827-4fce-83aa-e55f189692df)（需 Jira 登入）
日志已经上传，请帮忙查看。



## 附件截圖

1. 📎 **111.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3f81cbed-d89d-443e-be98-a6aa127ed34e)
2. 📎 **222.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d6b082a9-c487-46ac-accb-8fc8e8caf190)
3. 📎 **consolidation.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/447af71e-7827-4fce-83aa-e55f189692df)


## Jira Comments

> **Sang** (2025-02-25):
>     查查是否有sub-till 沒開機或連不上local network 因為consolidated 需要全部till info. 如缺sub till data, till 0 在做consolidate 時會主動嘗試連去sub till 取資料。如sub till 沒開機或沒連綫，主機在嘗試連機時會等到timeout 才放棄，然後繼續在做不完整的consolid day end

> **pierre.shi** (2025-02-25):
> Hi   谢谢~他们那边子till设置确实挺多的。已告知店铺，并让他们测试。

> **Cy Lau** (2025-02-25):
>  可以問一下其實子till 是不是都是連去同一個local network

> **pierre.shi** (2025-02-25):
> Hi   好的  

> **Cy Lau** (2025-02-25):
> 探問一下就可以，這個他們不知什麼原因很敏感 但我真的很懷疑，Sang 也因為這樣所以加長了Timeout…. 所以問一下網絡分佈就可以，他們不答就不答吧

> **Sang** (2025-02-25):
>    When did CF5 have this problem, try to get logs which have a normal consolidated day end process for comparison

> **Ken Wang** (2025-02-25):
>  Please update the ticket status

> **pierre.shi** (2025-02-25):
> Hi    please help to close the ticket. store user didn’t submit this issue again.

## 相關資訊

- **Jira:** [FE-1629](https://ctil.atlassian.net/browse/FE-1629)
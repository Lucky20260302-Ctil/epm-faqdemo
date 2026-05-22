---
project: BE
issue_key: BE-1017
issue_type: Improvement
status: Closed
tags:
- 04_data_sync
- api
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1017
created: '2025-03-03'
resolved: '2026-05-05'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1017: [Coach][PIPL] When EXIT_PERMIT = 1, upserted value of vip_comp_code need to be 11 in vip table'
---
# BE-1017: [Coach][PIPL] When EXIT_PERMIT = 1, upserted value of vip_comp_code need to be 11 in vip table

## 問題描述

[Coach][PIPL] When EXIT_PERMIT = 1, upserted value of vip_comp_code need to be 11 in vip table

For situation, HK region search a member from CN that no releated records in HK region backend DB

steps:

1. To HK region POS

2. Serach a member with EXIT_PERMIT = 1  from CN that HK region has no this member before

3. insert the member into HK backend DB

4. Check the vip_comp_code of the member in HKHK backend DB

Existing result:

upserted value of vip_comp_code is 10 in vip table

> 📎 **image-20250303-072616.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c5ee5d2a-0b32-4ebe-b613-1b1adc7210b5)（需 Jira 登入）
Expected result:

upserted value of vip_comp_code need to be 11 in vip table

*Testing data:

vip_no = 'OCE020C00200088'



## 附件截圖

1. 📎 **image-20250303-072616.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c5ee5d2a-0b32-4ebe-b613-1b1adc7210b5)

## 相關資訊

- **Jira:** [BE-1017](https://ctil.atlassian.net/browse/BE-1017)
- **解決方式:** Done
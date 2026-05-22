---
project: FE
title: "FE-1850: INC3381142 Till 0 Dayend Report Format Issue"
issue_key: FE-1850
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, report]
jira_url: "https://ctil.atlassian.net/browse/FE-1850"
created: 2026-01-09
resolved: 
resolution: 
has_images: True
---

# FE-1850: INC3381142 Till 0 Dayend Report Format Issue

## 問題描述

Symptom:
Till 0 Dayend Report Issue

Troubleshooting:

1. 用户反馈0号机的日结报告，会出两张纸，签名位置会打印到第二页上，很浪费纸张；

2. Till1号机的日结报告是正常；

3. 用户希望设置0号机日结报告全部内容打印在同一张纸上。

> 📎 **image-20260109-030941.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9230841d-2170-4041-8f79-a4c4d1149f43)（需 Jira 登入）
1.@@Sang 查到Till0 的RP file一共有74行，留白了9行。Till1 的RP file一共有65行，留白了6行。

请查看确认为什么till0 留白比till1 留白多了3行？

CC @@Joy Li @@pierre.shi FYI.

> 📎 **image-20260109-031404.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3bdc0e0c-1a75-4d19-99e4-5b1f9688de57)（需 Jira 登入）
2.Till1 的RP file一共有65行，留白了6行。

> 📎 **image-20260109-031614.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/65ed9cd8-5b8d-47dd-9893-fcccbf038d49)（需 Jira 登入）

3.

till0 POS version:75.004.1305.0001

till1 POS version:75.004.1100.0010

> 📎 **image-20260109-030701.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/97ff4e1e-6af6-4be4-aca1-999521d27608)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260109-030941.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9230841d-2170-4041-8f79-a4c4d1149f43)
2. 📎 **image-20260109-031404.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3bdc0e0c-1a75-4d19-99e4-5b1f9688de57)
3. 📎 **image-20260109-031614.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/65ed9cd8-5b8d-47dd-9893-fcccbf038d49)
4. 📎 **image-20260109-030701.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/97ff4e1e-6af6-4be4-aca1-999521d27608)

## 相關資訊

- **Jira:** [FE-1850](https://ctil.atlassian.net/browse/FE-1850)
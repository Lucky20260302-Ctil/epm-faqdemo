---
project: FE
issue_key: FE-1734
issue_type: Bug DEV
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end-v750.01r01a
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1734
created: '2025-07-23'
resolved: '2025-09-08'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1734: [INC3104662]PRC region, V75, on 19th Jul, Till 0 missing the Mpos dayend report'
---
# FE-1734: [INC3104662]PRC region, V75, on 19th Jul, Till 0 missing the Mpos dayend report

## 問題描述

PRC region, V75, on 19th Jul, Till 0 missing the Mpos dayend report

从T9报告上看，19号till0dayend report出来以后，直接consolidation了。丢掉了20号dayend时line1885至1905dayend结束的那段流程，而直接跳到了consolidation的流程。

> 📎 **image (23).png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/89c960cc-e1d5-44b0-84ce-8f32447f1e88)（需 Jira 登入）

> 📎 **image (24).png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/34a89d5e-d73e-4030-83d4-774d0db15a73)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e1d13ec6-2902-4b88-a7fc-3700abd91f77)（需 Jira 登入）



## 附件截圖

1. 📎 **image (23).png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/89c960cc-e1d5-44b0-84ce-8f32447f1e88)
2. 📎 **image (24).png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/34a89d5e-d73e-4030-83d4-774d0db15a73)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e1d13ec6-2902-4b88-a7fc-3700abd91f77)

## 相關資訊

- **Jira:** [FE-1734](https://ctil.atlassian.net/browse/FE-1734)
- **解決方式:** Done
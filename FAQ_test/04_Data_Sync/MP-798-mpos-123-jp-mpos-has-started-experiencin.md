---
project: MP
title: "MP-798: [MPOS-123] JP MPOS has started experiencing situations where scanning product A brings up product B's information"
issue_key: MP-798
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-798"
created: 2025-09-08
resolved: 
resolution: 
has_images: True
---

# MP-798: [MPOS-123] JP MPOS has started experiencing situations where scanning product A brings up product B's information

## 問題描述

refer to INC3180836， kindly provide the RCA.

The scanned SKU is not the same as the displayed SKU on Mpos
Version:75.004.1305.0001
Mpos: Local iis
Mpos version:3.30.3
Troubleshooting：
1.All Mpos have the same issue
2.After restarting IIS, it returned to normal, but after a period of time, the same problem occurred again
3.For example, the scanned SKU is CAL17, but the Mpos displays CW329

> 📎 **image-20250908-065052.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4aa85b07-bf53-4dd6-8a0a-7dd8bf53c187)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250908-065052.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4aa85b07-bf53-4dd6-8a0a-7dd8bf53c187)


## Jira Comments

> **Tovi Wang** (2025-09-08):
> Waiting SOG team double confirm the issue details with store in TMR. CC   

> **Joy Li** (2025-09-09):
> Log copied from J804 till 0 IIS folder on 2025-09-09

> **Cy Lau** (2025-09-09):
> Scanned 4 times 196395775941

> **Cy Lau** (2025-09-09):
> 5-Sept :  Only 1 time

> **Tovi Wang** (2025-09-18):
> User mis-operation and mis-understanding.Closed ticket.

## 相關資訊

- **Jira:** [MP-798](https://ctil.atlassian.net/browse/MP-798)
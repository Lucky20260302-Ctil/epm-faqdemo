---
project: MP
title: "MP-816: MPOS NZ Rounding incorrect when change is ending in 6¢"
issue_key: MP-816
issue_type: Bug QA
status: Open
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, mp, performance_timeout, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-816"
created: 2026-03-04
resolved: 
resolution: 
has_images: True
---

# MP-816: MPOS NZ Rounding incorrect when change is ending in 6¢

## 問題描述

MPOS: When the price is 738.34 and the cash is 739. the original change should be 0.66, after rounding, it should be 0.70

> 📎 **image-20260304-092851.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e6b89d98-7e7e-4b3a-bca6-bd9ffdb3b3d0)（需 Jira 登入）

Here is the same case in POS:

> 📎 **image-20260304-093048.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/33aa9fb9-63e2-499e-bd11-d590ed00eaa2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260304-092851.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e6b89d98-7e7e-4b3a-bca6-bd9ffdb3b3d0)
2. 📎 **image-20260304-093048.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/33aa9fb9-63e2-499e-bd11-d590ed00eaa2)

## 相關資訊

- **Jira:** [MP-816](https://ctil.atlassian.net/browse/MP-816)
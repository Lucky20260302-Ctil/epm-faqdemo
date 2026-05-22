---
project: MP
title: "MP-736: [CS-1284] HK OC501 - transactions on Nov 20 was wrongly booked into Nov 15. - RIN01426108"
issue_key: MP-736
issue_type: Change Request
status: Closed
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-736"
created: 2024-12-09
resolved: 2025-03-06
resolution: Done
has_images: True
---

# MP-736: [CS-1284] HK OC501 - transactions on Nov 20 was wrongly booked into Nov 15. - RIN01426108

## 問題描述

There was a MPOS issue happened at OC501 on Nov. 20th.  Helpdesk Case number **RIN01426108.**

One of the transactions on Nov 20 was wrongly booked into Nov 15.

memo number is MA012864.

Because not found in intraday transactions, asked to open a new sales memo MA012865 and was successfully logged into transaction data.

in Dec.3, A/C found mismatch transactions, and found the issue.

**Log: \\172.16.183.201\localuser\support\JIRA_DB\MP-736\**

> 📎 **image-20241209-095232.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bab7ef3f-551d-4875-ad33-dd1d305ea0fd)（需 Jira 登入）

> 📎 **2024-12-09_175407-20241209-095409.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0156adf1-d235-4371-b328-cb97708ae089)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241209-095232.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bab7ef3f-551d-4875-ad33-dd1d305ea0fd)
2. 📎 **2024-12-09_175407-20241209-095409.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0156adf1-d235-4371-b328-cb97708ae089)

## 相關資訊

- **Jira:** [MP-736](https://ctil.atlassian.net/browse/MP-736)
- **解決方式:** Done
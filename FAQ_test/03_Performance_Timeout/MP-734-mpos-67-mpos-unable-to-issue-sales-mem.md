---
project: MP
title: "MP-734: [MPOS-67] MPOS - Unable to issue sales memo If login account is different compare to 'Sales staff' & 'Cashier' we selected"
issue_key: MP-734
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, mp, performance_timeout, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-734"
created: 2024-12-03
resolved: 2025-02-24
resolution: Done
has_images: True
---

# MP-734: [MPOS-67] MPOS - Unable to issue sales memo If login account is different compare to 'Sales staff' & 'Cashier' we selected

## 問題描述

 for the release 'MPOS_3.29.4 ver 3' you shared today, we found that, if If login account is different compare to 'Sales staff' & 'Cashier' we selected, then system will pop-up below error message. Kindly help to check.

BTW, I tested with other api version, also have this issue, I guess it's cause by IPA?

Testing machine IP: 10.33.248.8(OCQ93)

Region: 13, **apawiqwposweb24**

IPA Version: 3.29.4

Login account is: QHUANG

Cashier & Sales staff is: YZHANG

**Log: (API log and IPA log) : \\172.16.183.201\localuser\support\JIRA_DB\MPOS-67\**

> 📎 **image-20241203-080810.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2ddca6a8-314e-4c37-b6cf-caa58902c0c5)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241203-080810.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2ddca6a8-314e-4c37-b6cf-caa58902c0c5)

## 相關資訊

- **Jira:** [MP-734](https://ctil.atlassian.net/browse/MP-734)
- **解決方式:** Done
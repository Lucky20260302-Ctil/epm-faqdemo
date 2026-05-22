---
project: FE
title: "FE-1480: ba&sh affiliate model CR"
issue_key: FE-1480
issue_type: Change Request
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1480"
created: 2024-08-06
resolved: 2024-09-23
resolution: Done
has_images: False
---

# FE-1480: ba&sh affiliate model CR

## 問題描述

[@Jason Wu](mailto:Jason_Wu@ctil.com), [@Sang Ko](mailto:sang_ko@ctil.com) and [@Andrew Au](mailto:Andrew_Au@ctil.com),

 

Please provide the back-end VIP master retrieval configuration setting to Sam for testing asap. Thanks.

 

[@Sang Ko](mailto:sang_ko@ctil.com)

 

Please modify the POS program accordingly. I’ll create a ticket in Jira for our reference.

 

The following changes will be made in the POS program:

1. Mask the phone numbers and retain the last 5 digits (e.g., XXXXX 34567).

2. Implement exact search in the Member profile screen.

3. Disable the Advanced Search function.

4. Ensure that the POS clears VIP data from the local database during the day-end process.



## 相關資訊

- **Jira:** [FE-1480](https://ctil.atlassian.net/browse/FE-1480)
- **解決方式:** Done
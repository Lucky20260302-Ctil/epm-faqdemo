---
project: BE
issue_key: BE-1055
issue_type: SOW
status: Closed
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1055"
created: 2025-04-22
resolved: 2025-06-11
resolution: Done
has_images: False
---

# BE-1055: SOW of changing CAR Interface posting date time

> **類型:** SOW | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 5.5
> **解決日期:** 2025-06-11
> **負責人:** Jerry Wong
> **組件:** Data Interface

## 問題描述

Currently in CAR interface for transaction posting, POS will send data file to CAR and the posting datetime is using backend server datetime in Hong Kong time zone.

It causes a symptom that data datetime is not reflecting the corresponding region datetime especially for Japan and Korea since there is 1 hour time difference between Hong Kong time zones.

 

To resolve this issue, this solution is introduced that putting the transaction date and time into posting date and time fields inside the interface file for sending to CAR. The change will apply to Coach Japan, Coach Korea and Kate Spade Japan.



## 相關資訊

- **Jira:** [BE-1055](https://ctil.atlassian.net/browse/BE-1055)
- **解決方式:** Done
- **標籤:** CAR
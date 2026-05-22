---
project: WEB
issue_key: WEB-221
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, web, workflow_business, ename]
jira_url: "https://ctil.atlassian.net/browse/WEB-221"
created: 2022-05-17
resolved: 2022-05-31
resolution: Done
has_images: False
---

# WEB-221: Bug - Ename duplicate VIP ID

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 6.0
> **解決日期:** 2022-05-31
> **負責人:** Joy Li
> **組件:** eName

## 問題描述

COACH Jira [ARP-22]  Bug - Ename duplicate VIP ID

 

After checking, we confirmed that the issue is caused by two device in same shop click the new member function at same time (time different around 30ms).

Therefore the same VIP no are generated for both device and cause the problem.



## 相關資訊

- **Jira:** [WEB-221](https://ctil.atlassian.net/browse/WEB-221)
- **解決方式:** Done
---
project: BE
issue_key: BE-762
issue_type: SOW
status: Closed
faq_score: 6.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, be, install_deploy, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-762"
created: 2023-06-15
resolved: 2023-07-27
resolution: Done
has_images: False
---

# BE-762: KS SEA CRM Memberson CDP backend Sale journal schedule short period task

> **類型:** SOW | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 6.0
> **解決日期:** 2023-07-27
> **負責人:** Bobby
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

**Develop a program to update transaction to CDP**

1. **Register Transaction to CDP**
 Once the transaction is posted to back-end Sales Journal. ChainStorePlus back end will have a scheduled task to call CDP ‘Search Profile - Simple’, ‘Get Profile Summary’ and then ‘Register Transaction’ API to register the transaction to CDP.

2. **Void Transaction to CDP**
 Once the transaction is posted to back-end Sales Journal. ChainStorePlus back end will have a scheduled task to call CDP ‘Get Transaction’ and then ‘Void Transaction’ API to cancel the transaction in CDP.

 

the program run every 3 mins by hosting on schedule task.

 



## 相關資訊

- **Jira:** [BE-762](https://ctil.atlassian.net/browse/BE-762)
- **解決方式:** Done
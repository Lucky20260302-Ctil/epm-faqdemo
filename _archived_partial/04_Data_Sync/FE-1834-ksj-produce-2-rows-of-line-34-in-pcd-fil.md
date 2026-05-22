---
project: FE
issue_key: FE-1834
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1834
created: '2025-12-16'
resolved: '2026-03-03'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1834: [KSJ] Produce 2 rows of line 34 in pcd file after completed an order with new member created by POS'
---
# FE-1834: [KSJ] Produce 2 rows of line 34 in pcd file after completed an order with new member created by POS

## 問題描述

[KSJ] Produce 2 rows of line 34 in pcd file after completed an order with new member created by POS

Pre-condition: 

WEBAPIUPDATENEWMEMBER=N
WEBAPIUPDATENEWMEMBERATDAYEND=N

Reproduce steps:

1. Set WEBAPIUPDATENEWMEMBER=N
WEBAPIUPDATENEWMEMBERATDAYEND=N

2. Open POS

3. create a new member 

4. completed an order with the new member created by POS

5. Check the pcd file

Existing result:

Produce 2 rows of line 34 in pcd file

> 📎 **image-20251216-024639.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/75f202ba-76fe-4db3-b527-691f4d6eb3b4)（需 Jira 登入）
Affacted version:

7.5.0.04R13E2 (build251215)



## 附件截圖

1. 📎 **image-20251216-024639.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/75f202ba-76fe-4db3-b527-691f4d6eb3b4)


## Jira Comments

> **Automation for Jira** (2025-12-22):
> Issue has been created since Days since: 6 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sherman tse** (2026-03-03):
> Verified on QA

## 相關資訊

- **Jira:** [FE-1834](https://ctil.atlassian.net/browse/FE-1834)
- **解決方式:** Done
---
project: FE
issue_key: FE-1952
issue_type: Bug PRD
status: HOLD
tags:
- 05_error_exception
- error_exception
- faq
- fe
- frontend
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1952
created: '2026-05-14'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1952: [CS-2672] Issue_PRC_INC3520233_OCF516 till0 sales cannot be uploaded to HKMR timely'
---
# FE-1952: [CS-2672] Issue_PRC_INC3520233_OCF516 till0 sales cannot be uploaded to HKMR timely

## 問題描述

Till0 sales cannot be uploaded to HKMR timely 

Worknote from Jira ticket:

我查了下05-14新建的2笔Till0销售可以自动生成ACP file并且正常上传到DB...我没有做任何变更.

请继续监测 OCF516 till0 的销售上传情况。下面截图供参考。

1. 

05-14 做了2笔销售

> 📎 **image-20260515-052453.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/05fbfecc-e322-42a0-a6b1-f862bd891c0e)（需 Jira 登入）
 2.

select * from sqlpcdossb
where sqlpcd_post_ref like 'acp20260514124006.OCF516__0%'
---sales memo: 00002795

select * from sqlpcdossb
where sqlpcd_post_ref like 'acp20260514164006.OCF516__0%'
---sales memo: 00002796

> 📎 **image-20260515-052515.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/40212678-48c7-4f6b-8601-090a12bbc276)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260515-052453.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/05fbfecc-e322-42a0-a6b1-f862bd891c0e)
2. 📎 **image-20260515-052515.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/40212678-48c7-4f6b-8601-090a12bbc276)

## 相關資訊

- **Jira:** [FE-1952](https://ctil.atlassian.net/browse/FE-1952)
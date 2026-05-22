---
project: FE
issue_key: FE-1124
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1124
created: '2022-06-21'
resolved: '2022-06-29'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1124: J812 Cash Denomination missing'
---
# FE-1124: J812 Cash Denomination missing

## 問題描述

Email: Please follow up on INC1814512

 Reproduce step:

1. Input Cash Denomination then click F1 confirm

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7b215a39-e8df-4fa3-9314-9f10973bf01c)（需 Jira 登入）
2. Back to Cash Drawer Tender Count Input and re-enter cash denomination.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e658b088-d651-4880-a76d-fec9fffb994f)（需 Jira 登入）
3. Click F10 Cancel without any change.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/13c3e962-e053-4c3a-abc5-afacfec08e61)（需 Jira 登入）
4. Then finish the day end process. The cash denomination will missing.



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7b215a39-e8df-4fa3-9314-9f10973bf01c)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e658b088-d651-4880-a76d-fec9fffb994f)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/13c3e962-e053-4c3a-abc5-afacfec08e61)

## 相關資訊

- **Jira:** [FE-1124](https://ctil.atlassian.net/browse/FE-1124)
- **解決方式:** Done
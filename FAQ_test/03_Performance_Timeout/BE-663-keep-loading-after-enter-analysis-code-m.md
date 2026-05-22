---
project: BE
issue_key: BE-663
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- backend-(web)
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-663
created: '2022-10-27'
resolved: '2024-03-01'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-663: Keep loading after enter analysis code maintenance page'
---
# BE-663: Keep loading after enter analysis code maintenance page

## 問題描述

env: [https://172.16.138.55/ChainStorePlus_AIGLE/login](https://172.16.138.55/ChainStorePlus_AIGLE/mf8006)

Location:

Table Maintenance > Secondary > Analysis code > Product Analysis code/ Member Analysis code/ Customer Analysis code

Reproduce steps:

1. Create the Code of Product LIne MF7000 / Member Line MF7003 / Customer Line MF7006

2. Create Product MF3003/ Member MF7005/ Customer Analysis code MF7008 & Select code that just created by Product LIne MF7000 / Member Line MF7003 / Customer Line MF7006

3. Go back to Product LIne MF7000 / Member Line MF7003 / Customer Line MF7006

4. Del the Code of Product LIne MF7000 / Member Line MF7003 / Customer Line MF7006

5. Go back to Product/ Member/ Customer Analysis code

6. Click on the Product/ Member/ Customer Analysis code that just create

Existing result:

Keep loading in analysis code maintenance page (member MF7005/ product MF3003 /  customer MF7008)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3399bbcf-82ea-4ef6-abf2-850533148644)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3399bbcf-82ea-4ef6-abf2-850533148644)

## 相關資訊

- **Jira:** [BE-663](https://ctil.atlassian.net/browse/BE-663)
- **解決方式:** Done
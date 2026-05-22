---
project: BE
issue_key: BE-893
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
jira_url: https://ctil.atlassian.net/browse/BE-893
created: '2024-08-22'
resolved: '2024-09-09'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-893: Stock Transfer Receive Recovery Process(IC8001)：modify时，修改Rcvy.Rec.由“1”改为“2”，点击Save，页面一直在loading'
---
# BE-893: Stock Transfer Receive Recovery Process(IC8001)：modify时，修改Rcvy.Rec.由“1”改为“2”，点击Save，页面一直在loading

## 問題描述

Reproduce steps:

1. select Reference No. 'BF0 - T0000002' 

2. 点击modify按钮

3. 修改y.Rec.由“1”改为“2”

4. 点击save

> 📎 **image-20240822-090723.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d3598279-8aae-4203-95ca-d56ec6e5dcb8)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240822-090723.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d3598279-8aae-4203-95ca-d56ec6e5dcb8)

## 相關資訊

- **Jira:** [BE-893](https://ctil.atlassian.net/browse/BE-893)
- **解決方式:** Done
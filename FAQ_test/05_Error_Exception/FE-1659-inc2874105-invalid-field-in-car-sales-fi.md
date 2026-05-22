---
project: FE
issue_key: FE-1659
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- interface
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1659
created: '2025-03-24'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1659: INC2874105 Invalid field in CAR sales files during 3/21-3/23 for KR OCF90 pilot store'
---
# FE-1659: INC2874105 Invalid field in CAR sales files during 3/21-3/23 for KR OCF90 pilot store

## 問題描述

Invalid field in CAR  sales files during 3/21-3/23
Please help to find the root cause of this issue.this is for KR OCF90 pilot store.

1.@@Sang ’H’这一行为什么会有一串“NUL“是从哪里来的？客户输入的嘛还是怎样？

CC @@Cy Lau @@Bobby @@pierre.shi  FYI.

> 📎 **image-20250324-062747.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d1d92e32-2cc0-4268-ab24-b5ce8f52012d)（需 Jira 登入）
2.在TIll0 PC250321.DAT 和 M till PC250321.M file里也能发现。Please help to further checking.

Till0 PC file

> 📎 **image-20250324-062858.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/21498390-2cc9-48fd-8017-a4d6f541d4fb)（需 Jira 登入）
M Till PC file

> 📎 **image-20250324-062920.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7958ee39-2c0e-47b9-bbfb-a71727145789)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250324-062747.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d1d92e32-2cc0-4268-ab24-b5ce8f52012d)
2. 📎 **image-20250324-062858.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/21498390-2cc9-48fd-8017-a4d6f541d4fb)
3. 📎 **image-20250324-062920.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7958ee39-2c0e-47b9-bbfb-a71727145789)

## 相關資訊

- **Jira:** [FE-1659](https://ctil.atlassian.net/browse/FE-1659)
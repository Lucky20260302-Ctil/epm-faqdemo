---
project: FE
issue_key: FE-1851
issue_type: Bug QA
status: DEV Done
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1851
created: '2026-01-09'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1851: [BASH] Member searching behavior become different after applied BASH release for fixing member issue'
---
# FE-1851: [BASH] Member searching behavior become different after applied BASH release for fixing member issue

## 問題描述

[BASH] Member searching behavior become different after applied BASH release for fixing member issue

Reproduce steps:

1. Select a Coach FE with C360 set up

2. Back up for the FE program

3. Apply the BASH release into the FE

4. Open POS & To Member section 

5. Searching for members from C360 by mobile phone: 123 (has more than 1 members)

Coach C360 behavior:

- Pop up a list of member with same mobile phoner result

C360 set up applied with BASH behavior:

- Display a member in member detail page

> 📎 **image-20260109-075323.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a9f9f5de-1683-48b0-b626-b129c681ea76)（需 Jira 登入）
*no config changed

VM: 172.16.138.103
.\sxd

Yan20201104@



## 附件截圖

1. 📎 **image-20260109-075323.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a9f9f5de-1683-48b0-b626-b129c681ea76)

## 相關資訊

- **Jira:** [FE-1851](https://ctil.atlassian.net/browse/FE-1851)
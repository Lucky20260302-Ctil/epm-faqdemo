---
project: MP
issue_key: MP-790
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- faq
- install_deploy
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-790
created: '2025-08-11'
resolved: '2025-08-20'
fix_version: ''
components: []
has_images: true
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'MP-790: 【MPOS-114】CJ MPOS Prod_ J801 Sales page show null ''''button'''''
---
# MP-790: 【MPOS-114】CJ MPOS Prod_ J801 Sales page show null ''button''

## 問題描述

Issue :White button displays on mPOS(Confirmed other pilot stores does not have this issue)

The issue occurs only at J801 after we updated the version(Ver 3.30.3) on 8/6 evening

J801 uploaded the log at 14:40pm on 8/10

Occurs with unspecified users.
The number of white buttons varies depending on the person.
Pressing the buttons does nothing.
The issue disappears after logging off and logging back in.
Reinstalling the app does not resolve the issue—it still occurs.

> 📎 **image-20250811-014746.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8d27be70-e2a0-4879-816e-7070f781a660)（需 Jira 登入）
FE POS version ：75.004.1305.0001

MPOS IPA: 3.30.3(Local IIS)

> 📎 **image-20250811-014823.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bef50f61-91c4-422a-96c7-320bc97a5135)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250811-014746.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8d27be70-e2a0-4879-816e-7070f781a660)
2. 📎 **image-20250811-014823.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bef50f61-91c4-422a-96c7-320bc97a5135)

## 相關資訊

- **Jira:** [MP-790](https://ctil.atlassian.net/browse/MP-790)
- **解決方式:** Done
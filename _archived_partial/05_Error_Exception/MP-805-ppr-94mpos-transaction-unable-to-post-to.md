---
project: MP
issue_key: MP-805
issue_type: Bug PRD
status: Open
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-805
created: '2025-12-22'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-805: [PPR-94]MPOS Transaction unable to post to DB'
---
# MP-805: [PPR-94]MPOS Transaction unable to post to DB

## 問題描述

Neil callout that create MPOS transaction for AU region but unable post to DB. Testing store: OCA213(IP: 10.34.103.17), transaction no: MA000001. kindly help to check

> 📎 **image-20251222-035315.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d0a83754-432c-4307-a616-c7f1661e3cea)（需 Jira 登入）

Troubleshooting:

1.From MPOS API log,We can see the memo MA000001 was created in 2025-12-19 15:51:09

> 📎 **image-20251222-035759.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d7bad6b3-ea73-4516-b835-dc4c479a5110)（需 Jira 登入）
2.And can find the memo in MPOS PC file

> 📎 **image-20251222-040118.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f6b22bb1-02bc-46c6-9b23-271de03679c5)（需 Jira 登入）
3.Upload PCD file：

2025/12/19 15:51:11.203 Create MSMQ to apawiqwposmqs21\PRIVATE$\Server20a
2025/12/19 15:51:11.219 Upload PCD file D:\www\apawiqwposweb24\SanyoService.API.FE_20\App_Data\Shops\oca213\Retdata6\UploadPCD\ACP2025121915511120.OCA213_M Successful

> 📎 **image-20251222-040143.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/59732b6c-5230-4f13-aea8-01587d65ca1a)（需 Jira 登入）
4.@@Cy Lau @@Daniel Leung But I can’t find the MPOS ACP file in polling posting log:

A. 2025-12-19 MQ log not have any MPOS data:

> 📎 **image-20251222-040340.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/55b22ab6-c82a-4011-a92b-dbec24f3a947)（需 Jira 登入）
B. 2025-12-19 posting log not have any MPOS ACP file.

> 📎 **image-20251222-040527.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4960c509-878e-44a5-af6c-22e9e0021d9c)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251222-035315.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d0a83754-432c-4307-a616-c7f1661e3cea)
2. 📎 **image-20251222-035759.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d7bad6b3-ea73-4516-b835-dc4c479a5110)
3. 📎 **image-20251222-040118.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f6b22bb1-02bc-46c6-9b23-271de03679c5)
4. 📎 **image-20251222-040143.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/59732b6c-5230-4f13-aea8-01587d65ca1a)
5. 📎 **image-20251222-040340.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/55b22ab6-c82a-4011-a92b-dbec24f3a947)
6. 📎 **image-20251222-040527.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4960c509-878e-44a5-af6c-22e9e0021d9c)

## 相關資訊

- **Jira:** [MP-805](https://ctil.atlassian.net/browse/MP-805)
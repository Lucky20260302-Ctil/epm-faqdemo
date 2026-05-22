---
project: MP
issue_key: MP-753
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
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-753
created: '2025-03-04'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'MP-753: [RIN01454411]JP - J355  - Mpos : when user enter sales staff/cashier information, the mpos always keep loading'
---
# MP-753: [RIN01454411]JP - J355  - Mpos : when user enter sales staff/cashier information, the mpos always keep loading

## 問題描述

Store user has some problem with mpos
Symptom:

1. when user enter sales staff/cashier information, the mpos always keep lording more than 20mins

Software Version:
IIS: Cloud
IIS Version: 72.0225.0004
MPOS Version: 3.25.1

Troubleshooting:

A. user said the issue often appear on all mpos and they need to reboot the mpos and register the information again.
B. guide user to turn off/on the SDAS01 but issue still.
C. other function like scan the sku or search customer is ok.

> 📎 **image-20250304-013854.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/58e69c79-4e30-4a01-a622-edc46a15dfc6)（需 Jira 登入）
1. [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d6e1a96f-a894-46cf-a32c-fcc888ba4ffb) ,MPOS logs for your further checking.

2.Issue Vedio from store.

> 📎 **ScreenRecording_02-18-2025 18-38-15_1.mp4** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5263919a-23d7-4e78-8066-782ba5ef8eb2)（需 Jira 登入）
3.@@Daniel Leung @@Cy Lau From UI log &,I can see that there are some time no log.Could you help to double check why there are keep loading when user enter staff code&cashier code?What’s the details logic of enter staff code&cashier code?the code info come from Till0 dbsse?Please help to clarify.Thanks!

> 📎 **image-20250304-014612.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bd53238a-0ec0-413e-b091-e50b2261b8c5)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250304-013854.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/58e69c79-4e30-4a01-a622-edc46a15dfc6)
2. 📎 **ScreenRecording_02-18-2025 18-38-15_1.mp4** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5263919a-23d7-4e78-8066-782ba5ef8eb2)
3. 📎 **image-20250304-014612.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bd53238a-0ec0-413e-b091-e50b2261b8c5)

## 相關資訊

- **Jira:** [MP-753](https://ctil.atlassian.net/browse/MP-753)
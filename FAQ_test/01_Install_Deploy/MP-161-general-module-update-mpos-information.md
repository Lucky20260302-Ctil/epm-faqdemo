---
project: MP
issue_key: MP-161
issue_type: Improvement
status: Closed
tags:
- 01_install_deploy
- faq
- install_deploy
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-161
created: '2020-05-05'
resolved: '2020-05-26'
fix_version: ''
components: []
has_images: true
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'MP-161: General Module - Update MPOS Information into BE DB locregister table'
---
# MP-161: General Module - Update MPOS Information into BE DB locregister table

## 問題描述

For easy to verify the MPOS version, MPOS should update version into back end database [locregister] table as same as front end POS. 

Proposed column mapping as below:

- locreg_company = company code

- locreg_loc = Store Code (e.g. OC100)

- locreg_till = Till No. (e.g. MA)

- locreg_computername = MPOS Alias name

- locreg_ip = MPOS IP

- locreg_installedversion = MPOS APP version

- locreg_installeddate = ?

- locreg_opmode = N (Normal mode)

- locreg_msmqservername = MPOS MSMQ Server name

- locreg_updateby = mpos

- locreg_updatedt = Last update date time

- locreg_printer = LASER ??

- locreg_api_ver = MPOS API version

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4173a24e-cd5c-4936-a338-4a24349572fd)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4173a24e-cd5c-4936-a338-4a24349572fd)

## 相關資訊

- **Jira:** [MP-161](https://ctil.atlassian.net/browse/MP-161)
- **解決方式:** Done
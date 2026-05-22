---
project: MP
title: "MP-161: General Module - Update MPOS Information into BE DB locregister table"
issue_key: MP-161
issue_type: Improvement
status: Closed
faq_score: 7.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-161"
created: 2020-05-05
resolved: 2020-05-26
resolution: Done
has_images: True
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
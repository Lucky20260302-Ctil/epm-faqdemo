---
project: MP
title: "MP-801: [MPOS-126] J804 one MPOS shows it has reached the maximum when logging in"
issue_key: MP-801
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-801"
created: 2025-09-19
resolved: 
resolution: 
has_images: True
---

# MP-801: [MPOS-126] J804 one MPOS shows it has reached the maximum when logging in

## 問題描述

[INC3183121]

User has some problems with CJ one MPOS:
Symptom:
MPOS shows it has reached the maximum when logging in
Error: 

Excess Maximum Number Register
Device Excess Maximum Limit

Device information
Name: J723-iphone-01
iOS: 18.6.2
Serial number: H1X9XXKXC4

SOG Checked:

1. User has logout some unused MPOS but issue still

2. Reboot MPOS device but issue still

> 📎 **image-20250919-012946.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7350404d-5618-4e9f-bee0-45b7f977a81c)（需 Jira 登入）

Troubleshooting:

I checked BE locregister table found that J804 has registered 36 MPOS device.

I have some question for this case:

1. But I found that some MPOS locreg_uupdatedt date are still stuck in the previous date and have not been updated to the current [date.Is](http://date.Is) this normal?

2. Does the screenshot error indicate that the J804 MPOS login count for that day has exceeded the maximum login count for that day? What is the maximum daily number of MPOS logins for a store?

3. How can we check and confirm how many MPOS have been successfully logged in on the same day? Do we have any logs to view?Thanks!

> 📎 **1.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/02fd8ed8-a444-48f8-9ca6-c3c2fe4fa471)（需 Jira 登入）

> 📎 **2.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/00fecbbb-a050-4a2d-bb84-ece81f65df80)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250919-012946.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7350404d-5618-4e9f-bee0-45b7f977a81c)
2. 📎 **1.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/02fd8ed8-a444-48f8-9ca6-c3c2fe4fa471)
3. 📎 **2.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/00fecbbb-a050-4a2d-bb84-ece81f65df80)

## 相關資訊

- **Jira:** [MP-801](https://ctil.atlassian.net/browse/MP-801)
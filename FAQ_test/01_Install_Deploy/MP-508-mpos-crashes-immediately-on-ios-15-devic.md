---
project: MP
title: "MP-508: MPOS Crashes Immediately on iOS 15 Device"
issue_key: MP-508
issue_type: Bug DEV
status: Closed
faq_score: 5.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-508"
created: 2021-10-08
resolved: 2021-12-08
resolution: Done
has_images: False
---

# MP-508: MPOS Crashes Immediately on iOS 15 Device 

## 問題描述

After installing MPOS on iOS 15, it crashes immediately. During the investigation, we found out the current development environment is using Flutter 2.0.6, which might be the reason why it crashes on iOS 15.

Solution: we have upgraded the dev env to use Flutter 2.2.0 to make MPOS working on iOS 15.



## 相關資訊

- **Jira:** [MP-508](https://ctil.atlassian.net/browse/MP-508)
- **解決方式:** Done
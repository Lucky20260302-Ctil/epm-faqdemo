---
project: MP
title: "MP-507: MPOS Fails the Installation on iOS 15 Devices"
issue_key: MP-507
issue_type: Bug DEV
status: Closed
faq_score: 7.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-507"
created: 2021-10-08
resolved: 2021-12-08
resolution: Done
has_images: False
---

# MP-507: MPOS Fails the Installation on iOS 15 Devices

## 問題描述

After upgrade to iOS 15, MPOS is prevented to install because the deploy machine was running macOS Catalina (with Xcode 12), which doesn't support code signing for iOS 15.

 

Solution: we have upgraded our machine to macOS Big Sur (with Xcode 13) and re-compiled MPOS in order to install it on iOS 15 device successfully.

 

More details:

[https://developer.apple.com/support/xcode/](https://developer.apple.com/support/xcode/)



## 相關資訊

- **Jira:** [MP-507](https://ctil.atlassian.net/browse/MP-507)
- **解決方式:** Done
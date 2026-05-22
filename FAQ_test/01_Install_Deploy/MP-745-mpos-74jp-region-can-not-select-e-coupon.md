---
project: MP
title: "MP-745: [MPOS-74]JP Region, can not select E-Coupon even the member we selected have available ecoupon"
issue_key: MP-745
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-745"
created: 2025-02-11
resolved: 2025-05-02
resolution: Done
has_images: True
---

# MP-745: [MPOS-74]JP Region, can not select E-Coupon even the member we selected have available ecoupon

## 問題描述

after deploy the patch COACH_MPOSWebAPI_R3.29.5d, we did testing for JP region, we found that in MPOS, even the member we selected have available e-coupon, e-coupon will show as blank when we trying to select it. kindly help to check.

Testing info:

CS2K Testing machine ip: 172.24.253.20(J805)

IPA Version: 3.29.5-20250108.2

API: COACH_MPOSWebAPI_R3.29.5d ( connect to apawiqwposweb24)

Testing vip no#: J101WJ00051712/OCQ92WJ01356793

 

> 📎 **image-20250211-154045.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e8618696-6589-491d-a073-16b6be1abd79)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250211-154045.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e8618696-6589-491d-a073-16b6be1abd79)

## 相關資訊

- **Jira:** [MP-745](https://ctil.atlassian.net/browse/MP-745)
- **解決方式:** Done
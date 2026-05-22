---
project: FE
title: "FE-1856: [CS-1973] INC3399076,KR V75 pilot store  OC825 CS2000  UI daiplay issue"
issue_key: FE-1856
issue_type: Bug PRD
status: Closed
faq_score: 8.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1856"
created: 2026-01-19
resolved: 2026-02-26
resolution: Done
has_images: True
---

# FE-1856: [CS-1973] INC3399076,KR V75 pilot store  OC825 CS2000  UI daiplay issue 

## 問題描述

KR store callout that After upgrading to V75, some parts become Japanese and English.

Confirmed with two other pilot stores OC807 and OC860 that they also have the same issues.

Normal all should display as Korean.

@@Sang @@Cy Lau @@Joy Li I suspect it's a problem with the language pack file settings.Please help to further checking and confirming the language pack file.

Troubleshooting:

1.repaired cs2000 program,issue still.

2.change windows system language from 'English' to  'Korean.'Issue still.

1. 在销售页面有2处显示日语,应该显示韩文。

> 📎 **1.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fbf72d36-0a3f-426b-9860-edd91ac4b4f2)（需 Jira 登入）
2.会员页面显示英文 Purchase History，应该显示韩文。

> 📎 **屏幕截图 2026-01-19 110034.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d13a97f3-c8be-406e-8244-50e7fccb69d4)（需 Jira 登入）
LL coupon notes can only input English after upgrade (previously supported Korean).

COACH say 72 can support Korean. but V75 fail (75.004.1404.0000)

Could you please help to check and confirm? 

> 📎 **image-20260205-013136.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e833434c-3bed-4229-aa5d-06840b59cf0d)（需 Jira 登入）


## 附件截圖

1. 📎 **1.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fbf72d36-0a3f-426b-9860-edd91ac4b4f2)
2. 📎 **屏幕截图 2026-01-19 110034.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d13a97f3-c8be-406e-8244-50e7fccb69d4)
3. 📎 **image-20260205-013136.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e833434c-3bed-4229-aa5d-06840b59cf0d)

## 相關資訊

- **Jira:** [FE-1856](https://ctil.atlassian.net/browse/FE-1856)
- **解決方式:** Done
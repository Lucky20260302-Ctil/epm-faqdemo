---
project: FE
title: "FE-1858: C360 Mmeber search Bad request"
issue_key: FE-1858
issue_type: Bug PRD
status: Open
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1858"
created: 2026-01-22
resolved: 
resolution: 
has_images: True
---

# FE-1858: C360 Mmeber search Bad request

## 問題描述

FE POS search panel shown “Name”
But only first name and last name in C360

> 📎 **image-20260121-235747.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d4dc7628-e227-472f-9805-b16a8f3281e9)（需 Jira 登入）
data input
{
  "Body": "{"MemberNo":"","Name":"layla ","FirstName":"","LastName":"","ID":"","HomePhone":"","MobilePhone":"","Email":"","StaffNo":""}"
}

Boby to C360

  "Body": "{"CustomerLookupRequest":[{"source":"CS2ANZ","brand":"KS","customerid":"","lastname":"","firstname":"","housenumber":"","addressline":"","city":"","state":"","zip":"","country":"","email":"","phonenumber":"","last4digitphone":""}]}"
}

Therefore C360 return bad request.



## 附件截圖

1. 📎 **image-20260121-235747.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d4dc7628-e227-472f-9805-b16a8f3281e9)

## 相關資訊

- **Jira:** [FE-1858](https://ctil.atlassian.net/browse/FE-1858)
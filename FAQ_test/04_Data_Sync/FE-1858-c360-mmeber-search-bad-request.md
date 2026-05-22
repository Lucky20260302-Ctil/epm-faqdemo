---
project: FE
issue_key: FE-1858
issue_type: Bug PRD
status: Open
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1858
created: '2026-01-22'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1858: C360 Mmeber search Bad request'
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
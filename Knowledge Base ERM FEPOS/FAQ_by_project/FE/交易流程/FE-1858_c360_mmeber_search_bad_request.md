---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "FE POS search panel shown “Name”"
root-cause: "待提取"
solution: "_（無 resolution 或 comment 記錄）_"
jira: FE-1858
resolved: 
fix-version: ""
---

# FE-1858: C360 Mmeber search Bad request

## 問題

FE POS search panel shown “Name”
But only first name and last name in C360
data input
{
  "Body": "{"MemberNo":"",<span style="color:#ff5630">"Name":"layla ",</span>"FirstName":"","LastName":"","ID":"","HomePhone":"","MobilePhone":"","Email":"","StaffNo":""}"
}
Boby to C360
"Body": "{"CustomerLookupRequest":[{"source":"CS2ANZ","brand":"KS","customerid":"",<span style="color:#ff5630">"lastname":"","firstname":"",</span>"housenumber":"","addressline":"","city":"","state":"","zip":"","country":"","email":"","phonenumber":"","last4digitphone":""}]}"
}
Therefore C360 return bad request.

## 根因

（需從 Jira 提取）

## 解法

_（無 resolution 或 comment 記錄）_

## 相關資訊

- Jira: [FE-1858](https://ctil.atlassian.net/browse/FE-1858)
- Fix Version: 未記錄
- 解決日期: 未記錄

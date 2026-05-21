---
tags: [faq, WEB, bug]
component: "Backend API"
symptom: "CJ Line QA environment returns HTTP 400 error when calling specific backend endpoints"
root-cause: "API request validation was rejecting requests due to incorrect parameter format in the CJ Line integration."
solution: "Fixed API parameter validation to accept CJ Line request format. See CS-70."
jira: WEB-247
resolved: 2022-09-02
fix-version: ""
---

# WEB-247: CJ Line QA: 400 Error from Backend API

## 問題

CJ Line QA environment returns HTTP 400 error when calling specific backend endpoints

## 根因

API request validation was rejecting requests due to incorrect parameter format in the CJ Line integration.

## 解法

Fixed API parameter validation to accept CJ Line request format. See CS-70.

## 相關資訊

- Jira: [WEB-247](https://ctil.atlassian.net/browse/WEB-247)
- Fix Version: 未記錄
- 解決日期: 2022-09-02

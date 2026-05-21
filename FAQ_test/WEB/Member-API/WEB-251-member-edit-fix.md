---
tags: [faq, WEB, bug]
component: "Member API"
symptom: "Member Edit function in CS2000 web fails to update certain member fields correctly"
root-cause: "The member edit API was not correctly handling partial field updates, causing some fields to remain unchanged after save."
solution: "Fixed member edit API to properly handle all field updates including partial updates."
jira: WEB-251
resolved: 2022-10-11
fix-version: ""
---

# WEB-251: Member Edit Function Fix — Field Update Failure

## 問題

Member Edit function in CS2000 web fails to update certain member fields correctly

## 根因

The member edit API was not correctly handling partial field updates, causing some fields to remain unchanged after save.

## 解法

Fixed member edit API to properly handle all field updates including partial updates.

## 相關資訊

- Jira: [WEB-251](https://ctil.atlassian.net/browse/WEB-251)
- Fix Version: 未記錄
- 解決日期: 2022-10-11

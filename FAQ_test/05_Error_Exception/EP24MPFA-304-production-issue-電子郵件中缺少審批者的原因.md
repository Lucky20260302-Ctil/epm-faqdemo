---
project: EP24MPFA
issue_key: EP24MPFA-304
issue_type: ''
status: ''
tags:
- 05-error-exception
- 05_error_exception
- ep24mpfa
- epm
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EP24MPFA-304
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
EP24MPFA-304: [Production Issue] 電子郵件中缺少審批者的原因

| 問題

為什麼審批者批准後，電子郵件內容中沒有顯示審批原因（Reason）？

| 根因

Email Template 未包含 Reason 欄位。之前的 Email Template 並不包含 Reason 欄位顯示（Lucky_Huang 於 2025-01-16 指出），導致批准郵件中無法顯示審批者所填寫的原因，而拒絕郵件則可正常顯示原因。

| 解法

修改 Email Template，將 Reason 欄位加入批准（Approve）郵件模板中，確保審批者填寫的原因能正確顯示在郵件內容中，與拒絕（Reject）郵件格式保持一致。

| 相關資訊

- Jira: [EP24MPFA-304](https://ctil.atlassian.net/browse/EP24MPFA-304)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EP24MPFA

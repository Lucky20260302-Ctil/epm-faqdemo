---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3385
issue_type: ''
status: ''
tags:
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3385
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---

EPMTDCPROT-3385: EPRO-929 [Production] Supplier with same name as FMS Only Supplier can be selected in Full Registration Invitation

## 症狀

在進行 Supplier Full Registration Invitation 時，為何可以選擇與系統中已存在的 FMS Only Supplier 同名之供應商？

## 根因

根據 Comment (Gavin Zhou)：進行 Full Registration 時，系統原先未對公司名稱進行重複檢查，導致使用者可以對與系統中已存在供應商同名的公司發出 Full Registration Invitation。

## 解法

在 Full Registration Invitation 流程中加入公司名稱重複驗證：若輸入的公司名稱與系統中已存在的供應商名稱相同，則應阻擋並提示使用者，避免建立重複的供應商記錄。

## 相關資訊

- Jira: [EPMTDCPROT-3385](https://ctil.atlassian.net/browse/EPMTDCPROT-3385)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT

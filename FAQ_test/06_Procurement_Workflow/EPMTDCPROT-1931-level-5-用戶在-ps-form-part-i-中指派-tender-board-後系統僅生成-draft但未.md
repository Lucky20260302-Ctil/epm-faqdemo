---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1931
issue_type: ''
status: ''
tags:
title: "EPMTDCPROT-1931-level-5-用戶在-ps-form-part-i-中指派-tender-board-後系統僅生成-draft但未"
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1931
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---

EPMTDCPROT-1931: 

## 症狀

Level 5 用戶在 PS Form Part I 中指派 Tender Board 後，系統僅生成 Draft，但未向 Tender Board 成員發送指派通知郵件。

## 根因

系統缺少該場景（Level 5 用戶指派 Tender Board）對應的郵件通知模板。Mike Chen 確認：「已經確定是沒有模板導致的」。

## 解法

補建遺漏的郵件通知模板，使 Level 5 用戶指派 Tender Board 時能正確觸發通知郵件發送。Shaun_Huang 確認 sit test pass。

## 相關資訊

- Jira: [EPMTDCPROT-1931](https://ctil.atlassian.net/browse/EPMTDCPROT-1931)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT | 附件: [58134](https://ctil.atlassian.net/rest/api/3/attachment/content/58134) | [58133](https://ctil.atlassian.net/rest/api/3/attachment/content/58133) | [62606](https://ctil.atlassian.net/rest/api/3/attachment/content/62606) |

---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1796
issue_type: ''
status: ''
title: "EPMTDCPROT-1796-供應商邀請郵件invitation-email的模板無法檢索數據導致郵件內容顯示為空或無法正確呈現"
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1796
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-1796: 

## 症狀

供應商邀請郵件（Invitation Email）的模板無法檢索數據，導致郵件內容顯示為空或無法正確呈現。

## 根因

郵件模板未配置正確的數據映射，模板內容為空數據（Mike Chen 確認：「模板就是空数据」），導致系統在生成郵件時無法填入對應的動態欄位資料。

## 解法

修正郵件模板的數據綁定配置，確保模板能正確檢索並填入供應商相關數據。修正後由 Joseph_Hu 確認 Passed。

## 相關資訊

- Jira: [EPMTDCPROT-1796](https://ctil.atlassian.net/browse/EPMTDCPROT-1796)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT | 附件: [57505](https://ctil.atlassian.net/rest/api/3/attachment/content/57505) | [58780](https://ctil.atlassian.net/rest/api/3/attachment/content/58780) |

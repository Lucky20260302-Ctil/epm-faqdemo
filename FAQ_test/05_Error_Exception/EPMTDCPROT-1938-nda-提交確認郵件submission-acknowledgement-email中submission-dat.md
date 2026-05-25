---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1938
issue_type: ''
status: ''
title: "EPMTDCPROT-1938-nda-提交確認郵件submission-acknowledgement-email中submission-dat"
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1938
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-1938: 

## 症狀

NDA 提交確認郵件（Submission Acknowledgement Email）中，Submission Date Time 欄位無法正確檢索，且 Issue Date Time 顯示的時區不正確（與本地時間相差 8 小時）。

## 根因

系統在生成郵件時未正確處理時區轉換。Mike Chen 指出「时区问题目前暂无系统的解决方案」，但 submission date time 的資料檢索問題已修正。時區偏差（UTC vs 本地時間差 8 小時）為系統性問題，Gavin Zhou 也確認「时区不对，差8个小时，但是时分秒是对的」。

## 解法

修正了 submission date time 的資料檢索邏輯使其可正確顯示。時區問題（Issue Date Time 差 8 小時）暫無系統級解決方案，需後續規劃統一的時區處理機制。

## 相關資訊

- Jira: [EPMTDCPROT-1938](https://ctil.atlassian.net/browse/EPMTDCPROT-1938)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT | 附件: [58150](https://ctil.atlassian.net/rest/api/3/attachment/content/58150) | [58149](https://ctil.atlassian.net/rest/api/3/attachment/content/58149) |

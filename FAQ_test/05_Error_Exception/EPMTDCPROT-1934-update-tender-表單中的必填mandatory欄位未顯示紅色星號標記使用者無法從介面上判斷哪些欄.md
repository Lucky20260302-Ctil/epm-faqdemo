---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1934
issue_type: ''
status: ''
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1934
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-1934: 

## 症狀

Update Tender 表單中的必填（mandatory）欄位未顯示紅色星號（*）標記，使用者無法從介面上判斷哪些欄位為必填。

## 根因

前端表單渲染邏輯未正確為 mandatory 欄位添加紅色星號視覺標記。Gavin Zhou 測試確認「没有加红色星星」，Michael Ren 完成修正後標記為 done。

## 解法

修正前端代碼，為所有 mandatory 欄位添加紅色星號（*）標記，使使用者能清楚識別必填欄位。Gavin Zhou 確認 uat pass。

## 相關資訊

- Jira: [EPMTDCPROT-1934](https://ctil.atlassian.net/browse/EPMTDCPROT-1934)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT | 附件: [58140](https://ctil.atlassian.net/rest/api/3/attachment/content/58140) | [58139](https://ctil.atlassian.net/rest/api/3/attachment/content/58139) | [58277](https://ctil.atlassian.net/rest/api/3/attachment/content/58277) |

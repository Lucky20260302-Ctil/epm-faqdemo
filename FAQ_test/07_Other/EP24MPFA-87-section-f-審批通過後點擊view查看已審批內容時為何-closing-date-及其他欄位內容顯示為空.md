---
project: EP24MPFA
issue_key: EP24MPFA-87
issue_type: ''
status: ''
tags:
- 07-other
- 07_other
- ep24mpfa
- epm
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EP24MPFA-87
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Other
category_label: 其他
quality: complete
---

EP24MPFA-87: 

## 症狀

Section F 審批通過後，點擊「View」查看已審批內容時，為何 Closing date 及其他欄位內容顯示為空白？

## 根因

Section F 的 View 模式（審批後查看）未能正確載入已審批的欄位資料。Joseph_Hu 於 2024-09-02 複測確認：Closing date 仍然為空，表明審批流程完成後，Section F 的內容未正確持久化，或 View 頁面未正確渲染該欄位的已儲存資料。

## 解法

修正 Section F 審批完成後的資料持久化邏輯與 View 模式渲染邏輯，確保 Closing date 及所有已填寫欄位在審批通過後，點擊 View 時能完整且正確地顯示。

## 相關資訊

- Jira: [EP24MPFA-87](https://ctil.atlassian.net/browse/EP24MPFA-87)
- Fix Version: 未標註
- 分類: 其他
- 專案: EP24MPFA

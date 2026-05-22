---
project: EP24MPFA
issue_key: EP24MPFA-251
tags: [faq, epm, ep24mpfa, 07-other]
jira_url: "https://ctil.atlassian.net/browse/EP24MPFA-251"
category: 07_Other
category_name: "其他"
---

EP24MPFA-251: 

| 問題

PR 搜尋列表中，「Title」欄位的排序功能為何無法正常運作並出現 Error？

| 根因

搜尋列表的「Sort by Title」功能存在後端錯誤，導致排序請求失敗並顯示 Error。Jocelynml_Chan 測試確認其他新增的搜尋欄位（Subject、Budget、Division/Department、Procurement Officers）運作正常，但 Title 排序仍報錯，說明問題侷限在排序邏輯本身。

| 解法

修正「Sort by Title」的後端排序邏輯，確保能正確按 Title 欄位排序而不觸發 Error。搜尋條件中的 Subject、Budget、Division/Department、Procurement Officers 等新增欄位維持現有正確實作。

| 相關資訊

- Jira: [EP24MPFA-251](https://ctil.atlassian.net/browse/EP24MPFA-251)
- Fix Version: 未標註
- 分類: 其他
- 專案: EP24MPFA

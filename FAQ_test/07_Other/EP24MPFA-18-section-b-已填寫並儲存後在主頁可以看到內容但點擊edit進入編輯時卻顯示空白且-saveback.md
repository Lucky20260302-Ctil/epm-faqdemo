---
project: EP24MPFA
issue_key: EP24MPFA-18
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
jira_url: https://ctil.atlassian.net/browse/EP24MPFA-18
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Other
category_label: 其他
quality: complete
---

EP24MPFA-18: 

## 症狀

Section B 已填寫並儲存後，在主頁可以看到內容，但點擊「Edit」進入編輯時卻顯示空白，且 Save/Back 按鈕無反應。是什麼原因？

## 根因

表單編輯模式的資料載入邏輯存在缺陷：已儲存的 Section B 資料在重新進入編輯模式時未能正確載入，導致頁面空白且按鈕無回應。此問題具跨 Section 複現性：Section A 選擇「not applicable」時 Procurement Method 無法顯示、文件消失，同樣是編輯模式資料載入失敗的症狀。

## 解法

修正 Section A 與 Section B 的編輯模式資料載入邏輯，確保點擊 Edit 後能正確載入已儲存的表單資料（含文字欄位內容），並恢復 Save/Back 按鈕的正常功能。

## 相關資訊

- Jira: [EP24MPFA-18](https://ctil.atlassian.net/browse/EP24MPFA-18)
- Fix Version: 未標註
- 分類: 其他
- 專案: EP24MPFA

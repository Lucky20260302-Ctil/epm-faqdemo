---
project: EP24MPFA
issue_key: EP24MPFA-243
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
jira_url: https://ctil.atlassian.net/browse/EP24MPFA-243
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Other
category_label: 其他
quality: complete
---
EP24MPFA-243: 

| 問題

Approval History 中，為何 Remarks/Reason 顯示不完整？Approved 案例只顯示 text field 輸入的文字而未顯示 checkbox 選項；Rejected 案例的 checkbox 原因只顯示數字（如「1」）而非完整文字。

| 根因

Approval History 的顯示邏輯存在兩個缺陷：(1) Approved 案例中，審批人在 checkbox 勾選的項目未被納入顯示，僅顯示了「Other」文字框中輸入的內容；(2) Rejected 案例中，拒絕原因的 checkbox 選項僅輸出了選項的索引數字而非對應的文字描述。

| 解法

修正 Approval History 的顯示邏輯：(1) Approved 案例應同時顯示 checkbox 選項文字和 Other 文字框內容；(2) Rejected 案例的拒絕原因應顯示完整文字描述而非數字索引；(3) 所有顯示內容應以換行分隔呈現，格式為：<拒絕原因1>, <拒絕原因2>, <remarks文字>。

| 相關資訊

- Jira: [EP24MPFA-243](https://ctil.atlassian.net/browse/EP24MPFA-243)
- Fix Version: 未標註
- 分類: 其他
- 專案: EP24MPFA

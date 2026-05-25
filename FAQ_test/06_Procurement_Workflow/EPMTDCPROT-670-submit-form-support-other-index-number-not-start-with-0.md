---
project: EPMTDCPROT
issue_key: EPMTDCPROT-670
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
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-670
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---

EPMTDCPROT-670: Submit Form Support other index number not start with 0

## 症狀

前端提交 e-form 時，傳送至後端的物件 array index 必須從 0 開始（如 psTenders[0]/id），不支援從其他 index 起始（如 psTenders[1]/id）。當前端因業務邏輯產生非 0 起始的 array index 時，Workflow service 與 validation service 無法正確轉換與處理該筆資料。

## 根因

Workflow service 與 validation service 中的 Form Object converter 在解析前端提交的 form data 時，僅實作了 array index 從 0 開始的轉換邏輯。Aaron_So 在 Comment 中明確指出需修改的程式碼位置：當前端更新物件列表時，converter 假設 index 必須從零起始，未處理任意起始 index 的情況。

## 解法

修改 Workflow service 與 validation service 中的 Form Object converter，擴展其支援任意起始 index 的 array 更新（不限於從 0 開始）。William Qiu 提供了包含非 0 起始 index 的完整 test case（psTenders[1]/id 等），驗證修改後 converter 可正確處理。

## 相關資訊

- Jira: [EPMTDCPROT-670](https://ctil.atlassian.net/browse/EPMTDCPROT-670)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-670/image-20241008-020308.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-670/image-20241008-020353.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-670/image-20241008-070959.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


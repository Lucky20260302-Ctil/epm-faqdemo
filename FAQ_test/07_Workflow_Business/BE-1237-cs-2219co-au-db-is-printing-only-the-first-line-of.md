---
project: BE
issue_key: BE-1237
issue_type: Bug PRD
status: Open
tags:
- 07_workflow_business
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1237
created: '2026-03-20'
resolved: ''
fix_version: ''
components:
- Table
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

BE-1237: CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines

## 症狀

CO-AU 環境中，POS 輸入 4 行備註（每行 40 字元）完成交易後，BE DB jouinv 資料表的 remarks 欄位僅儲存/顯示第一行，其餘行遺失。

## 根因

結構不相容：FE DBSSE 有 8 個 remarks 欄位（每個上限 40 字元），但 BE jouinv 資料表僅有 1 個 jouinv_remarks 欄位且上限為 40 字元，導致多行備註被截斷。

## 解法

擴充 BE jouinv 資料表的 remarks 欄位結構，使其能容納 FE 傳入的多行備註內容（增加欄位數量或擴大欄位長度）。

## 相關資訊

- Jira: [BE-1237](https://ctil.atlassian.net/browse/BE-1237)
- 組件: Table
- 負責人: Jerry Wong
- 附件: [image-20260320-034153.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81318) | [image-20260320-034324.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81321) | [image-20260320-034402.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81319) | [image-20260320-034859.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81320) | [image-20260320-040941.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81323)


## 相關截圖

![[../attachments/BE-1237/image-20260320-034153.png]]

![[../attachments/BE-1237/image-20260320-034324.png]]

![[../attachments/BE-1237/image-20260320-034402.png]]

![[../attachments/BE-1237/image-20260320-034859.png]]

![[../attachments/BE-1237/image-20260320-040941.png]]


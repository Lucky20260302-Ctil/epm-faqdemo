---
project: EPMTDCPROT
issue_key: EPMTDCPROT-678
issue_type: ''
status: ''
title: "EPMTDCPROT-678-psprocurement-service中的-procurement-method-欄位為何不是-array-類型"
tags:
- 07-other
- 07_other
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-678
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Other
category_label: 其他
quality: complete
---

EPMTDCPROT-678: 

## 症狀

PS（Procurement Service）中的 Procurement Method 欄位為何不是 Array 類型，導致使用者只能選擇一個項目？

## 根因

Procurement Method 欄位的資料型別定義為單一值（Single Value）而非陣列（Array），導致前端只能綁定單選元件，使用者無法多選採購方式。

## 解法

將 Procurement Method 欄位的資料型別從單一值修改為 Enum（多選列舉型別），使前端可使用多選元件，允許使用者同時選擇多個採購方式。

## 相關資訊

- Jira: [EPMTDCPROT-678](https://ctil.atlassian.net/browse/EPMTDCPROT-678)
- Fix Version: 未標註
- 分類: 其他
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-678/image-20240927-023229.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-678/image-20240927-023245.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-678/image-20240927-023951.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-678/image-20240930-032816.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


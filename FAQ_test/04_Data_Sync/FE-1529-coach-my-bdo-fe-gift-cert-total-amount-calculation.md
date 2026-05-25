---
project: FE
issue_key: FE-1529
issue_type: Bug QA
status: Closed
title: "FE-1529-coach-my-bdo-fe-gift-cert-total-amount-calculation"
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1529
created: '2024-10-18'
resolved: '2024-10-19'
fix_version: V750.04R07A
components:
- Front End
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

FE-1529: Coach MY BDO FE - gift cert total amount calculation error

## 症狀

在 Coach MY BDO 的 POS（v750.04R07）建立禮券（Gift Certificate）發行備忘錄時，即使備忘錄包含多行明細，產生的 PCD 檔案中總金額計算錯誤（例如顯示為 1400.00 而非正確總額），導致 BE 入帳及電子發票介面發生問題。

## 根因

POS 在寫入 PCD 記錄類型 '31'（禮券備忘錄）時，總金額欄位的計算邏輯存在缺陷，未正確加總所有明細行的金額，導致 PCD 檔案中的總金額與 POS 畫面顯示不一致。

## 解法

修正於 v750.04R07A（Build 241019），修復 PCD '31' 禮券備忘錄的總金額計算及 TMU 列印輸出問題。更新後 PCD 檔案中的總金額與 POS 畫面顯示一致，BE 入帳正常。

## 相關資訊

- Jira: [FE-1529](https://ctil.atlassian.net/browse/FE-1529)
- Fix Version: V750.04R07A
- 解決日期: 2024-10-19
- 組件: Front End
- 負責人: Andy Ko
- 附件: [image-20241018-033559.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47062) | [image-20241018-033658.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47061) | [image-20241019-014836.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47134) | [image-20241019-015023.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47135) | [image-20241019-015201.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47136)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1529/image-2024-10-19-22-43-48-078.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1529/image-20241018-033559.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1529/image-20241018-033658.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1529/image-20241019-014836.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1529/image-20241019-015023.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 7 張截圖，[查看全部](/FAQ_test/attachments/FE-1529/)

---
project: FE
issue_key: FE-1393
issue_type: Bug PRD
status: Closed
tags:
title: "FE-1393-cs-1034-issue_jp_rin01339795-a-barcode-was-splited"
- 06_printing_hardware
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1393
created: '2024-05-17'
resolved: '2024-05-24'
fix_version: v750.04R04A
components:
- Front End
has_images: false
category: 06_Printing_Hardware
category_label: 列印與硬體
quality: complete
---

FE-1393: Issue_JP_RIN01339795 A barcode was splited up when printed out.

## 症狀

POS 版本升級（V72 至 V75）後，條碼列印出現分裂/斷開的異常狀況。原因為條碼列印的 layout INI 設定檔在版本升級過程中被清除，導致新版 POS 無法取得正確的條碼列印參數。

## 根因

版本升級流程中的 adminUpdate.bat 未將舊版 CS2000POS\Layout 目錄下的條碼列印 INI 設定檔備份並遷移至新版 CSPLUS\Layout 目錄，導致列印參數遺失。

## 解法

修改 V72 與 V75 的 adminUpdate.bat：V72 先將 Layout 檔案備份至 Retdata6\layout 目錄；V75 再從 Retdata6\layout 複製至 CSPLUS\layout。降版時亦從 Retdata6\layout 還原。修復版本：v750.04R04A。

## 相關資訊

- Jira: [FE-1393](https://ctil.atlassian.net/browse/FE-1393)
- Fix Version: v750.04R04A
- 解決日期: 2024-05-24
- 組件: Front End
- 負責人: Joy Li
- 附件: [FE-1393- Backup layout.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/41686) | [image-20240521-055538.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41567)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1393/image-20240521-055538.png" style="max-width:100%;border-radius:6px;margin:4px 0">


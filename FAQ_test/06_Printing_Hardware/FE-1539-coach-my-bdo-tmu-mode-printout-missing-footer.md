---
project: FE
issue_key: FE-1539
issue_type: Bug QA
status: Closed
title: "FE-1539: Coach MY BDO - TMU mode printout missing footer"
tags:
- 06_printing_hardware
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1539
created: '2024-10-24'
resolved: '2024-10-28'
fix_version: ''
components:
- Front End
has_images: false
category: 06_Printing_Hardware
category_label: 列印與硬體
quality: complete
---

FE-1539: Coach MY BDO - TMU mode printout missing footer

## 症狀

Coach MY BDO 店鋪使用 TMU 模式列印時，POS 與 MPOS 的所有單據（銷售單、電子收據）底部頁尾（Footer）遺失，Zebra 列印亦有相同問題。

## 根因

TMU 模式的頁尾檔案設定在 tblconfig 中未正確配置。TMU 列印需要分別設定四種交易類型的頁尾檔案：FOOTERFILENAMENORMAL（銷售/存款結算）、FOOTERFILENAMEEXCHANGE（銷售換貨）、FOOTERFILENAMERETURN（銷售退貨/作廢/作廢存款結算、作廢銷售退貨/作廢銷售換貨）。

## 解法

檢查並設定 tblconfig 中對應的頁尾檔案名稱參數（FOOTERFILENAMENORMAL、FOOTERFILENAMEEXCHANGE、FOOTERFILENAMERETURN），確保 TMU 模式可正確讀取並列印頁尾內容。

## 相關資訊

- Jira: [FE-1539](https://ctil.atlassian.net/browse/FE-1539)
- 解決日期: 2024-10-28
- 組件: Front End
- 負責人: Sang
- 附件: [CRXFOOTSALES_EN.txt](https://ctil.atlassian.net/rest/api/3/attachment/content/47346) | [Dbtrans.sdf](https://ctil.atlassian.net/rest/api/3/attachment/content/47347) | [image-20241024-013530.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47344) | [image-20241024-014735.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47348) | [image-20241024-021309.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47352)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1539/image-20241024-013530.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1539/image-20241024-014735.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1539/image-20241024-021309.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1539/screenshot-link_att.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1539/signal-2024-10-24-093659.jpeg" style="max-width:100%;border-radius:6px;margin:4px 0">


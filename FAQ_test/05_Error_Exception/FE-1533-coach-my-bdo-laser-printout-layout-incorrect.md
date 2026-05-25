---
project: FE
issue_key: FE-1533
issue_type: Bug QA
status: Closed
tags:
title: "FE-1533-coach-my-bdo-laser-printout-layout-incorrect"
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1533
created: '2024-10-21'
resolved: '2024-10-29'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1533: Coach MY BDO - laser printout layout incorrect

## 症狀

Coach MY BDO 雷射印表機列印 memo 時以直式（portrait）輸出，導致內容過小且 QR code 無法掃描，先前正常為橫式（landscape）。

## 根因

印表機驅動程式問題（printer driver issue），非 POS 程式本身瑕疵。

## 解法

更換為正確的印表機驅動程式即可恢復正常橫式列印。

## 相關資訊

- Jira: [FE-1533](https://ctil.atlassian.net/browse/FE-1533)
- 解決日期: 2024-10-29
- 組件: Front End
- 負責人: Sang
- 附件: [20241021_104323.jpg](https://ctil.atlassian.net/rest/api/3/attachment/content/47158) | [20241021_104327.jpg](https://ctil.atlassian.net/rest/api/3/attachment/content/47159)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1533/20241021_104323.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1533/20241021_104327.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


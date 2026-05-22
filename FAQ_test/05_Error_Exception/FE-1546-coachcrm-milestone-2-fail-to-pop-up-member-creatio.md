---
project: FE
issue_key: FE-1546
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1546
created: '2024-11-01'
resolved: '2024-11-08'
fix_version: FE-V750.04R09
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1546: Fail to pop up member creation screen after scan a new wechat QR code

## 症狀

掃描新的微信 QR Code 後，無法彈出會員建立畫面。

## 根因

系統設定 tblconfig.MEMBERNOTFOUNDAUTOCREATE 未設為 'Y'，導致找不到會員時不會自動觸發建立畫面。

## 解法

將 tblconfig.MEMBERNOTFOUNDAUTOCREATE 設為 'Y' 以啟用自動建立會員畫面功能。

## 相關資訊

- Jira: [FE-1546](https://ctil.atlassian.net/browse/FE-1546)
- Fix Version: FE-V750.04R09
- 解決日期: 2024-11-08
- 組件: Front End
- 負責人: Sherman tse
- 附件: [image-20241101-084227.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47634) | [image-20241101-095340.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47657)

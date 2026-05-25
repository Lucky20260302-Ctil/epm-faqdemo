---
project: MP
issue_key: MP-702
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-702
created: '2024-05-28'
resolved: '2024-06-07'
fix_version: 3.28.2_IPA
components:
- MPOS
- MPOS API
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

MP-702: Japanese user login in MPOS which caused posting error

## 症狀

使用者在 MPOS 登入時輸入日文字元，導致 posting error。

## 根因

日文字元登入 MPOS 會產生失敗的登入記錄，這些記錄在 posting 時因編碼或格式問題導致錯誤。

## 解法

短期：通知使用者不要在 MPOS 登入時輸入日文。長期：增強程式以在 MPOS 登入時阻擋日文字元輸入。

## 相關資訊

- Jira: [MP-702](https://ctil.atlassian.net/browse/MP-702)
- Fix Version: 3.28.2_IPA
- 解決日期: 2024-06-07
- 組件: MPOS, MPOS API
- 負責人: Joy Li
- 附件: [image-20240528-084347.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41810) | [TestCase_CS-873.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/42036)


## 相關截圖

![[../attachments/MP-702/image-20240528-084347.jpg]]


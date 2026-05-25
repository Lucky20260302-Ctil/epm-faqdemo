---
project: FE
issue_key: FE-938
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-938
created: '2021-03-19'
resolved: '2022-08-18'
fix_version: v720.01R03A
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-938: Price Modification cannot is applied into item with negative quantity (sales return)

## 症狀

對退貨品項（負數量）使用 Shift+F1 修改價格時，系統顯示錯誤訊息，無法完成價格修改。發生於無備忘錄號碼的退貨情境，系統找不到歷史有效價格，改用當前價格後仍被驗證阻擋。

## 根因

退貨品項無備忘錄號碼時，系統無法從歷史記錄中找到有效售價，只能使用當前價格。但 Shift+F1 的 Price Modification 功能中的驗證邏輯（Validate Corrected list Price lower than max discount price）阻擋了價格修改操作。

## 解法

啟用 Price Correction Mode（價格修正模式），繞過「修正後價格不得低於最大折扣價」的驗證檢查。修正版本：v720.01R03A (KTS 210322)。

## 相關資訊

- Jira: [FE-938](https://ctil.atlassian.net/browse/FE-938)
- Fix Version: v720.01R03A
- 解決日期: 2022-08-18
- 組件: Front End
- 負責人: Sang
- 附件: [image-2021-03-19-10-35-55-212.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37318) | [image-2021-03-19-10-37-02-499.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37321) | [image-2021-03-19-16-51-41-621.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37327)


## 相關截圖

![[../attachments/FE-938/image-2021-03-19-10-35-55-212.png]]

![[../attachments/FE-938/image-2021-03-19-10-37-02-499.png]]

![[../attachments/FE-938/image-2021-03-19-16-51-41-621.png]]


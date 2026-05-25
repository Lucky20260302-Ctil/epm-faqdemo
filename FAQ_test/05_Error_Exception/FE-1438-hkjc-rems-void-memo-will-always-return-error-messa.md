---
project: FE
issue_key: FE-1438
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1438
created: '2024-06-27'
resolved: '2024-07-09'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1438: REMS void memo will always return error message even though API returned sucess

## 症狀

作廢含 PP pay code（burn points / 點數折抵）的交易時，即使 API 回傳成功，POS 仍顯示失敗訊息，阻擋作廢流程完成。

## 根因

作廢邏輯中，當 void API 回傳 false 時才判定失敗，但 burn points 情境下 API 回傳值判斷有誤，導致成功也被誤報為失敗。

## 解法

修正 void memo 邏輯（v750.01R02G），確保 burn points 交易的 void API 成功時不再誤報錯誤。

## 相關資訊

- Jira: [FE-1438](https://ctil.atlassian.net/browse/FE-1438)
- 解決日期: 2024-07-09
- 組件: Front End
- 負責人: Sang
- 附件: [Untitled.jpg](https://ctil.atlassian.net/rest/api/3/attachment/content/42601)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1438/Untitled.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


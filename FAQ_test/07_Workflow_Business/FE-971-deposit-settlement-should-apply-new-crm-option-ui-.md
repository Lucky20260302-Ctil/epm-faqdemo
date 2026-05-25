---
project: FE
issue_key: FE-971
issue_type: Bug QA
status: Closed
title: "FE-971-deposit-settlement-should-apply-new-crm-option-ui-"
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-971
created: '2021-05-07'
resolved: '2021-05-13'
fix_version: v750.01R01A, v720.01R03B,, v720.01R04
components:
- Frontend
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

FE-971: Deposit Settlement should apply new CRM option UI (same as issuing Sales Memo)

## 症狀

開立訂金結算備忘錄（Deposit Settlement）時，Send e-Receipt 對話框中未顯示會員的 CRM Email 地址，導致無法發送電子收據給會員。但以相同會員開立一般銷售備忘錄（Sales Memo）時，Send e-Receipt 對話框則可正常顯示 CRM Email，兩者行為不一致。

## 根因

訂金結算流程中的 Send e-Receipt UI 未正確套用與銷售備忘錄相同的 CRM Email 顯示邏輯，導致會員 Email 欄位在訂金結算時未被填入 Send e-Receipt 對話框。

## 解法

已於以下版本中修正此問題：v720.01R03B、v720.01R04、v750.01R01A。修正後訂金結算的 Send e-Receipt 對話框可正確顯示會員 CRM Email，與銷售備忘錄行為一致。

## 相關資訊

- Jira: [FE-971](https://ctil.atlassian.net/browse/FE-971)
- Fix Version: v750.01R01A, v720.01R03B,, v720.01R04
- 解決日期: 2021-05-13
- 組件: Frontend
- 負責人: howard
- 附件: [image-2021-05-07-15-57-21-304.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37349) | [image-2021-05-07-15-57-52-474.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37353) | [image-2021-05-07-15-58-22-053.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37357) | [image-2021-05-13-10-01-35-722.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37362)


## 相關截圖

<img src="/FAQ_test/attachments/FE-971/image-2021-05-07-15-57-21-304.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-971/image-2021-05-07-15-57-52-474.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-971/image-2021-05-07-15-58-22-053.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-971/image-2021-05-13-10-01-35-722.png" style="max-width:100%;border-radius:6px;margin:4px 0">


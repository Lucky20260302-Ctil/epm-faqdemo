---
project: FE
issue_key: FE-972
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-972
created: '2021-05-11'
resolved: '2024-05-04'
fix_version: ''
components:
- Front End
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

FE-972: Staff purchase quota calculation logic with MM coupon

## 症狀

員工擁有可用配額2935元，享有50%會員折扣及額外40%的MM折價券。當未折扣金額大於配額時，POS會阻止交易，但實際上折扣後金額並未超過可用配額，導致員工無法完成合法交易。

## 根因

POS在檢查員工購買限額時，未先扣除MM折價券的折扣金額，導致以原始未折扣金額進行配額比對，而非以實際折扣後金額進行比對，造成誤判。

## 解法

更新至KTS 220616 v750.02版本（Jira FE-972），該版本修正了員工購買限額的計算邏輯：先排除折價券數量進行限額計算，並在套用MM折價券後再檢查限額。

## 相關資訊

- Jira: [FE-972](https://ctil.atlassian.net/browse/FE-972)
- 解決日期: 2024-05-04
- 組件: Front End
- 負責人: Sang
- 附件: [image-2022-06-16-13-55-18-180.png](https://ctil.atlassian.net/rest/api/3/attachment/content/38301)

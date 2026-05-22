---
project: FE
issue_key: FE-812
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-812
created: '2020-10-22'
resolved: '2020-11-23'
fix_version: v710.02R14U
components:
- Sales
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

FE-812: void sales transaction can use cash coupon, but Void sales cash coupon show repeat

## 症狀

作廢銷售交易（Void Sales）時可使用 Cash Coupon（現金券），但作廢後同一張 Cash Coupon 記錄出現重複，導致 Coupon 資料不一致。

## 根因

系統在 Void Memo with Coupon Redeem 流程中寫入 Coupon 記錄的邏輯存在缺陷，導致同一筆 Coupon 被重複寫入資料庫。

## 解法

升級至版本 v710.02R14U（IMX），該版本已修正 Void Memo with Coupon Redeem 重複寫入 Coupon 記錄的問題。

## 相關資訊

- Jira: [FE-812](https://ctil.atlassian.net/browse/FE-812)
- Fix Version: v710.02R14U
- 解決日期: 2020-11-23
- 組件: Sales
- 負責人: Derek_Leung
- 附件: [image-2020-10-22-12-13-43-466.png](https://ctil.atlassian.net/rest/api/3/attachment/content/38756)

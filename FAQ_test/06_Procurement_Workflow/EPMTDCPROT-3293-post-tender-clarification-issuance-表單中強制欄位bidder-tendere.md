---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3293
issue_type: ''
status: ''
title: "EPMTDCPROT-3293-post-tender-clarification-issuance-表單中強制欄位bidder-tendere"
tags:
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3293
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---

EPMTDCPROT-3293: 

## 症狀

Post-Tender Clarification Issuance 表單中，強制欄位「Bidder / Tenderer」未顯示在表單上，但表單仍可成功提交並通過審批，導致供應商無法收到 Post-Tender Clarification 的待辦通知郵件。

## 根因

資料庫中的 EformConfig 設定可能遺漏了 Bidder/Tenderer 欄位的配置。William Qiu 指出：「目前是通過db的EformConfig進行控制的…出現這種情況需要查看production的db是否這個config漏了東西而導致的」。

## 解法

檢查並修正 Production 環境中 EformConfig 的設定，確保 Bidder/Tenderer 欄位在 Post-Tender Clarification Issuance 表單中正確顯示且為必填，避免因資料庫配置缺失導致欄位遺漏。

## 相關資訊

- Jira: [EPMTDCPROT-3293](https://ctil.atlassian.net/browse/EPMTDCPROT-3293)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT | 附件: [72737](https://ctil.atlassian.net/rest/api/3/attachment/content/72737) | [72738](https://ctil.atlassian.net/rest/api/3/attachment/content/72738) |

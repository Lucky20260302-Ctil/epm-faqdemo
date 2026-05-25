---
project: BE
issue_key: BE-1232
issue_type: Bug QA
status: Closed
title: "BE-1232-cs-2099-anz-gcsap-cannot-process-void-gc-issue-rec"
tags:
- 07_workflow_business
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1232
created: '2026-03-02'
resolved: '2026-03-05'
fix_version: BE-V70R3.147
components:
- Data Interface
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

BE-1232: SAP cannot process void GC issue records

## 症狀

ANZ 地區 Gift Card 交易在 void 後，產生的 Gift Cert 記錄匯出至 SAP 時無法處理，SAP 端報錯。問題發生在 Sales Memo 轉換為 Gift Cert 的過程中，Gift Cert 記錄包含了不應存在的 Discount 記錄（Indicator = D），導致 SAP 介面處理異常。

## 根因

POS 後端在將 GiftCard Sales Memo 轉換為 Gift Cert 記錄（CAR Interface）時，現有邏輯錯誤地將 Discount 記錄（Indicator = D）一併帶入 Gift Cert。依照規格，Gift Cert Memo 僅應包含 Gift Cert Header（Indicator = I）及 Payment（Indicator = P），不應包含 Discount 記錄。Discount 記錄的存在導致 SAP 端無法正確解析並處理 void GC 記錄。

## 解法

修改 CAR Interface 轉換邏輯，在 Sales Memo → Gift Cert 的轉換過程中，移除 GiftCard 交易的 Discount 記錄（Indicator = D），確保 Gift Cert 輸出僅包含 Header 與 Payment 記錄。此修正已於 BE-V70R3.147 版本中發布（2026-03-05），並經 QA 測試驗證通過。

## 相關資訊

- Jira: [BE-1232](https://ctil.atlassian.net/browse/BE-1232)
- Fix Version: BE-V70R3.147
- 解決日期: 2026-03-05
- 組件: Data Interface
- 負責人: Sherman tse
- 附件: [test case of CS-2099- ANZ GC- SAP cannot process void GC issue records.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/80067)

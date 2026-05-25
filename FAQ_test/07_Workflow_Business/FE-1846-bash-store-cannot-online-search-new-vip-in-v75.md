---
project: FE
issue_key: FE-1846
issue_type: Bug PRD
status: Selected for Development (migrated)
title: "FE-1846: BASH Store cannot online search new VIP in v75"
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1846
created: '2026-01-06'
resolved: ''
fix_version: ''
components:
- Frontend
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

FE-1846: BASH Store cannot online search new VIP in v75

## 症狀

BASH 品牌店鋪升級至 V75 後，無法即時線上搜尋新加入的 VIP 會員。原先當 CRM 系統將新會員資料傳送至後端資料庫後，POS 可立即搜尋到該會員，但升級後必須等待 zfile 整合並關閉重新開啟 POS 系統才能找到新會員，影響門市人員作業效率。

## 根因

V75 版本中 VIP 會員資料的即時線上搜尋機制出現回歸問題（Regression），導致 POS 無法即時查詢 CRM 推送至後端資料庫的新會員資料，僅能依賴批次 zfile 整合後的資料更新，需重啟 POS 才能生效。

## 解法

此問題已在 v750.05R04 版本中修復，適用於 BASH、IMX、A+O、SPH 品牌。請將 POS 前端更新至 v750.05R04 或更高版本，更新後新 VIP 會員資料即可透過線上搜尋即時查詢，無需關閉重啟 POS。

## 相關資訊

- Jira: [FE-1846](https://ctil.atlassian.net/browse/FE-1846)
- 組件: Frontend
- 負責人: Sang
- 附件: [image-20260106-032841.png](https://ctil.atlassian.net/rest/api/3/attachment/content/72470)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1846/image-20260106-032841.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


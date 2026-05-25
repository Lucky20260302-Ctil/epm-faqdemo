---
project: WEB
issue_key: WEB-404
issue_type: Bug QA
status: Closed
tags:
title: "WEB-404-cs-1514-tw-crm-cross-border-should-only-happen-for"
- 07_workflow_business
- faq
- web
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/WEB-404
created: '2025-08-07'
resolved: '2025-08-07'
fix_version: BE-V70R3.114
components:
- BEAPICRM
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

WEB-404: TW CRM - Cross border should only happen for CN member, rest regions no need

## 症狀

台灣地區會員在 POS 查詢時，系統會錯誤地觸發跨境（Cross Border）隱私政策檢查，顯示不必要的跨境查詢阻擋訊息。實際上跨境政策檢查僅需針對中國（CN）地區會員執行，台灣及其他地區會員不應受到此限制。

## 根因

BEGWCRM 與 BEAPICRM 服務在 AWS 上未依地區進行拆分部署，導致所有地區的 CRM API 請求都經過相同的跨境政策檢查邏輯，使非 CN 地區會員也被錯誤地觸發跨境檢查。

## 解法

將 BEGWCRM 與 BEAPICRM 服務依地區分別部署於 AWS 上，使各地區的 CRM API 獨立運作。此修正已於 2025-08-06 發布於 BE-V70R3.114 版本（屬設定調整，無程式碼變更）。

## 相關資訊

- Jira: [WEB-404](https://ctil.atlassian.net/browse/WEB-404)
- Fix Version: BE-V70R3.114
- 解決日期: 2025-08-07
- 組件: BEAPICRM
- 負責人: Joy Li
- 附件: [image-20250807-010942.png](https://ctil.atlassian.net/rest/api/3/attachment/content/62853)


## 相關截圖

<img src="/FAQ_test/attachments/WEB-404/image-20250807-010942.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


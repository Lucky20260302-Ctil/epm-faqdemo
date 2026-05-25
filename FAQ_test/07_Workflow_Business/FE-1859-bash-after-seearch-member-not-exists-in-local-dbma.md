---
project: FE
issue_key: FE-1859
issue_type: Bug PRD
status: Open
tags:
title: "FE-1859-bash-after-seearch-member-not-exists-in-local-dbma"
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1859
created: '2026-01-23'
resolved: ''
fix_version: ''
components:
- Front End
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

FE-1859: After seearch member (Not exists in local DBMas) by BEDB connection (CS2000) cannot applied

## 症狀

Ba&sh 品牌 POS 升級至 v750.05R03 後，當透過 BEDB（CS2000）連線搜尋不存在於本地資料庫的會員時，POS 雖可成功擷取會員資訊並顯示 VIP 編號，但該會員無法被正式套用至交易中——無法帶出折扣、訊息及優惠券，會員物件僅有 VIP 編號而缺少其他關鍵屬性。

## 根因

當 config ONLINEMEMBERENQUIRY 設為 'N' 時，系統會優先搜尋本地 DB，若找不到會員則透過 EnableOnlineMember 功能連線至 BE DB 搜尋。然而 v750.05R03 中的 EnableOnlineMember 線上會員搜尋功能存在 Bug（Jira FE-1846），導致從 BE DB 取回的會員物件未完整轉換或驗證，缺少會員類型、折扣等屬性，使 POS 無法正常套用該會員資料。

## 解法

方案一（升級）：升級至 v750.05R04，此版本已修復 EnableOnlineMember 從 BE DB 搜尋會員的功能（KTS 260106 FE-1846）。方案二（Workaround）：將 ONLINEMEMBERENQUIRY 設為 'Y'，直接使用 BE DB 進行會員查詢，繞過有 Bug 的本地搜尋 fallback 路徑，但此舉會增加 BE DB 及網路負載。

## 相關資訊

- Jira: [FE-1859](https://ctil.atlassian.net/browse/FE-1859)
- 組件: Front End
- 負責人: Sang
- 附件: [image-20260123-082332.png](https://ctil.atlassian.net/rest/api/3/attachment/content/74513) | [image-20260123-091210.png](https://ctil.atlassian.net/rest/api/3/attachment/content/74525)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1859/image-20260123-082332.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1859/image-20260123-091210.png" style="max-width:100%;border-radius:6px;margin:4px 0">


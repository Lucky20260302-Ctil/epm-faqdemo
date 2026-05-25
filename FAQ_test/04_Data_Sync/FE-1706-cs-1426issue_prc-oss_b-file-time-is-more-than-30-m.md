---
project: FE
issue_key: FE-1706
issue_type: Bug PRD
status: Closed
title: "FE-1706: Issue_PRC OSS_B file time is more than 30 minutes"
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1706
created: '2025-05-30'
resolved: ''
fix_version: ''
components:
- Front End
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

FE-1706: Issue_PRC OSS_B file time is more than 30 minutes

## 症狀

中國大陸 PRC OSS_B 輪詢及過帳（Posting）每日出現延遲超過 30 分鐘的情況，尤其在晚上 10 點後，CN 店舖集中做 Day End 時更為嚴重。ACP 檔案從進入 posting 隊列到實際處理之間已延遲超過 40 分鐘。

## 根因

根據 2025-09-10 的 RCA 結論：(1) OSS token 過期導致輪詢失敗，token 有效期不足以處理積壓的檔案；(2) 過多的 dummy stx 檔案佔用輪詢資源，拖慢整體處理速度。此問題與 BE-1141 的根因相似，屬同一類 OSS 架構瓶頸問題。

## 解法

程式已於 2025-07-03 發布，包含三項增強措施：(1) OSS token 失效後自動重新獲取（token 刷新設定為 10 分鐘）；(2) 將輪詢程式拆分為上傳與下載兩個獨立部分，分別處理 stx 檔案與 acp 檔案；(3) 在 CN 區域新增一個獨立的輪詢及過帳節點 OSS_C，分散處理負載。部署後延遲問題已解決。

## 相關資訊

- Jira: [FE-1706](https://ctil.atlassian.net/browse/FE-1706)
- 組件: Front End
- 負責人: Joy Li
- 附件: [image-20250530-073503.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58477) | [image-20250530-073837.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58479) | [image-20250530-074005.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58481) | [image-20250530-074100.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58480) | [image-20250530-074206.png](https://ctil.atlassian.net/rest/api/3/attachment/content/58478)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1706/image-20250530-073503.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1706/image-20250530-073837.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1706/image-20250530-074005.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1706/image-20250530-074100.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1706/image-20250530-074206.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


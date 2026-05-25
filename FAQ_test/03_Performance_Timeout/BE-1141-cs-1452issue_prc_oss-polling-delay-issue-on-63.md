---
project: BE
issue_key: BE-1141
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1141
created: '2025-06-30'
resolved: '2025-07-03'
fix_version: BE-V70R3.112
components:
- polling
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: complete
---

BE-1141: Issue_PRC_OSS Polling Delay issue on 6.3

## 症狀

中國大陸 PRC OSS 輪詢（Polling）出現嚴重延遲，OSS 資料夾中累積超過 4 萬個 stx 檔案，且 OSS token 有效期僅 1 小時，若輪詢檔案過多，部分店舖（如 OCF88、OCF9）的檔案在 token 過期前無法完成輪詢。此外，產生 Zlog 的作業會鎖定 POSTAB 資料表，導致輪詢作業完全停擺。

## 根因

(1) OSS token 有效期過短（僅 1 小時），當待輪詢檔案過多時，token 過期導致輪詢失敗並不斷重試，產生大量 stx 暫存檔；(2) Zlog 產生作業對 POSTAB 資料表施加鎖定，阻塞其他作業甚至 SSMS 查詢，間接導致輪詢停止；(3) 重送機制會持續產生 stx 檔案，造成檔案堆積惡性循環。

## 解法

在 OSSPolling.exe.config 中新增三個組態參數：(1) IGNORE_STX（Y/N）：控制是否只輪詢 acp 檔案、忽略 stx 檔案；(2) ENABLE_RESEND（Y/N）：控制是否處理重送訊息，設為 N 可避免持續產生 stx 檔案；(3) IGNORE_ACP（Y/N）：控制是否只輪詢 stx 檔案。修復版本：BE-V70R3.112，於 2025-07-03 發布。

## 相關資訊

- Jira: [BE-1141](https://ctil.atlassian.net/browse/BE-1141)
- Fix Version: BE-V70R3.112
- 解決日期: 2025-07-03
- 組件: polling
- 負責人: Sherman tse
- 附件: [image-20250702-023854.png](https://ctil.atlassian.net/rest/api/3/attachment/content/60947) | [image-20250702-024106.png](https://ctil.atlassian.net/rest/api/3/attachment/content/60948) | [Test case of [CS-1452]Issue_PRC_OSS Polling Delay issue on 6.3.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/61075)


## 相關截圖

<img src="/FAQ_test/attachments/BE-1141/image-20250702-023854.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1141/image-20250702-024106.png" style="max-width:100%;border-radius:6px;margin:4px 0">


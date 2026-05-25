---
project: BE
issue_key: BE-945
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-945
created: '2024-11-15'
resolved: '2024-11-18'
fix_version: ''
components:
- Data Interface
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: complete
---

BE-945:  Got timeout error after process Backend data sync

## 症狀

在 Coach CRM 後台數據同步過程中出現超時錯誤（Timeout Error）。當用戶建立包含會員資料的訂單、上傳至後台數據庫並執行後台數據同步時，系統無法成功將會員訂單發送至 CRM，並拋出超時異常。

## 根因

數據同步的 SQL 查詢使用了 LEFT JOIN 方式連接 crmlog 資料表，當資料量較大時，LEFT JOIN 會產生大量中間結果集，導致查詢執行時間過長，最終觸發超時錯誤。

## 解法

將 SQL 查詢語句中的 LEFT JOIN crmlog 改為使用 EXISTS / NOT EXISTS 子查詢來過濾 crmlog 記錄。此改動可大幅減少查詢掃描範圍，避免產生大量中間結果集，從而解決超時問題。

## 相關資訊

- Jira: [BE-945](https://ctil.atlassian.net/browse/BE-945)
- 解決日期: 2024-11-18
- 組件: Data Interface
- 負責人: Anson Cheung
- 附件: [CRM-20241115.log](https://ctil.atlassian.net/rest/api/3/attachment/content/48316) | [CRM-ERROR-20241115.log](https://ctil.atlassian.net/rest/api/3/attachment/content/48315) | [image-20241115-060656.png](https://ctil.atlassian.net/rest/api/3/attachment/content/48317)


## 相關截圖

![[../attachments/BE-945/image-20241115-060656.png]]

![[../attachments/BE-945/screenshot-link_att.jpg]]


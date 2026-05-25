---
project: FE
issue_key: FE-1908
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1908
created: '2026-03-26'
resolved: '2026-04-17'
fix_version: FE-75.004.2400.0000
components:
- Frontend
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1908: CJ_Customer data search_cannot see "membership available period" info

## 症狀

於POS查詢客戶資料時，無法顯示「會員有效期限（membership available period）」資訊，無論會員是否已過期皆不顯示

## 根因

FE程式碼（v75）的MemberPanelViewModel中缺少對vipdef資料集的fetch邏輯，導致會員額外定義（包含Stage Expiry Date）無法顯示。此問題僅發生在使用CS2000作為線上會員系統（ONLINECRMSYSTEM='CS2000'）的Coach JP站點

## 解法

在MemberPanelViewModel加入vipdef查詢處理邏輯（ProcessViPFound），使Coach JP站點可正確顯示會員階段資訊。修正包含於v750.04R23及後續版本

## 相關資訊

- Jira: [FE-1908](https://ctil.atlassian.net/browse/FE-1908)
- Fix Version: FE-75.004.2400.0000
- 解決日期: 2026-04-17
- 組件: Frontend
- 負責人: Joy Li
- 附件: [image-20260326-153925.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81964) | [image-20260326-154012.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81965) | [image-20260326-154748.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81966) | [image-20260326-154931.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81967) | [image-20260326-155044.png](https://ctil.atlassian.net/rest/api/3/attachment/content/81968)


## 相關截圖

![[../attachments/FE-1908/image-20260326-153925.png]]

![[../attachments/FE-1908/image-20260326-154012.png]]

![[../attachments/FE-1908/image-20260326-154748.png]]

![[../attachments/FE-1908/image-20260326-154931.png]]

![[../attachments/FE-1908/image-20260326-155044.png]]

> 共 21 張截圖，[查看全部](../attachments/FE-1908/)

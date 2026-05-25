---
project: FE
issue_key: FE-1383
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1383
created: '2024-05-09'
resolved: '2024-05-24'
fix_version: v750.04R04A
components:
- Day End
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: complete
---

FE-1383: day end issue caused by dbhist too large

## 症狀

dbhist.sdf 檔案過大導致 Day End 流程失敗。每次開立 Sales Memo 後，FE 會在 jouprint 表中插入記錄，但該表從未被清除，資料持續累積。

## 根因

jouprint 表沒有 purge 機制，隨著交易量增加，dbhist.sdf 不斷增長，最終超過系統可處理的大小限制，導致 Day End 異常。

## 解法

在 Day End 流程中加入清除 dbhist.sdf 中 jouprint 表的邏輯。同時需設定 dbtrans.tblconfig 中 ENABLECACHEPRINTDATA=Y。程式修正已納入 v750.04R04A。

## 相關資訊

- Jira: [FE-1383](https://ctil.atlassian.net/browse/FE-1383)
- Fix Version: v750.04R04A
- 解決日期: 2024-05-24
- 組件: Day End
- 負責人: Joy Li
- 附件: [image-20240513-031533.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41308) | [image-20240513-031923.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41307)


## 相關截圖

![[../attachments/FE-1383/image-20240513-031533.png]]

![[../attachments/FE-1383/image-20240513-031923.png]]


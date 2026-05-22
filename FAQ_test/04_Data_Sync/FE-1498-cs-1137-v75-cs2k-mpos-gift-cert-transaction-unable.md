---
project: FE
issue_key: FE-1498
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1498
created: '2024-09-08'
resolved: '2024-09-23'
fix_version: V75.04R04I-2
components:
- Front End
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

FE-1498: v75 - CS2K & MPOS Gift cert transaction unable post to DB.

## 症狀

V75 版本中，使用 CS2K 或 MPOS 進行 Gift Certificate（禮券）交易時，包含序號（SN）商品的銷售備忘錄無法成功 Posting 至後台資料庫，導致資料同步失敗。

## 根因

PCD 檔案中 record 33 與 record 32 的寫入順序不正確。當交易包含序號商品且使用 GC 付款時，錯誤的 record 順序導致後台 posting 程序無法正確解析檔案，引發 posting error。

## 解法

修正 PCD 檔案中 record 33 與 record 32 的產生順序，確保 GC 交易在包含 SN 商品時能正確被 posting 程序解析。修正版本：V75.04R04I-2。

## 相關資訊

- Jira: [FE-1498](https://ctil.atlassian.net/browse/FE-1498)
- Fix Version: V75.04R04I-2
- 解決日期: 2024-09-23
- 組件: Front End
- 負責人: Cy Lau

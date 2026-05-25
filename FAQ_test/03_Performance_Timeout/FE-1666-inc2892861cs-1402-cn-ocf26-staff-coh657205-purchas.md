---
project: FE
issue_key: FE-1666
issue_type: Bug PRD
status: Closed
tags:
title: "FE-1666-inc2892861cs-1402-cn-ocf26-staff-coh657205-purchas"
- 03_performance_timeout
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1666
created: '2025-04-03'
resolved: ''
fix_version: ''
components:
- Front End
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: complete
---

FE-1666: CN OCF26 staff COH657205  purchase balance issue

## 症狀

中國 OCF26 分店員工（E-type member COH657205）累積購買金額已超過年度限額 60,000 元，但 POS 前台沒有顯示任何購買限額超標嘅警告提示。經查發現 FE 端 tblvipamt 資料表中該員工嘅累積購買金額與 BE 端 vipfig 資料表不一致，部分月份銷售金額未正確同步到 FE。

## 根因

根因係 BE 與 FE 之間嘅 VIP 購買金額同步機制出現缺失。BE 端 vipfig 資料表記錄嘅每月購買金額係正確的，但 BE 透過 record type '14' 將更新資料推送至 FE 時，部分月份（2024-08 及 2025-02）嘅銷售資料並未成功寫入 FE Dbmas 嘅 tblvipamt 資料表，導致 FE 計算嘅累計金額偏低。具體原因可能係 z-file 傳輸過程中遺失或 FE 端接收更新時出現異常。另外，同一 staff code 喺不同 Till 嘅 tblvipamt 資料亦不一致，顯示同步機制並非 reliably 運作。

## 解法

先確認 BE 端 VIP type 'E' 嘅 Control Period 設定為 'F'（Yearly）及 viptyp_Start_month 設定正確（此案例為 4，即每年 4 月 1 日至翌年 3 月 31 日）。然後從 BE 端重新產生 vipfig z-file 並下發至所有 FE POS，以修補 tblvipamt 資料。長期需確保 BE 推送 vipfig 更新嘅機制穩定，且每個 Till 都能正確接收並寫入 tblvipamt。注意：此 Issue 狀態為 Closed 但無 resolution 標記，亦無 fix versions，可能透過手動 data patch 結案。

## 相關資訊

- Jira: [FE-1666](https://ctil.atlassian.net/browse/FE-1666)
- 組件: Front End
- 負責人: Sang
- 附件: [image-20250403-031646.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54349) | [image-20250403-031846.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54348) | [image-20250403-032110.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54350) | [image-20250403-032231.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54351) | [image-20250403-070655.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54368)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1666/image-20250403-031646.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1666/image-20250403-031846.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1666/image-20250403-032110.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1666/image-20250403-032231.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1666/image-20250403-070655.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 15 張截圖，[查看全部](/FAQ_test/attachments/FE-1666/)

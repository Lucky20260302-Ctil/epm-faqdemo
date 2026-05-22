---
project: FE
issue_key: FE-1611
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1611
created: '2025-01-20'
resolved: '2025-05-21'
fix_version: ''
components:
- DiscountVar
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

FE-1611: Issue-JP-J433&J378 POS didn't reflect Promo Code : CLE062A _RIN01439021

## 症狀

日本門店 J433 與 J378 的 POS 無法顯示促銷代碼 CLE062A，導致清倉活動銷售金額無法反映在報表中。其他門店（如 J425）正常顯示該促銷代碼。

## 根因

Zlog 檔案 z241226.06 更新 dbmas 失敗（「Fail to update zfile」），導致促銷代碼未成功匯入至門店本機資料庫（dbmas）。Zupdate 程式在更新失敗時未能產生明確的錯誤通知（PCD 代碼），使問題不易被發現。

## 解法

短期解決：於 BE UI 重新儲存促銷代碼，強制重新匯入 Zlog 至 dbmas。長期修正：v750.04R10 版本更新 Zupdate 程式，當更新 DB 失敗時寫入 PCD '81' 錯誤代碼（格式：81 P01 z22100301 0 Update DB Table ERROR），以便監控與排查。

## 相關資訊

- Jira: [FE-1611](https://ctil.atlassian.net/browse/FE-1611)
- 解決日期: 2025-05-21
- 組件: DiscountVar
- 負責人: Cy Lau
- 附件: [image-20250120-073645.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50736) | [image-20250120-074219.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50735) | [image-20250122-023047.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50843) | [image-20250122-023444.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50844) | [J433.241226 log.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/50750)

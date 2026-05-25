---
project: FE
issue_key: FE-1882
issue_type: Bug QA
status: Selected for Development (migrated)
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1882
created: '2026-02-10'
resolved: ''
fix_version: ''
components:
- Front End
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-1882: Incorrect amount of change after apply rounding: CHANGEROUND=R settings

## 症狀

Coach ANZ 區域 POS 啟用找零捨入功能（CHANGEROUND=R、CHANGERNDDEC=0.1、CHANGEROUND_ENABLE=Y）後，結帳畫面上顯示的找零金額與實際列印在收據上的找零金額不一致。例如：商品金額 $1,094.11，顧客支付 $1,095，畫面顯示應找零 $0.89，但收據上列印的找零金額卻為 $0.80。

## 根因

POS 在計算找零時的捨入邏輯存在不一致：畫面顯示階段的 Change 計算是以原始計算結果呈現，但在列印收據及實際交易提交時又進行了一次捨入（Round），兩階段的捨入時機與邏輯不同步，導致畫面顯示值與收據列印值出現偏差。

## 解法

開發團隊已修改找零捨入相關程式，修正畫面顯示與收據列印之捨入邏輯使其一致。修復程式已上傳至內部共用路徑（\\ds411\share\POS_FE_Release_64\20260210 Coach v750.04R21 - ANZ），待正式 QA 驗證後發佈。目前 Ticket 狀態為「Selected for Development (migrated)」。

## 相關資訊

- Jira: [FE-1882](https://ctil.atlassian.net/browse/FE-1882)
- 組件: Front End
- 負責人: Sherman tse
- 附件: [image-20260210-014710.png](https://ctil.atlassian.net/rest/api/3/attachment/content/77484) | [image-20260210-031721.png](https://ctil.atlassian.net/rest/api/3/attachment/content/77511) | [image-20260210-031736.png](https://ctil.atlassian.net/rest/api/3/attachment/content/77510) | [image-20260210-031750.png](https://ctil.atlassian.net/rest/api/3/attachment/content/77512)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1882/image-20260210-014710.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1882/image-20260210-031721.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1882/image-20260210-031736.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1882/image-20260210-031750.png" style="max-width:100%;border-radius:6px;margin:4px 0">


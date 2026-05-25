---
project: MP
issue_key: MP-756
issue_type: Bug QA
status: Closed
tags:
title: "MP-756-mpos-82mpos-v3302-ksj-mpos-unable-to-print-directl"
- 06_printing_hardware
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-756
created: '2025-03-14'
resolved: '2025-05-02'
fix_version: ''
components:
- MPOS
has_images: false
category: 06_Printing_Hardware
category_label: 列印與硬體
quality: complete
---

MP-756: MPOS v3.30.2 - KSJ MPOS unable to print directly after issue sales memo

## 症狀

MPOS IPA v3.30.2 版本在完成銷售交易後，應直接列印收據，但卻彈出 e-Receipt 選擇視窗。此功能僅應在已啟用電子收據的區域顯示，KSJ 地區不應出現此彈窗。

## 根因

IPA 版本 v3.30.2 中電子收據（e-Receipt）功能判斷邏輯有誤，未正確檢查該區域是否已啟用 e-Receipt 設定，導致所有區域完成交易後都會彈出選擇視窗，而非自動直接列印。

## 解法

更新 MPOS IPA 至修正版本 3.30.2-20250314.1，該版本修正了 e-Receipt 視窗的顯示邏輯，確保未啟用 e-Receipt 的區域可直接列印。

## 相關資訊

- Jira: [MP-756](https://ctil.atlassian.net/browse/MP-756)
- 解決日期: 2025-05-02
- 組件: MPOS
- 負責人: Daniel Leung
- 附件: [image-20250314-071649.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53115) | [Test case of MPOS-82-MPOS v3.30.2 - KSJ MPOS unable to print directly after issue sales memo.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/53232)


## 相關截圖

<img src="/FAQ_test/attachments/MP-756/image-20250314-071649.png" style="max-width:100%;border-radius:6px;margin:4px 0">


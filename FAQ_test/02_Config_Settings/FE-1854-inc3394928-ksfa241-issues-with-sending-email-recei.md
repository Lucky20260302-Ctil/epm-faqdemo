---
project: FE
issue_key: FE-1854
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1854
created: '2026-01-16'
resolved: ''
fix_version: ''
components:
- interface
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-1854: INC3394928 -KSFA241  Issues with sending email receipt to the customer

## 症狀

POS 顯示「send e-receipt fail, allow re-send later」錯誤，無法發送電子收據給客戶。僅特定銷售單據（如 20000044）的電子收據發送失敗，其他單據的電子收據可正常發送。API 回應錯誤為「No such host is known. (d:443)」，且該單據在 eReceipt 服務端無任何記錄。

## 根因

Web 伺服器上的配置設定不正確，導致呼叫 eReceiptRestfulService API 時無法解析目標主機名稱，出現 DNS 解析錯誤「No such host is known」。此為主機名稱解析失敗的網路層問題，非程式錯誤，因此 eReceipt API 端沒有收到請求記錄。

## 解法

Coach 支援團隊修正 Web 伺服器上的配置設定後問題已解決。若遇到相同錯誤，請檢查 Web 伺服器上 eReceipt API 的主機名稱設定是否正確，確認 DNS 可正常解析目標主機。重新發送電子收據可作為臨時處理方式，但需修正配置才能根本解決。

## 相關資訊

- Jira: [FE-1854](https://ctil.atlassian.net/browse/FE-1854)
- 組件: interface
- 負責人: Cy Lau
- 附件: [apilog_ereceipt_v2_20260116.sqlite](https://ctil.atlassian.net/rest/api/3/attachment/content/73606) | [eReceipt-20260116.log](https://ctil.atlassian.net/rest/api/3/attachment/content/73604) | [image-20260116-034942.png](https://ctil.atlassian.net/rest/api/3/attachment/content/73600) | [image-20260116-035145.png](https://ctil.atlassian.net/rest/api/3/attachment/content/73602) | [image-20260116-035705.png](https://ctil.atlassian.net/rest/api/3/attachment/content/73603)

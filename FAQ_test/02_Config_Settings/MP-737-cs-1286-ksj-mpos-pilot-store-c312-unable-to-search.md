---
project: MP
issue_key: MP-737
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-737
created: '2024-12-11'
resolved: '2025-03-13'
fix_version: ''
components:
- MPOS API
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

MP-737: KSJ mPOS: Pilot store C312 unable to search VIP

## 症狀

KSJ 試點門市 C312 的 mPOS 無法查詢 VIP 會員。當客戶使用家中電話號碼註冊會員時，以手機號碼進行 VIP 查詢會失敗，POS 端無法找到對應的會員資料。

## 根因

MPOS C360 查詢流程未更新至與 FEPOS 相同的新架構（doSearchAdv）。appsettings.json 中的 c360_brand 設定值為「KS」，但 C360 API 需要該值為「KS」才能查詢，同時前端又需要「N」才能正確處理。兩者衝突導致查詢失敗。另外，vipmas_access_brand 欄位長度限制也造成部分資料無法正確回傳。

## 解法

於 POS_API 的 appsettings.json 中新增獨立設定項「c360_vip_access_brand」，將 vipmas_access_brand 的輸出值與 c360_brand 分開控制。修正版本：POS_API v2.09.02_20241217。

## 相關資訊

- Jira: [MP-737](https://ctil.atlassian.net/browse/MP-737)
- 解決日期: 2025-03-13
- 組件: MPOS API
- 負責人: Sherman tse
- 附件: [image-20241211-054959.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49184) | [image-20241211-153744.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49206) | [image-20241211-153850.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49207) | [image-20241211-154830.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49208) | [image-20241212-015845.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49210)

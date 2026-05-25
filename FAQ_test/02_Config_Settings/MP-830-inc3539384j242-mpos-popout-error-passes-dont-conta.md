---
project: MP
issue_key: MP-830
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-830
created: '2026-04-27'
resolved: ''
fix_version: ''
components:
- MPOS
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

MP-830: J242 MPOS popout error "Passes don't contain empty strings or space characters" after scaned the QR code

## 症狀

J242 門市的 MPOS 在掃描 QR Code 後彈出錯誤訊息「Passes don't contain empty strings or space characters」，無法正常操作。即使檢查 dbtrans 設定正確、切換 Cloud IIS 與 Local IIS 後問題仍存在。

## 根因

MPOS 的 xconfig 設定檔內容異常或損壞，導致掃描 QR Code 時 Pass 驗證失敗，觸發該錯誤訊息。

## 解法

重新匯入 Local IIS 的 MPOS xconfig 設定檔，匯入後錯誤即消失。若使用 Cloud IIS，請先切換至 Local IIS 後再重新匯入 xconfig。

## 相關資訊

- Jira: [MP-830](https://ctil.atlassian.net/browse/MP-830)
- 組件: MPOS
- 負責人: Joy Li
- 附件: [image-20260428-015657.png](https://ctil.atlassian.net/rest/api/3/attachment/content/85531) | [image-20260428-015906.png](https://ctil.atlassian.net/rest/api/3/attachment/content/85533) | [image-20260428-020901.png](https://ctil.atlassian.net/rest/api/3/attachment/content/85539) | [J242 0427测试.mp4](https://ctil.atlassian.net/rest/api/3/attachment/content/85532)


## 相關截圖

![[../attachments/MP-830/image-20260428-015657.png]]

![[../attachments/MP-830/image-20260428-015906.png]]

![[../attachments/MP-830/image-20260428-020901.png]]

![[../attachments/MP-830/screenshot-85532_st.png]]


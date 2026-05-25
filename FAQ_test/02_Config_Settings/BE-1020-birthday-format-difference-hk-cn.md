---
project: ChainStorePlus
issue_key: BE-1020
issue_type: Bug QA
status: Closed
tags:
- 02_config_settings
- chainstoreplus
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1020
created: '2025-03-03'
resolved: '2025-04-29'
fix_version: ''
components:
- MPOS
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
title: 'BE-1020: Difference birthday format between HK and CN'
---
# BE-1020: Difference birthday format between HK and CN

## 問題

在香港與中國大陸的 POS 系統上，會員生日顯示格式不一致：香港僅顯示月份（如「July」），中國大陸則顯示完整日期（如「2021/07/06」）。使用者對哪種格式為正確設定感到困惑。

## 根因

此差異由 tblconfig 中的 ShowFullBirthday 參數控制：設定為 'Y' 時顯示完整生日日期（yyyy/MM/dd 格式）；設定為 'N' 時僅顯示生日月份。香港與中國大陸的此項設定值不同，導致顯示格式差異。

## 解法

可透過設定 tblconfig.ShowFullBirthday 參數來控制 POS 前端生日顯示格式。若需僅顯示月份，設定為 'N'；若需顯示完整日期，設定為 'Y'。此為前端設定項目，無需程式變更。

## 相關資訊

- **Jira：** [BE-1020](https://ctil.atlassian.net/browse/BE-1020)
- **Fix Version：** 無（設定調整，無需程式修正）
- **解決日期：** 2025-04-29
- **組件：** MPOS
- **附件截圖：** [image-20250303-101748.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52400)


## 相關截圖

<img src="../attachments/BE-1020/image-20250303-101748.png" style="max-width:100%;border-radius:6px;margin:4px 0">


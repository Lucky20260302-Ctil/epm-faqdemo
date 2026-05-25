---
project: FE
issue_key: FE-1655
issue_type: Bug QA
status: Closed
title: "FE-1655: User can still login to POS even his account is not in any RTM Domain Group"
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1655
created: '2025-03-20'
resolved: '2025-08-28'
fix_version: ''
components:
- Front End v720.02
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-1655: User can still login to POS even his account is not in any RTM Domain Group

## 症狀

使用者即使其帳號不在任何RTM網域群組中，仍可登入POS系統，導致AD網域權限驗證失效。此問題發生在ENABLEDASECROLE設定為'N'的情況下，系統完全跳過網域群組驗證，僅使用POS資料庫中的使用者角色進行驗證。

## 根因

ENABLEDASECROLE設定為'N'時，POS系統停用AD網域群組成員驗證，完全改為僅依據POS資料庫中的使用者角色來判斷登入權限。這導致不在任何RTM網域群組（RTMHK_FE*）中的使用者也能成功登入，形成安全漏洞。

## 解法

將POS升級至v720.01R07G或更新版本，並進行以下設定：EnableDASec='Y'、EnableDASecRole='G'、wiam_enable='Y'、wiam_grp_filter='RTMHK_FE'。此版本新增EnableDASecRole='G'模式，改為檢查使用者是否屬於wiam_grp_filter指定的網域群組，而非僅檢查POS資料庫中的使用者角色。

## 相關資訊

- Jira: [FE-1655](https://ctil.atlassian.net/browse/FE-1655)
- 解決日期: 2025-08-28
- 組件: Front End v720.02
- 負責人: Gavin Zhou
- 附件: [image-20250320-053413.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53450) | [image-20250320-053601.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53449) | [RE_ RTM WIAM rollout plan.msg](https://ctil.atlassian.net/rest/api/3/attachment/content/53448)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1655/image-20250320-053413.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1655/image-20250320-053601.png" style="max-width:100%;border-radius:6px;margin:4px 0">


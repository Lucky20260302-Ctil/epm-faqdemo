---
project: FE
issue_key: FE-1385
issue_type: Bug QA
status: Closed
title: "FE-1385: vbretail.ini missing Web3 config"
tags:
- 01_install_deploy
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1385
created: '2024-05-09'
resolved: '2024-05-24'
fix_version: v750.04R04A
components:
- Front End
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---

FE-1385: vbretail.ini missing Web3 config

## 症狀

POS 前端安裝後，vbretail.ini 設定檔缺少 [3P Module Config] 區段，導致 Web3 / 3P Module 相關連結無法正常運作。用戶無法透過 POS 前端存取第三方模組功能頁面。

## 根因

FE 安裝封包在建置時遺漏了 [3P Module Config] 配置區段，該區段包含 InstallationPath 參數，用於指定 3P Module 的伺服器 URL（QA 環境為 https://qacs2000web.coach.com/3PModule，PRD 環境為 https://cs2000web.coach.com/3PModule）。缺少此設定導致 POS 無法正確路由至第三方模組。

## 解法

於 FE 安裝封包中補回 [3P Module Config] 區段及其 InstallationPath 設定。修正後的封包已於 v750.04R04A 版本中發布，安裝後確認 3P Module 連結可正常存取。若遇到相同問題，請確認 vbretail.ini 中是否存在 [3P Module Config] 區段並檢查 InstallationPath 是否指向正確的伺服器 URL。

## 相關資訊

- Jira: [FE-1385](https://ctil.atlassian.net/browse/FE-1385)
- Fix Version: v750.04R04A
- 解決日期: 2024-05-24
- 組件: Front End
- 負責人: Andy Ko
- 附件: [image-20240522-090936.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41633)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1385/image-20240522-090936.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


---
project: FE
issue_key: FE-1745
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1745
created: '2025-08-18'
resolved: '2025-09-30'
fix_version: FE-75.004.1310.0000
components:
- Front End
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---

FE-1745: Fail to register OCF26 till A PC with CSPlus.Lic file

## 症狀

安裝 V75 POS 時，使用 CSPlus.Lic 授權檔註冊 Till A 失敗，系統報錯無法完成 POS 註冊。

## 根因

（1）CSPlus.Lic 授權檔中的授權序號（RKey）不支援 Till A-Z 範圍的 Till ID，導致 Till A 無法被識別；（2）授權檔已過期，系統拒絕註冊。

## 解法

（1）更新至 v750.04R13J（或 v750.04R14 / v750.05），該版本 License S/N (RKey) 已支援 Till A-Z 範圍；（2）若授權檔已過期，需重新產生有效的 CSPlus.Lic 檔案。Patch 路徑：\\ds411\share\POS_FE_Release_64\20250819 Coach v750.04R13J。

## 相關資訊

- Jira: [FE-1745](https://ctil.atlassian.net/browse/FE-1745)
- Fix Version: FE-75.004.1310.0000
- 解決日期: 2025-09-30
- 組件: Front End
- 負責人: Shaun_Huang
- 附件: [image-20250818-065746.png](https://ctil.atlassian.net/rest/api/3/attachment/content/63628) | [image-20250819-042400.png](https://ctil.atlassian.net/rest/api/3/attachment/content/63690) | [OCF26_a.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/63629)


## 相關截圖

![[../attachments/FE-1745/image-20250818-065746.jpg]]

![[../attachments/FE-1745/image-20250819-042400.jpg]]


---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3343
issue_type: ''
status: ''
title: "EPMTDCPROT-3343: [Phase 2 DEV] Sysadmin cannot cancel the delegation"
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3343
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-3343: [Phase 2 DEV] Sysadmin cannot cancel the delegation

## 症狀

Sysadmin 嘗試取消其他使用者建立的委派（Delegation）時出現錯誤，無法取消，該如何解決？

## 根因

根據 Comment (Michael Ren)：Sysadmin 可以取消委派，但必須符合以下三種情況之一：(1) admin 是 Delegator；(2) admin 是 Delegation-To 對象；(3) admin 是委派的創建者（Creator）。原先未正確涵蓋這三種場景，導致 Sysadmin 無法取消非自己創建的委派。

## 解法

修正 Phase 2 DEV 中的委派取消邏輯，確保 Sysadmin 在符合上述三種場景時可成功取消委派，不再出現錯誤訊息。

## 相關資訊

- Jira: [EPMTDCPROT-3343](https://ctil.atlassian.net/browse/EPMTDCPROT-3343)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-3343/image-20260120-032620.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3343/image-20260120-032643.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3343/image-20260120-073209.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3343/image-20260120-074931.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3343/image-20260120-075333.png" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 6 張截圖，[查看全部](/FAQ_test/attachments/EPMTDCPROT-3343/)

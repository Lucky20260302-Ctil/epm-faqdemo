---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3316
issue_type: ''
status: ''
title: "EPMTDCPROT-3316: [Phase 2 DEV] Delegation Email - Supplier Role"
tags:
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3316
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---

EPMTDCPROT-3316: [Phase 2 DEV] Delegation Email - Supplier Role

## 症狀

Supplier Role 委派電子郵件中，Delegator 與 Delegate-To 收到的任務資訊內容不一致，該如何處理？

## 根因

根據 Comment (William Qiu)：委派郵件通知實際上只會發送給 Delegate-To User，並同時抄送（CC）給提交者及 Delegator。然而 System Notification 介面上並未顯示 CC 資訊，導致使用者誤以為郵件內容不一致。

## 解法

將 Delegator 與 Delegate-To 的郵件模板（Email Template）內容同步一致，確保兩方收到的任務資訊相同；CC 資訊雖不顯示在 System Notification 上，但實際郵件發送時會正確抄送。

## 相關資訊

- Jira: [EPMTDCPROT-3316](https://ctil.atlassian.net/browse/EPMTDCPROT-3316)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-3316/image-20260114-033609.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3316/image-20260114-033628.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3316/image-20260114-033707.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3316/image-20260116-071239.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


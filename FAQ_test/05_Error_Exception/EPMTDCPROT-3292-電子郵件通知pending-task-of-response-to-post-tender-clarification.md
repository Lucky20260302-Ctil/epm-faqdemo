---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3292
issue_type: ''
status: ''
tags:
title: "EPMTDCPROT-3292-電子郵件通知pending-task-of-response-to-post-tender-clarification"
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3292
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-3292: 

## 症狀

電子郵件通知「Pending Task of Response to Post-Tender Clarifications」中的連結錯誤，供應商點擊後被重定向到內部portal（EPRO）而非正確的供應商入口，導致供應商無法直接回覆標後澄清（Post-Tender Clarification）。

## 根因

shortUrl 生成時以手動方式設置固定 domain，導致使用者收到的連結 domain 為寫死的值。先前測試環境中內部portal與供應商portal共用同一 domain，因此未發現問題；但 TDC Production 環境中內部portal與供應商portal使用不同 domain，導致供應商收到的電子郵件連結指向錯誤的內部portal。

## 解法

改用統一 function 生成 shortUrl，根據收件人身份（是否為供應商）自動判斷並選用對應的正確 domain。修復後已在多種郵件通知場景完成測試驗證，包括 RFQ 與 Tender 的 acknowledgement、NDA、Briefing、Offer Response、PTC (Technical/Fee)、PTN、LOA 等，確保各類通知連結均指向正確的入口。

## 相關資訊

- Jira: [EPMTDCPROT-3292](https://ctil.atlassian.net/browse/EPMTDCPROT-3292)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-3292/00b596866e604696ab232cdef2d24ca-20260115-073530.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3292/04ef8e127b9629628e8f9129dd50c90-20260115-073542.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3292/05dddfd14df0ee2e91c22f65275a9df-20260115-065516.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3292/081eb83cf7e67f06ab8a3270460758f-20260115-065649.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3292/082a47d6d1186601de97ff90f6a412d-20260115-065640.png" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 109 張截圖，[查看全部](/FAQ_test/attachments/EPMTDCPROT-3292/)

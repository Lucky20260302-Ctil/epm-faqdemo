---
project: ERM FEPOS
title: "FE-1643: [ACU-115] CN Member can't be created by QR code scanning or mobile number inputting"
issue_key: FE-1643
issue_type: Bug PRD
status: Closed
tags: [faq, erm-fepos]
jira_url: "https://ctil.atlassian.net/browse/FE-1643"
created: 2025-03-07
resolved: 2025-05-02
fix_version: "BEAPI V1.7.5"
components: [Front End]
---

# FE-1643: [ACU-115] CN Member can't be created by QR code scanning or mobile number inputting

## 問題

Coach 中國（CN）會員透過微信小程序註冊後，在 POS 端使用 QR Code 掃描或輸入手機號碼查詢會員時，會員資料可顯示但無法指派會員卡，點擊 Confirm 按鈕後出現錯誤，導致無法完成會員建立。

## 根因

BEAPI 在處理 CN 會員建立時，VIP 編號（vip no.）生成失敗，導致會員卡無法正確指派，進而使 Confirm 操作失敗。

## 解法

將 BEAPI 更新至 V1.7.5 版本（2025/03/07 發布），該版本修復了 VIP 編號生成失敗的問題。程式路徑：`\\ds411\public\samuel\beapi\v1.7.5_20250307`。

## 相關資訊

- **Jira：** [FE-1643](https://ctil.atlassian.net/browse/FE-1643)
- **Fix Version：** BEAPI V1.7.5
- **解決日期：** 2025-05-02
- **組件：** Front End
- **附件截圖：**
  - [image-20250307-063356.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52698)

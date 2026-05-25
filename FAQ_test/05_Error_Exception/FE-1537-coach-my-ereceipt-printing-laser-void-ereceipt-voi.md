---
project: FE
issue_key: FE-1537
issue_type: Bug QA
status: Closed
tags:
title: "FE-1537-coach-my-ereceipt-printing-laser-void-ereceipt-voi"
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1537
created: '2024-10-22'
resolved: '2025-02-21'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1537: Coach MY - ereceipt printing LASER - void eReceipt "Void Reason" is cut off

## 症狀

Coach 品牌使用 LASER 印表機列印 void eReceipt 時，「Void Reason」（作廢原因）文字在收據底部被裁切，無法完整顯示。

## 根因

報表範本 CaocheReceipt.rpt 中 Void Reason 欄位的行高（Line Height）不足，導致 LASER 列印時文字超出可顯示範圍而被截斷。

## 解法

修改報表範本 CaocheReceipt.rpt，將 Void Reason 欄位的行高擴展（Extended Line Height）。（KTS 241023 Jira FE-1537，適用版本 v750.04R08+ / v750.05）

## 相關資訊

- Jira: [FE-1537](https://ctil.atlassian.net/browse/FE-1537)
- 解決日期: 2025-02-21
- 組件: Front End
- 負責人: Sang
- 附件: [241023 FE-1537 Coach Void eReceipt - SHow Void Reason.pdf](https://ctil.atlassian.net/rest/api/3/attachment/content/47293) | [image-20241022-084329.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47266) | [image-20241023-030255.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47292)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1537/image-20241022-084329.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1537/image-20241023-030255.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">


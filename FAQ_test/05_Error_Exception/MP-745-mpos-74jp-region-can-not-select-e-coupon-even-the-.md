---
project: MP
issue_key: MP-745
issue_type: Bug PRD
status: Closed
tags:
title: "MP-745-mpos-74jp-region-can-not-select-e-coupon-even-the-"
- 05_error_exception
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-745
created: '2025-02-11'
resolved: '2025-05-02'
fix_version: ''
components:
- MPOS
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

MP-745: JP Region, can not select E-Coupon even the member we selected have available ecoupon

## 症狀

部署 COACH_MPOSWebAPI_R3.29.5d 修補程式後，日本區域 MPOS 無法顯示會員的可用電子優惠券（E-Coupon）。即使後端 API 正確回傳 124 張優惠券資料，MPOS 畫面仍顯示為空白，使用者無法選取任何優惠券。

## 根因

MPOS IPA 客戶端（v3.29.5-20250108.2）在處理 API 回傳的電子優惠券資料時存在渲染缺陷，導致有效的 API 回傳資料無法正確顯示於前端畫面。

## 解法

由開發人員 Daniel Leung 修復 MPOS IPA 程式，更新至版本 3.29.5-20250212.1 後即可正常顯示電子優惠券列表。修復版本：IPA 3.29.5-20250212.1。

## 相關資訊

- Jira: [MP-745](https://ctil.atlassian.net/browse/MP-745)
- 解決日期: 2025-05-02
- 組件: MPOS
- 負責人: Joseph_Hu
- 附件: [2025-02-11.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/51464) | [202502121402400000.mp4](https://ctil.atlassian.net/rest/api/3/attachment/content/51468) | [image-20250211-154045.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51448) | [image-20250211-163624.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51450) | [image-20250211-164244.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51451)


## 相關截圖

<img src="/FAQ_test/attachments/MP-745/image-20250211-154045.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-745/image-20250211-163624.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-745/image-20250211-164244.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-745/image-20250212-013533.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-745/image-20250212-013634.png" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 8 張截圖，[查看全部](/FAQ_test/attachments/MP-745/)

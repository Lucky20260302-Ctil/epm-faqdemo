---
project: FE
issue_key: FE-1660
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1660
created: '2025-03-25'
resolved: '2025-05-02'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1660: No member card created while scanning new registered member' QR code

## 症狀

在中國 POS 掃描新註冊會員的 QR Code 後，無法建立會員卡，系統彈出錯誤訊息「Object Reference not set to an instance of an object」。會員已於小程序會員中心註冊成功，但 POS 端無法正確識別並建立會員卡。

## 根因

因 SOW 需求關閉了 Acxiom CRM 的 upsert（更新/插入）功能（AcxiomCRM_enableUpsert 設為 disable），導致 CRM API 回傳的會員資料中缺少 vip_no（會員編號）欄位。FE 程式碼在處理回傳結果時，因 vip_no 為 null 而觸發 Null Reference 例外錯誤。

## 解法

BE API 修正版本 v1.7.12_20250326：新增檢查邏輯，當 Acxiom CRM 回傳的 profile 無 vip_no（會員編號）時，即使 upsert 功能被 disable，仍強制執行同步 upsert 以產生會員編號。同時，當 CRM 回傳錯誤時，於 profile search 的 data.jsonData 欄位回傳「ERROR|{code}|{message}」格式的錯誤資訊。

## 相關資訊

- Jira: [FE-1660](https://ctil.atlassian.net/browse/FE-1660)
- 解決日期: 2025-05-02
- 組件: Front End
- 負責人: Sherman tse
- 附件: [ACU-138.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/53742) | [beapi_apilog_20250325.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/53772) | [image-20250325-130157.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53740) | [image-20250325-130243.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53739) | [image-20250325-130303.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53741)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1660/image-20250325-130157.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1660/image-20250325-130243.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1660/image-20250325-130303.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1660/image-20250326-021522.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1660/image-20250326-023106.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 9 張截圖，[查看全部](/FAQ_test/attachments/FE-1660/)

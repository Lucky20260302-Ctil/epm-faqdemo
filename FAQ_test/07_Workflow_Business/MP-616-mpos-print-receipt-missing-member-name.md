---
project: MP
issue_key: MP-616
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-616
created: '2022-12-16'
resolved: '2023-11-16'
fix_version: ''
components:
- MPOS
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

MP-616: MPOS print receipt missing member name

## 症狀

MPOS 建立銷售備忘錄並選擇會員後，列印出的收據僅顯示會員編號，未顯示會員姓名。但以 Till POS 建立的相同銷售備忘錄則可正常列印會員姓名，導致門市人員無法在 MPOS 收據上辨識會員身分。

## 根因

問題根因為 Invtrx_Member_Name 欄位在 MPOS 建立銷售備忘錄時未被正確寫入，導致該欄位值為 null，收據列印時無法取得會員姓名進行顯示。

## 解法

此問題已於 MPOS 3.19.5 版本中修正（修補檔：\\ds411\share\CYLau\3.19.5\3.19.5-20221219.zip），修正後 MPOS 收據可正確顯示會員姓名。該修正同時涵蓋稅務豁免銷售備忘錄與 MM 折扣優惠券的相關處理邏輯。

## 相關資訊

- Jira: [MP-616](https://ctil.atlassian.net/browse/MP-616)
- 解決日期: 2023-11-16
- 組件: MPOS
- 負責人: Cy Lau
- 附件: [image-2022-12-16-18-13-59-960.png](https://ctil.atlassian.net/rest/api/3/attachment/content/40519) | [Screenshot_19.png](https://ctil.atlassian.net/rest/api/3/attachment/content/40516) | [Screenshot_20.png](https://ctil.atlassian.net/rest/api/3/attachment/content/40517) | [vbretail.ini](https://ctil.atlassian.net/rest/api/3/attachment/content/40522)


## 相關截圖

<img src="/FAQ_test/attachments/MP-616/Screenshot_19.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-616/Screenshot_20.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-616/image-2022-12-16-18-13-59-960.png" style="max-width:100%;border-radius:6px;margin:4px 0">


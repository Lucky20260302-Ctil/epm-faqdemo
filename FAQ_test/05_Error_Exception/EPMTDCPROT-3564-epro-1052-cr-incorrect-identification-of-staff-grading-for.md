---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3564
issue_type: ''
status: ''
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3564
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-3564: EPRO-1052 [CR] Incorrect identification of staff grading for DOI approval

## 症狀

DOI 表單中「Declaration of Conflict Grade」欄位顯示錯誤。低於 Grade E 的員工（如 Fanny Kam）發起 DOI 時，欄位錯誤顯示為「Grade E or above」而非其實際職級，導致審批路由被錯誤觸發至 Tender Board。依規範：低於 Grade E 員工的 DOI 應由 Grade E 或以上審批；Grade E 或以上員工的 DOI 才應由 Tender Board 審批。

## 根因

系統從 workflow/HR 獲取 staff grade 資訊的邏輯存在缺陷：DOI 表單生成時未能正確讀取發起人的實際職級，而是採用了預設或錯誤的 grade 對應值（一律顯示「Grade E or above」），導致審批路由規則失效。Jeffrey wen 在 Comment 中的測試用例分析明確指出此為 grade 識別邏輯錯誤。

## 解法

修正 DOI 表單中的 staff grade 識別邏輯，確保從 HR/workflow 系統正確獲取發起人職級資訊，並依職級分流審批路由：(a) 低於 Grade E → 審批路由至 Grade E 或以上審批人；(b) Grade E 或以上 → 審批路由至 Tender Board。同時確保 Tender Board 成員須先完成自身 DOI 方可進行 approval。此修正已納入 Batch 3 測試，需建立新的 DOI e-form，測試通過。

## 相關資訊

- Jira: [EPMTDCPROT-3564](https://ctil.atlassian.net/browse/EPMTDCPROT-3564)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-3564/image-20260511-070632.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3564/image-20260511-070647.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3564/image-20260511-070701.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3564/image-20260511-090750.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3564/image-20260511-090811.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 11 張截圖，[查看全部](/FAQ_test/attachments/EPMTDCPROT-3564/)

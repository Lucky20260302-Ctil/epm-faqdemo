---
project: BE
issue_key: BE-655
issue_type: Bug QA
status: Closed
tags:
- 06_printing_hardware
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-655
created: '2022-09-22'
resolved: '2023-02-16'
fix_version: ''
components:
- Backend (Web)
has_images: false
category: 06_Printing_Hardware
category_label: 列印與硬體
quality: complete
---
BE-655: Cannot print Amendment list successfully after make an amendment of delivery order batch

| 問題
在 Backend「Delivery Order Batch Information (IC1002)」功能中，對送貨單批次進行修改（Amendment）後，點擊「Print Amendment list」列印修改清單時，系統彈出「Data entry in progress」錯誤訊息，無法列印。

| 根因
修改送貨單批次後，系統對該筆資料保留了 Exclusive Lock（獨佔鎖定），導致列印功能無法存取該筆資料，觸發「Data entry in progress」錯誤。

| 解法
點擊「Modify」按鈕進入修改模式，再點擊「Remove Exclusive Lock」按鈕清除獨佔鎖定狀態後，即可正常列印 Amendment list。

| 相關資訊
- Jira: [BE-655](https://ctil.atlassian.net/browse/BE-655)
- 解決日期: 2023-02-16
- 組件: Backend (Web)
- 負責人: Ken Lam
- 附件: [image-2022-09-22-10-54-41-283.png](https://ctil.atlassian.net/rest/api/3/attachment/content/39718) | [image-2023-02-15-17-18-29-867.png](https://ctil.atlassian.net/rest/api/3/attachment/content/39720)
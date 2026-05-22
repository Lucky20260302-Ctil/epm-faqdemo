---
project: FE
issue_key: FE-1755
issue_type: Bug PRD
status: Closed
tags:
- 06_printing_hardware
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1755
created: '2025-09-29'
resolved: ''
fix_version: ''
components:
- Front End
has_images: false
category: 06_Printing_Hardware
category_label: 列印與硬體
quality: complete
---

FE-1755: CN Laser printer cannot reprint sales memo in till2 : Printing Error

## 症狀

中國分店 OC63 嘅 Till 2 無法使用 Laser Printer 重新列印銷售備忘錄（Sales Memo），出現「Printing Error」。即使重啟打印機和電腦、修復程式、嘗試列印 PDF 都無法解決。該 Till 係首次嘗試列印 Crystal Report 格式嘅備忘錄。

## 根因

根因係該 POS 電腦缺少 Crystal Report Runtime Library（Crystal Reports 運行時庫），或者現有安裝嘅 Runtime Library 已損壞。POS 在生成銷售備忘錄時需要調用 Crystal Report 引擎來渲染報表，若 Runtime Library 不存在或版本不符，就會導致列印失敗。呢個情況常見於新設置嘅 POS 電腦或系統更新後未一併安裝 Crystal Report 組件。

## 解法

在受影響嘅 POS 電腦上重新安裝 Crystal Report Runtime Library。安裝完成後無需重啟，直接測試重新列印銷售備忘錄即可恢復正常。此為常見嘅 POS 列印問題排查步驟之一，若日後遇到類似情況可優先檢查 Crystal Report Runtime 是否正確安裝。

## 相關資訊

- Jira: [FE-1755](https://ctil.atlassian.net/browse/FE-1755)
- 組件: Front End
- 負責人: Tovi Wang
- 附件: [CN OC63.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/65953) | [image-20250929-084132.png](https://ctil.atlassian.net/rest/api/3/attachment/content/65952) | [image-20250929-085410.png](https://ctil.atlassian.net/rest/api/3/attachment/content/65954) | [屏幕截图 2025-09-29 161507.png](https://ctil.atlassian.net/rest/api/3/attachment/content/65948)

---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "J242 MPOS popout error 'Passes don't contain empty strings or space characters' after scanned the QR"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: MP-830
resolved: 
fix-version: ""
---

# MP-830: [INC3539384]J242 MPOS popout error "Passes don't contain empty strings or space characters" after scaned the QR code

## 問題

J242 MPOS popout error "Passes don't contain empty strings or space characters" after scanned the QR code.
Troubleshooting:
1.Double checked and compared the dbtrans config,the config is correct.
2.change the MPOS from Cloud IIS to Local IIS.Re-import MPOS xconfig,same error still.
1.error:
2.Video
3.
POS version:75.004.1404.0000
MPOS version:3.30.3

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2026-04-28):
@@Daniel Leung @@Joy Li  Could you help to take a look this MPOS error and give me some advice?Thanks!
**Joy Li** (2026-04-28):
@@Tovi Wang  Can you share the QR code from till 0 which user scan?
**Tovi Wang** (2026-04-28):
@@Joy Li QR code here.It's also included in the screen recording.Please help to confirm.If need any other info please ping me.Thanks!
**Tovi Wang** (2026-05-13):
Re-import Local IIS MPOS xconfig.error gone.

## 相關資訊

- Jira: [MP-830](https://ctil.atlassian.net/browse/MP-830)
- Fix Version: 未記錄
- 解決日期: 未記錄

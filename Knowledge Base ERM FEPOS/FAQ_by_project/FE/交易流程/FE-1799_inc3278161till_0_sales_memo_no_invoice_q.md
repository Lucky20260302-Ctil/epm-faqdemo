---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "PRC OC231 POSv75"
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: FE-1799
resolved: 
fix-version: ""
---

# FE-1799: [INC3278161]Till 0 sales memo no invoice QR code

## 問題

PRC OC231 POSv75
Till 0 all sales memo no invoice QR code.
checked the value of invtrx_prt_einv in dbhist.sdf/jouinvh of memo ‘00026484' is ‘N’, updated to Y, still can’t print qrcode.
compare the dbtrans from OC231till0 and the dbtrans from OC134till0 which can print qrcode normally. have 2 diff about Qrcode and updated, but still failed to print.
all the logs on OC231 till0 has been uploaded, please help to check.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Automation for Jira** (2025-11-06):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-11-06):
@@pierre.shi Please verify is QR Code file ‘COH_WC.BMP’ exist in OC231 till0 CSPLUS application folder
**pierre.shi** (2025-11-06):
Hi@@Sangchecked that this file is existed in retdata6 folder, not found in csplus folder.
Checked on OC134till0, also the file is existed in retdata6 folder, not found in csplus folder.
**Sang** (2025-11-06):
@@pierre.shi  copy to CSPLUS folder, and try again
**pierre.shi** (2025-11-06):
@@Sang ok, let me try.
**pierre.shi** (2025-11-07):
Hi@@Sang copied to csplus folder, issue still.
**Sang** (2025-11-18):
@@pierre.shi @@Joy Li set Memo #00026713  jouinvH.invtrx_Prt_einv='Y'
**pierre.shi** (2025-11-19):
Hi@@Sang这个我拿的是最早之前的dbtrans和dbhist。后面我测试过，改了这个字段也没用。如果需要的话，我可以再找个单子测试下，拿最新的dbhist.sdf
**pierre.shi** (2025-11-19):
@@Sang 他们现在新生成的单子都是不能打印qrcode的，也不弹这个选择窗口
**Sang** (2025-11-21):
1. 
2.
**pierre.shi** (2025-11-24):
Hi@@Sang tblconfig.EINV_QRCODE_ENABLE is 'Y'

## 相關資訊

- Jira: [FE-1799](https://ctil.atlassian.net/browse/FE-1799)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
project: FE
issue_key: FE-1772
issue_type: Bug DEV
status: DEV Done
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1772
created: '2025-10-21'
resolved: ''
fix_version: ''
components:
- Front End v750.01R01A
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1772: PRC OC316 POSv75,Sales memo 00004891 invoice QR code can't be printed out

| 問題
POS 銷售備忘錄（Sales Memo）列印時，特定單號（如 00004891）的電子發票 QR code 無法列印出來，其他銷售備忘錄則正常。

| 根因
資料庫欄位 dbhist.[jouinvh].invtrx_prt_einv 未設定為 'Y'，導致該筆交易的電子發票 QR code 列印功能未啟用。

| 解法
手動更新資料庫：將 dbhist.[jouinvh].invtrx_prt_einv 設為 'Y' 後，重新列印即可正常顯示 QR code。（KTS 對應版本：v750.04R13D+，已修正 CustomerReceipt 佈局與 Sales Memo 對齊）

| 相關資訊
- Jira: [FE-1772](https://ctil.atlassian.net/browse/FE-1772)
- 組件: Front End v750.01R01A
- 負責人: pierre.shi
- 附件: [image-20251021-033851.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67289) | [image-20251021-034119.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67288) | [image-20251022-073746.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67396) | [image-20251022-092839.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67406) | [image-20251022-104533.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67408)
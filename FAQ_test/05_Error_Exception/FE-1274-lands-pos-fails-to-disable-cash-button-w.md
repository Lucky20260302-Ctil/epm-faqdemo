---
project: FE
issue_key: FE-1274
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- frontend
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1274
created: '2023-07-18'
resolved: '2023-08-08'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1274: [Lands] POS fails to disable Cash button when order needs to be refunded'
---
# FE-1274: [Lands] POS fails to disable Cash button when order needs to be refunded

## 問題描述

Reproduce step:

1. Add an item into the sales memo page

2. Change the item become -1 to process refund

3. To Payment page

Existing result:

POS fails to disable Cash button when order needs to be refunded

 

Remark:

VM: .245 (Lands side)

Tblsyscon set:

- Disable Cash/Cheque Refund (Syscon_Issue_Cashret_Flag='N', Syscon_Issue_RetVou_Flag='N')

- Enable Return Voucher (Syscon_Issue_Refund_Flag='Y')

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/dedfb6da-5989-4c7f-a5fe-c4c09fdad6eb)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/dedfb6da-5989-4c7f-a5fe-c4c09fdad6eb)

## 相關資訊

- **Jira:** [FE-1274](https://ctil.atlassian.net/browse/FE-1274)
- **解決方式:** Done
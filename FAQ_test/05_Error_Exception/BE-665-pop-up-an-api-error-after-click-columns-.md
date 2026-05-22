---
project: BE
issue_key: BE-665
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-665
created: '2022-11-01'
resolved: '2023-01-06'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-665: Pop up an api error after click Columns in Vendor Delivery Note'
---
# BE-665: Pop up an api error after click Columns in Vendor Delivery Note

## 問題描述

env: [https://172.16.138.55/ChainStorePlus_AIGLE/rc2001](https://172.16.138.55/ChainStorePlus_AIGLE/rc2001)

Location: 

Process > Stock receive > Vendor delivery note maintenance

Reproduce steps:

1. To Vendor delivery note maintenance

2. Click into one of the records

3. Click Item information tab

4. click Columns: Color / Size / inseam

Existing result:

Pop up an Api error: API Error [Request ID : 2022110110371419] (2022110110371035 Retry )

Object reference not set to an instance of an object.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d39b55a7-fc7f-4537-a669-caeb2920eab1)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d39b55a7-fc7f-4537-a669-caeb2920eab1)

## 相關資訊

- **Jira:** [BE-665](https://ctil.atlassian.net/browse/BE-665)
- **解決方式:** Done
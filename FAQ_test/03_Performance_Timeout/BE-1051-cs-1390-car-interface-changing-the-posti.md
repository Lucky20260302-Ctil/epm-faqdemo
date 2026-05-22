---
project: BE
issue_key: BE-1051
issue_type: SOW
status: Closed
tags:
- 03_performance_timeout
- be
- data-interface
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1051
created: '2025-04-11'
resolved: '2025-05-12'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1051: [CS-1390] CAR Interface Changing the posting date time to transaction hour-min'
---
# BE-1051: [CS-1390] CAR Interface Changing the posting date time to transaction hour-min

## 問題描述

Currently, CAR Interface file, the posting date time is using the server time which is HKT. Tapestry would like to get the regional date time especially for JP and KR since they have 1 hour advance to HKT. The solution is to put the transaction date and time to the posting date & time fields. 

> 📎 **image-20250411-013213.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0a42dd43-9333-4542-9359-47b7cd8a8a70)（需 Jira 登入）
Changing the posting date time to **transaction hour-min**

P|J801|00207838|20250223|D|1|196395660940|CY698|IMXXA|||01|3|1|0.00|JXXXX0003641186|**20250223|hhmm00**

 

a) hh = jouinv_hour, joudep_hour, jouser_hh, jougic_hour

b) mm = jouinv_mn, joudep_mn, jouser_mn, jougic_min

c) date = jouinv_date, joudep_date, jouser_date, jougic_date

The change will apply to Sales Memo - Item Layout, Sales Memo - Item Discount Layout, Payment Detail Layout, Deposit Memo - Item Layout, Service Memo - Item Layout, Gift Cert Memo - Header Layout. 



## 附件截圖

1. 📎 **image-20250411-013213.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0a42dd43-9333-4542-9359-47b7cd8a8a70)

## 相關資訊

- **Jira:** [BE-1051](https://ctil.atlassian.net/browse/BE-1051)
- **解決方式:** Done
- **標籤:** CAR
---
project: BE
issue_key: BE-935
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- backend-(chainstoreplus-7.0)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-935
created: '2024-11-06'
resolved: '2024-12-24'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-935: Item Additional Retail Price shows the On Sale Price Record'
---
# BE-935: Item Additional Retail Price shows the On Sale Price Record

## 問題描述

Receive a report that the Additional Retail Price page shows the On Sale Price Record in Item Master Maintenance. We need to filter the On Sale Price Record by the following logic.

select * from itmprx where (isnull(itmprx_onsale_disc_1,'') = ‘' and isnull(itmprx_onsale_disc_2,'') = '' and itmprx_sell_price_bx = 0) or (itmprx_sell_price_bx <> 0)



## 相關資訊

- **Jira:** [BE-935](https://ctil.atlassian.net/browse/BE-935)
- **解決方式:** Done
---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Receive a report that the Additional Retail Price page shows the On Sale Price Record in Item Master"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-935
resolved: 2024-12-24
fix-version: ""
---

# BE-935: Item Additional Retail Price shows the On Sale Price Record

## 問題

Receive a report that the Additional Retail Price page shows the On Sale Price Record in Item Master Maintenance. We need to filter the On Sale Price Record by the following logic.
select * from itmprx where (isnull(itmprx_onsale_disc_1,'') = ‘' and isnull(itmprx_onsale_disc_2,'') = '' and itmprx_sell_price_bx = 0) or (itmprx_sell_price_bx <> 0)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-24

## 相關資訊

- Jira: [BE-935](https://ctil.atlassian.net/browse/BE-935)
- Fix Version: 未記錄
- 解決日期: 2024-12-24

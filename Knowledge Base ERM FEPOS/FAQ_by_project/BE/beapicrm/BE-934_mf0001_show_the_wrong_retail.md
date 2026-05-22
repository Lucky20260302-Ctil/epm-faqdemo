---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Once we create the onsales record, it make the MF0001 show the work price record. Please refer below"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-934
resolved: 2024-12-03
fix-version: ""
---

# BE-934: MF0001 Show the wrong retail

## 問題

Once we create the onsales record, it make the MF0001 show the work price record. Please refer below showshort.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-03
### Jira Comments (9 則)
**Andrew_Au** (2024-11-06):
@@Jason Wu @@Terence Tsang @@Cy Lau
**Andrew_Au** (2024-11-06):
**Andrew_Au** (2024-11-06):
@@Bobby
**Bobby** (2024-11-06):
Since the Additional Retail Price page shows the On Sale Price Record in Item Master Maintenance. We need to filter the On Sale Price Record by the following logic.
select * from itmprx where (isnull(itmprx_onsale_disc_1,'') = ‘' and isnull(itmprx_onsale_disc_2,'') = '' and itmprx_sell_price_bx = 0) or (itmprx_sell_price_bx <> 0)
**Jerry Wong** (2024-11-08):
Prorunner Backend Web Release
\\ds411\CSMS70\delivery\prorunner\UAT\Backend (Web)\2024-11-07
Prorunner Backend .Net Release
\\ds411\CSMS70\delivery\prorunner\UAT\BackEnd.Net\2024-11-07
Lands Backend Web Release
\\ds411\CSMS70\delivery\lands\UAT\Backend (Web)\2024-11-07
Lands Backend .Net Release
\\ds411\CSMS70\delivery\lands\UAT\Backend.Net\2024-11-07
**Cy Lau** (2024-12-02):
@@Jerry Wong
Please state the source patch / control on [BackEnd.Net](http://BackEnd.Net)
**Cy Lau** (2024-12-02):
Current state treat as 
Not include Coach
**Andrew_Au** (2024-12-03):
Updated the web application and .net application to Prorunner production environment.
**Jerry Wong** (2024-12-03):
@@Cy Lau
Prorunner Backend API
[https://git.e-tendering.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-backend-api/-/tree/Prorunner-2024-10-04-OR0005-Update?ref_type=heads](https://git.e-tendering.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-backend-api/-/tree/Prorunner-2024-10-04-OR0005-Update?ref_type=heads)
Lands Backend API
[https://git.e-tendering.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-backend-api/-/tree/2024/11/06-Fix-BE-934-MF0001-Show-the-wrong-retail?ref_type=heads](https://git.e-tendering.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-backend-api/-/tree/2024/11/06-Fix-BE-934-MF0001-Show-the-wrong-retail?ref_type=heads)

## 相關資訊

- Jira: [BE-934](https://ctil.atlassian.net/browse/BE-934)
- Fix Version: 未記錄
- 解決日期: 2024-12-03

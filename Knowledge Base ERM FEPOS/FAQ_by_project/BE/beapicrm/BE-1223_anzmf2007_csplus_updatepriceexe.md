---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "On 13/1 got reports :"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: BE-1223
resolved: 
fix-version: ""
---

# BE-1223: [ANZ][MF2007] CSPLUS_updateprice.exe

## 問題

On 13/1 got reports :
Please investigate and suggest how support should help for providing information to trace includes but not limited to :
1. 
2.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Jerry Wong** (2026-01-19):
after my finding, the error message should be shown when running update itmprx sql then return 0 rows affected in SQL DB, so maybe the sql cannot find the original itmprx row by using all field instead of using index.
Module_CSDBUpdateObj.vb in CSDataInterface:
file import type = 118
**Jerry Wong** (2026-01-19):
Update sql sample:
UPDATE itmprx SET itmprx_item_no = '101                           '
, itmprx_country = ''
, itmprx_group = ''
, itmprx_col = 'QBLVW     '
, itmprx_size = ''
, itmprx_inseam = ''
, itmprx_loc = 'J805      '
, itmprx_onsale_price_bx_1 = 108.90
, itmprx_onsale_fr_date_1 = '1/20/2026 12:00:00 AM'
, itmprx_onsale_to_date_1 = '1/20/2026 12:00:00 AM'
, itmprx_sell_price_bx = 0.00
, itmprx_update_flag = NULL
, itmprx_avg_cost_bx = 0.00
, onsale_pri_bx_2 = 13200.00
, onsale_fr_date_2 = '2/9/2024 12:00:00 AM'
, onsale_to_date_2 = '1/19/2026 12:00:00 AM'
, itmprx_eff_date = NULL
, itmprx_new_retail_price_bx = 0.00
, itmprx_new_org_price_bx = 0.00
, itmprx_org_price_bx = 0.00
, itmprx_onsal_disc1 = 0
, itmprx_onsal_disc2 = 0.00
, itmprx_disc_code_1 = '001'
, itmprx_disc_code_2 = 'BLANK'
, itmprx_combine_key = '101                                               QBLVW                         J805      '
WHERE
 (itmprx_item_no = '101                           '
  OR (itmprx_item_no IS NULL
      AND '101                           ' IS NULL )
  )
 AND  (itmprx_country = '          '
  OR (itmprx_country IS NULL
      AND '          ' IS NULL )
  )
 AND  (itmprx_group = '          '
  OR (itmprx_group IS NULL
      AND '          ' IS NULL )
  )
 AND  (itmprx_col = 'QBLVW     '
  OR (itmprx_col IS NULL
      AND 'QBLVW     ' IS NULL )
  )
 AND  (itmprx_size = '          '
  OR (itmprx_size IS NULL
      AND '          ' IS NULL )
  )
 AND  (itmprx_inseam = '          '
  OR (itmprx_inseam IS NULL
      AND '          ' IS NULL )
  )
 AND  (itmprx_loc = 'J805      '
  OR (itmprx_loc IS NULL
      AND 'J805      ' IS NULL )
  )
 AND  (itmprx_onsale_price_bx_1 = 13200.00
  OR (itmprx_onsale_price_bx_1 IS NULL
      AND 13200.00 IS NULL )
  )
 AND  (itmprx_onsale_fr_date_1 = '2/9/2024 12:00:00 AM'
  OR (itmprx_onsale_fr_date_1 IS NULL
      AND '2/9/2024 12:00:00 AM' IS NULL )
  )
 AND  (itmprx_onsale_to_date_1 = '12/31/9999 12:00:00 AM'
  OR (itmprx_onsale_to_date_1 IS NULL
      AND '12/31/9999 12:00:00 AM' IS NULL )
  )
 AND  (itmprx_sell_price_bx = 0.00
  OR (itmprx_sell_price_bx IS NULL
      AND 0.00 IS NULL )
  )
 AND  (itmprx_update_flag = NULL
  OR (itmprx_update_flag IS NULL
      AND NULL IS NULL )
  )
 AND  (itmprx_avg_cost_bx = 0.00
  OR (itmprx_avg_cost_bx IS NULL
      AND 0.00 IS NULL )
  )
 AND  (onsale_pri_bx_2 = 17600.00
  OR (onsale_pri_bx_2 IS NULL
      AND 17600.00 IS NULL )
  )
 AND  (onsale_fr_date_2 = '2/8/2024 12:00:00 AM'
  OR (onsale_fr_date_2 IS NULL
      AND '2/8/2024 12:00:00 AM' IS NULL )
  )
 AND  (onsale_to_date_2 = '2/8/2024 12:00:00 AM'
  OR (onsale_to_date_2 IS NULL
      AND '2/8/2024 12:00:00 AM' IS NULL )
  )
 AND  (itmprx_eff_date = NULL
  OR (itmprx_eff_date IS NULL
      AND NULL IS NULL )
  )
 AND  (itmprx_new_retail_price_bx = 0.00
  OR (itmprx_new_retail_price_bx IS NULL
      AND 0.00 IS NULL )
  )
 AND  (itmprx_new_org_price_bx = 0.00
  OR (itmprx_new_org_price_bx IS NULL
      AND 0.00 IS NULL )
  )
 AND  (itmprx_org_price_bx = 0.00
  OR (itmprx_org_price_bx IS NULL
      AND 0.00 IS NULL )
  )
 AND  (itmprx_onsal_disc1 = 0.00
  OR (itmprx_onsal_disc1 IS NULL
      AND 0.00 IS NULL )
  )
 AND  (itmprx_onsal_disc2 = 0.00
  OR (itmprx_onsal_disc2 IS NULL
      AND 0.00 IS NULL )
  )
 AND  (itmprx_disc_code_1 = 'BLANK     '
  OR (itmprx_disc_code_1 IS NULL
      AND 'BLANK     ' IS NULL )
  )
 AND  (itmprx_disc_code_2 = 'BLANK     '
  OR (itmprx_disc_code_2 IS NULL
      AND 'BLANK     ' IS NULL )
  )
 AND  (itmprx_combine_key = '101                                               QBLVW                         J805      '
  OR (itmprx_combine_key IS NULL
      AND '101                                               QBLVW                         J805      ' IS NULL )
  )
**Andrew_Au** (2026-05-05):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [BE-1223](https://ctil.atlassian.net/browse/BE-1223)
- Fix Version: 未記錄
- 解決日期: 未記錄

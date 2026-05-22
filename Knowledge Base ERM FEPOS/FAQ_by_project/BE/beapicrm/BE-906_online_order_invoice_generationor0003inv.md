---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "step:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-906
resolved: 2025-02-27
fix-version: ""
---

# BE-906: Online Order Invoice Generation（OR0003）：Invoice Generation时，提示Save Failed

## 問題

step:
1、选择order No. 为‘‘00000004’’
2、鼠标右击
3、点击Invoice Generation

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-27
### Jira Comments (1 則)
**Jerry Wong** (2024-09-30):
jouinv_delivery_charge_item_code = itmast_item_no
jouinv_def_pay = paytab_code
required to set the value that is existing in corresponding table

## 相關資訊

- Jira: [BE-906](https://ctil.atlassian.net/browse/BE-906)
- Fix Version: 未記錄
- 解決日期: 2025-02-27

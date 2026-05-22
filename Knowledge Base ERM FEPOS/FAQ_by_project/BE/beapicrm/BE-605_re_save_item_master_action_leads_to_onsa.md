---
tags: [faq, be, beapicrm]
component: "Master"
symptom: "<u>**Basic Information**</u>"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-605
resolved: 2022-06-13
fix-version: ""
---

# BE-605: Re-save Item Master action leads to Onsales Price Data clear up 

## 問題

<u>**Basic Information**</u>
Ticket: RIN00998495
Region: Coach PRC
SKU: 5476
Incident Date: 2022-06-04
**<u>Scenario</u>**
After re-saving Item in Item Master, the Onsales price page of related Item will show as empty.
**<u>Reproduce Steps</u>**
1. In APABIQWPOSAPP21 (QA environment)
2. In Additional On Sales Price Information (MF2003), it shows some data which has not been expired.
3. Item Master Maintenance (MF0001), Re-save Item ‘1006’
4. Back to Additional On Sales Price Information (MF2003), All data of Item ‘1006’ are showing empty.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-06-13

## 相關資訊

- Jira: [BE-605](https://ctil.atlassian.net/browse/BE-605)
- Fix Version: 未記錄
- 解決日期: 2022-06-13

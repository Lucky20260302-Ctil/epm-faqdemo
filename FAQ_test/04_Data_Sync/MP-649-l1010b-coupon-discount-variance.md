---
project: MP
issue_key: MP-649
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-649
created: '2023-04-27'
resolved: '2024-08-30'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-649: L1010B Coupon Discount Variance'
---
# MP-649: L1010B Coupon Discount Variance

## 問題描述

Test data: COACH JP

FE 172.16.138.37

IIS 172.16.138.37 (region=18, J999) [http://172.16.138.37/sanyoservice.api.fe](https://172.16.138.247/sanyoservice.api.fe)

BE: 172.16.138.8

Item: 
W014 MAH ^WMN
W031 ACN ^WMN

Member : 
J101WJ00000163 
J101WJ00051712 
J999WJ00000120

 Ecoupon: L1010B

EC L1010BC0001-L1010BC0060

 

Case 1: 1item 1 coupon



## 相關資訊

- **Jira:** [MP-649](https://ctil.atlassian.net/browse/MP-649)
- **解決方式:** Done
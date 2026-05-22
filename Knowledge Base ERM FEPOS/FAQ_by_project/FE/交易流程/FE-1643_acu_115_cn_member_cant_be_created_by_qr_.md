---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "CN Test POS IP: 10.33. 248.4"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1643
resolved: 2025-05-02
fix-version: ""
---

# FE-1643: [ACU-115] CN Member can't be created by QR code scanning or mobile number inputting

## 問題

CN Test POS IP: 10.33. 248.4
FE: 75.0004.1000.0000
BE: 3.89a
Steps:
1.Register member from Mini program member center.
2.Go to POS member section, Click QR code Scanning or input registered mobile number to search.  Member details can be displayed but without member card assigned.
3.Click Confirm button, there will be the bellow error:[Record111.mp4](https://jira.tapestry.support/secure/attachment/921563/921563_Record111.mp4)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (6 則)
**Tovi Wang** (2025-03-07):
@@Anson Cheung @@Bobby
**Tovi Wang** (2025-03-07):
@@Anson Cheung
**Anson Cheung** (2025-03-07):
@@Tovi Wang
The issue is caused by fail to generate vip no., a fix is needed.
**Anson Cheung** (2025-03-07):
Release V1.7.5
[\\ds411\public\samuel\beapi\v1.7.5_20250307](file://ds411/public/samuel/beapi/v1.7.5_20250307)
-
**Tovi Wang** (2025-03-10):
@@Joseph_Hu @@Sherman tse Please help to arrange testing.Thanks!
CC @@Bobby @@Jason Wu @@Cy Lau
**Sherman tse** (2025-05-02):
Issue has fixed & tested
close case

## 相關資訊

- Jira: [FE-1643](https://ctil.atlassian.net/browse/FE-1643)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

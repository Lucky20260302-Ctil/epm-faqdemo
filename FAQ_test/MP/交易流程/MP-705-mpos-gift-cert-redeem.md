---
tags: [faq, MP, bug]
component: "MPOS"
symptom: "MPOS v3.28.3 cannot redeem gift certificates in Tapestry stores (MY region, OC602)"
root-cause: "Gift certificate redemption logic issue in MPOS API v3.28.3 — the API validation was rejecting valid gift cert redemption requests."
solution: "Fixed in MPOS v3.28.4 (released 2024-07-15). Also included in v3.29.1."
jira: MP-705
resolved: 2024-08-30
fix-version: "v3.28.4, v3.29.1"
---

# MP-705: MPOS v3.28.3 Unable to Redeem Gift Certificate (Tapestry MY)

## 問題

MPOS v3.28.3 cannot redeem gift certificates in Tapestry stores (MY region, OC602)

## 根因

Gift certificate redemption logic issue in MPOS API v3.28.3 — the API validation was rejecting valid gift cert redemption requests.

## 解法

Fixed in MPOS v3.28.4 (released 2024-07-15). Also included in v3.29.1.

## 相關資訊

- Jira: [MP-705](https://ctil.atlassian.net/browse/MP-705)
- Fix Version: v3.28.4, v3.29.1
- 解決日期: 2024-08-30

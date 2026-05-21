---
tags: [faq, FE, bug, production]
component: "Day End"
symptom: "After upgrading to V75, dayend info fails to upload for 10+ stores per day. Dayend data only uploads next day when cs2kconnect auto-runs on boot."
root-cause: "In V72, dayend forced a cs2kconnect execution to upload data immediately. In V75 this forced execution was removed. If store PC shuts down before cs2kconnect's scheduled run (10+ minutes after dayend), the upload never happens."
solution: "Workaround: keep store PCs running for 10+ minutes after dayend to allow cs2kconnect to complete. If missed, data auto-posts on next startup. Permanent fix: restore forced cs2kconnect during dayend."
jira: FE-1646
resolved: 2025-05-06
fix-version: "v750.04R11"
---

# FE-1646: V75 Day End cs2kconnect Schedule Not Triggered After Day End (10+ stores/day affected)

## 問題

After upgrading to V75, dayend info fails to upload for 10+ stores per day. Dayend data only uploads next day when cs2kconnect auto-runs on boot.

## 根因

In V72, dayend forced a cs2kconnect execution to upload data immediately. In V75 this forced execution was removed. If store PC shuts down before cs2kconnect's scheduled run (10+ minutes after dayend), the upload never happens.

## 解法

Workaround: keep store PCs running for 10+ minutes after dayend to allow cs2kconnect to complete. If missed, data auto-posts on next startup. Permanent fix: restore forced cs2kconnect during dayend.

## 相關資訊

- Jira: [FE-1646](https://ctil.atlassian.net/browse/FE-1646)
- Fix Version: v750.04R11
- 解決日期: 2025-05-06

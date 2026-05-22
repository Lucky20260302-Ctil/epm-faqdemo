---
project: MP
issue_key: MP-797
issue_type: Bug PRD
status: Release
tags:
- 01_install_deploy
- faq
- install_deploy
- mp
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-797
created: '2025-08-29'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'MP-797: [MPOS-118]CJ mPOS Prod_ J801 Saved transaction retains old cashier ID after upgrade'
---
# MP-797: [MPOS-118]CJ mPOS Prod_ J801 Saved transaction retains old cashier ID after upgrade

## 問題描述

After upgraded the version, retrieve the temporary saving transaction from POS. The Casher ID remained as the associate who saved the transaction so Casher at the POS need to input again.

Reproduce steps(v75.004.1305.0001)

1. MPOS login cashier is YZHANG.

2. CS2K login cashier is QHUANG.

3. Create transaction via MPOS then send to CS2K.

4. Retreive order from CS2K, the cashier will auto change to YZHANG.



## 相關資訊

- **Jira:** [MP-797](https://ctil.atlassian.net/browse/MP-797)
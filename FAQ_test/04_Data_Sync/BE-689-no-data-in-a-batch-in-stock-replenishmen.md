---
project: BE
issue_key: BE-689
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- backend-(web)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-689
created: '2022-11-09'
resolved: '2023-02-21'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-689: No data in a batch in Stock Replenishment Batch but sill able to execute Batch Validate'
---
# BE-689: No data in a batch in Stock Replenishment Batch but sill able to execute Batch Validate

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Stock Replenishment Batch Control Information (IC5000)

Reproduce steps:

1. To Stock Replenishment Batch Control Information

2. Create a batch (no need to insert data into the batch)

3. Click Batch Validation

Existing resu;t:

Pop up: Are you sure to proceed to Store Request Validation (IC5002)?, if Click OK, it will try to process the Validation (Ref: ChainStorePlus _ 99.mp4)

Expected resulr:

Should pop up: "No records within range" directly

 

Remark:

IC1002 also has the issue




## Jira Comments

> **Thomas** (2023-02-21):
> It is normal, same as other Batch Process (such as Physical In/Out Batch Control (IC6000), please check

## 相關資訊

- **Jira:** [BE-689](https://ctil.atlassian.net/browse/BE-689)
- **解決方式:** Done
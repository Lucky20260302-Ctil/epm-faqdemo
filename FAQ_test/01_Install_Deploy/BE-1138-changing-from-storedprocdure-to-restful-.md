---
project: BE
title: "BE-1138: Changing from StoredProcdure to Restful API calling for OSSRGM"
issue_key: BE-1138
issue_type: SOW
status: Closed
faq_score: 6.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, be, install_deploy, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1138"
created: 2025-06-19
resolved: 2025-09-23
resolution: Done
has_images: False
---

# BE-1138: Changing from StoredProcdure to Restful API calling for OSSRGM

## 問題描述

Since the server upgrade by HKMS2.0

the database of OSSRGM and ChainStorePlus would be seperated.

The current storedProcedure would not be able to be resused.

DataInterface program shall be used for fetching data, asking HKMS2.0 API to delete data , posting for insertion and resume mechanisms also need to be considerated(Maybe seq number)



## 相關資訊

- **Jira:** [BE-1138](https://ctil.atlassian.net/browse/BE-1138)
- **解決方式:** Done
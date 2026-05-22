---
project: FE
issue_key: FE-1125
issue_type: Change Request
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- printing
- sales
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1125
created: '2022-06-24'
resolved: '2024-05-04'
fix_version: ''
components: []
has_images: true
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1125: Add Registration Number on sales receipt for SG region'
---
# FE-1125: Add Registration Number on sales receipt for SG region

## 問題描述

**<u>Case Details</u>**
Coach MY & SG requests to shows following information on sales receipt;

1. Company name (Bottom)

2. Registration No. (Bottom)

3. Address (Top)

4. Telephone number (Top)

For existing MY sales receipt, it did display all of information above. 

Now, Coach requests to add Registration no for SG region.

Besides, the Company name & Registration No. are not showing up clearly on MY sales receipt. 
Coach is wondering if the margin of these information could be adjusted.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9af4999b-5fd1-43b8-8c27-c134128f723a)（需 Jira 登入）
**<u>Request</u>**

1. Add Registration number (201017653Z) for SY sales receipt

2. Adjust sales receipt margin in order to show Company name & Registration No. more clearly

**<u>Reference</u>**

- Registration no. display is decided by following configuration
 TBLCONFIG.COMPANYCODE = CoachMY

- Corresponding Registration No.
||Region||Company Name ||Registration No.||
|Coach MY|Coach Malaysia Sdn Bhd|201101009049 (937188T)|
|Coach SG|Coach Singapore Pte Ltd|201017653Z|



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9af4999b-5fd1-43b8-8c27-c134128f723a)

## 相關資訊

- **Jira:** [FE-1125](https://ctil.atlassian.net/browse/FE-1125)
- **解決方式:** Done
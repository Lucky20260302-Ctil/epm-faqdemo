---
project: FE
issue_key: FE-1770
issue_type: Task
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- receipt-printing
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1770
created: '2025-10-17'
resolved: '2026-02-11'
fix_version: ''
components: []
has_images: true
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1770: ANZ TMU Receipt printing(Tax Exemption & Footer'
---
# FE-1770: ANZ TMU Receipt printing(Tax Exemption & Footer

## 問題描述

ANZ (Australia and New Zealand) will adopt the SG (Singapore) printing layout. However, during testing of the SG layout with tax exemption applied, it was observed that **tax details such as tax amount and percentage are not displayed** in the printed output.

Given that:

- **AU** has a **10% GST**

- **NZ** has a **15% GST**

Both regions will be set to **tax-exempt** status. However, for transparency and audit purposes, the printed documents should still **display the tax exemption details**, including:

- Tax percentage

- Tax amount (even if zero)

- A note indicating exemption status

**Expected Outcome:**

- ANZ printing layout matches SG format.

- Tax exemption is applied for AU and NZ.

- Printed documents **include tax details** (percentage and amount) even when exempted.

**Acceptance Criteria:**

- Tax percentage and amount are shown on printed documents for ANZ, even when exempt.

- A clear indication of tax exemption is present.

- Layout remains consistent with SG format.

> 📎 **image-20251017-014806.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/929f7b9c-08e0-45a3-8bd0-569702a8b628)（需 Jira 登入）

> 📎 **image-20251017-014919.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2bf9c1ef-eaf4-42b3-a5cc-ebbf55dad48a)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251017-014806.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/929f7b9c-08e0-45a3-8bd0-569702a8b628)
2. 📎 **image-20251017-014919.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2bf9c1ef-eaf4-42b3-a5cc-ebbf55dad48a)

## 相關資訊

- **Jira:** [FE-1770](https://ctil.atlassian.net/browse/FE-1770)
- **解決方式:** Done
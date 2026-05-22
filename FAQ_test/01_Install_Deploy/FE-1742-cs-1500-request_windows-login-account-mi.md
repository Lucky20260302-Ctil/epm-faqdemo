---
project: FE
issue_key: FE-1742
issue_type: Task
status: Selected for Development (migrated)
faq_score: 5.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, install_package]
jira_url: "https://ctil.atlassian.net/browse/FE-1742"
created: 2025-08-05
resolved: 
resolution: 
has_images: False
---

# FE-1742: [CS-1500] Request_windows login account migration[Intune Deployment]

> **類型:** Task | **狀態:** Selected for Development (migrated)
> **分類:** 安裝與部署 | **FAQ 分數:** 5.5
> **負責人:** Cy Lau
> **組件:** Install_Package

## 問題描述

From [Keiji Ikehara](https://jira.tapestry.support/secure/ViewProfile.jspa?name=kikehara%40tapestry.com) : 
"#1. After Intune deployment, will be terminated SCCM soon.   before terminate, need to set up "MSI" installer  <<  Sanyo team task"

| Week | Spirit | Task | Description | 
| 16Jul - 29Jul | R22 | Analysis and Design | Complete project audit
Design new MSI architecture
Create test environment | 
| 30Jul-12Aug | R23 | Core Migration | Basic MSI project
Migrate files, registry, and basic components
Implement Prerequisites installation
(Drivers, Frameworks, Runtimes etc)
InstallScript -> MSI .net core Codes | 
| 13Aug-2Sept | R24 | Advanced Features | Develop custom actions for MSMQ,SQLEXPRESS and scheduled tasks
Create and test transforms
Implement upgrade scenarios | 
| 3Sept-16Sept | R25 | Testing and Validation | End-to-end testing on target environments
Intune deployment validation
Performance and rollback testing | 



## 相關資訊

- **Jira:** [FE-1742](https://ctil.atlassian.net/browse/FE-1742)
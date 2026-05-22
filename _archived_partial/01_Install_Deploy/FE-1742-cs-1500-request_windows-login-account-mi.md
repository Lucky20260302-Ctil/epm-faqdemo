---
project: FE
issue_key: FE-1742
issue_type: Task
status: Selected for Development (migrated)
tags:
- 01_install_deploy
- faq
- fe
- install_deploy
- install_package
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1742
created: '2025-08-05'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1742: [CS-1500] Request_windows login account migration[Intune Deployment]'
---
# FE-1742: [CS-1500] Request_windows login account migration[Intune Deployment]

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
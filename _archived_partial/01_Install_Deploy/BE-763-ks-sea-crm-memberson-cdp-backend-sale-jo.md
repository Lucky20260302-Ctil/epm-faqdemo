---
project: BE
issue_key: BE-763
issue_type: SOW
status: Closed
tags:
- 01_install_deploy
- backend-(chainstoreplus-7.0)
- be
- faq
- install_deploy
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-763
created: '2023-06-15'
resolved: '2023-07-27'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'BE-763: KS SEA CRM Memberson CDP backend Sale journal daily scheduled task'
---
# BE-763: KS SEA CRM Memberson CDP backend Sale journal daily scheduled task

## 問題描述

**Daily Batch Sales Transaction Interface**

In addition to register transaction to CDP via API, POS also needs to send the additional sales transaction information to CDP by daily batch interface file. Please refer to ‘*Appendix A.* **Daily Batch Sales Transaction Interface File Format’** section for the detail.

1. ChainStorePlus will develop an interface program to generate the interface file with delta sales transaction and send the file to CDP via SFTP.

2. The FTP server name, user ID and password will be provided by CDP later. We can set this information in the config file.

3. After the interface file successfully send to CDP, the interface file will be moved to the backup folder for audit trail.

4. The interface program will purge the interface files which are older than 60 days in backup folder. The number of days is configurable by the ‘housekeeping_days’ setting in the config file.

5. Setup a scheduled task in Tidal to execute the interface program once a day. Execute more than one time a day is allowed.

 

Please refer to BE-762 attached documents.

 



## 相關資訊

- **Jira:** [BE-763](https://ctil.atlassian.net/browse/BE-763)
- **解決方式:** Done
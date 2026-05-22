---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Set the config in DBviewer, then perform the Day End process, yet no shutdown message prompt."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-998
resolved: 2022-08-01
fix-version: ""
---

# FE-998: POS AutoShutdown exe not functioning

## 問題

Set the config in DBviewer, then perform the Day End process, yet no shutdown message prompt.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-08-01
### Jira Comments (1 則)
**Sang** (2021-07-22):
209. DotNet Dayend tblconfig.Shutdown - Support PosShutdown - Wait csplus exit and pcdmtn.* uploaded then shutdown PC (KTS 210719 v750.01R01A Jira [🔗](https://ctil.atlassian.net/browse/FE-998#icft=FE-998))209. DotNet Dayend tblconfig.Shutdown - Support PosShutdown - Wait csplus exit and pcdmtn.* uploaded then shutdown PC (KTS 210719 v750.01R01A Jira [🔗](https://ctil.atlassian.net/browse/FE-998#icft=FE-998))
a. New PosShutDown.exe _ Add para wait ## min (Ex: PosShutdown.exe 20)
b. Wait for wait for SSE Backup Completion (tblconfig.DISABLEBACKUPDBMASSSE='N')

## 相關資訊

- Jira: [FE-998](https://ctil.atlassian.net/browse/FE-998)
- Fix Version: 未記錄
- 解決日期: 2022-08-01

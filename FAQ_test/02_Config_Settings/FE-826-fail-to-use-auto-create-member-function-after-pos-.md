---
project: FE
issue_key: FE-826
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-826
created: '2020-11-06'
resolved: '2020-11-06'
fix_version: V720.02R03Q5
components:
- Frontend
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-826: Fail to use auto create member function after POS restart

## 症狀

POS重新啟動後，自動建立會員功能失效。重啟前已設定為啟用的「MEMBERNOTFOUNDAUTOCREATE」與「SHOWFORMATVIPNO」兩個設定參數，在POS重啟後被自動重置為預設值N（停用），導致無法在找不到會員時自動建立新會員。

## 根因

當POS啟動時若存在zlog檔案（位於Retdata6資料夾），系統在處理zlog的過程中會不正確地將MEMBERNOTFOUNDAUTOCREATE與SHOWFORMATVIPNO兩個設定參數重置為預設值N。此為POS啟動流程中zlog處理邏輯的缺陷，導致部分tblconfig設定被意外覆寫。

## 解法

將POS升級至V720.02R03Q5或更新版本，該版本已修正zlog處理時不當重置設定的問題。升級後，POS重啟時即使存在zlog檔案，MEMBERNOTFOUNDAUTOCREATE與SHOWFORMATVIPNO設定也不會被重置為預設值。

## 相關資訊

- Jira: [FE-826](https://ctil.atlassian.net/browse/FE-826)
- Fix Version: V720.02R03Q5
- 解決日期: 2020-11-06
- 組件: Frontend
- 負責人: Joy Li

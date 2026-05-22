---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Callout from coolbe on CS2K QA env."
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: BE-1067
resolved: 
fix-version: ""
---

# BE-1067: CS-1423 Callout from coolbe on CS2K QA env.

## 問題

Callout from coolbe on CS2K QA env.
**Request url**
[https://cjlineqa.coach.com/API_Gateway/api/v1/beapi/member/createMember](https://cjlineqa.coach.com/API_Gateway/api/v1/beapi/member/createMember)
**Time**
2025-05-21 18:00:25
**Request**
{"last_name":"Skr","first_name":"8.0","moblic_phone":"08012345678","kana_first_name":"","kana_last_name":"","sex":"C","no_DM":"Y","no_EDM":"Y","no_PHONE":"Y"}
**Repsonse**
{"line_uuid":"U657651c34342377b5cc95079ee178c97","exception":{"successful":false,"data":{"errorType":"Exception","errorCode":9999,"errorMessage":"Unexpected end when reading JSON. Path '', line 1, position 2.","errorDetails":" at Newtonsoft.Json.JsonTextReader.MatchValue(Boolean enoughChars, String value)\r\n at Newtonsoft.Json.JsonTextReader.MatchValue(String value)\r\n at Newtonsoft.Json.JsonTextReader.MatchValueWithTrailingSeparator(String value)\r\n at Newtonsoft.Json.JsonTextReader.ParseUndefined()\r\n at Newtonsoft.Json.JsonTextReader.ParseValue()\r\n at Newtonsoft.Json.JsonReader.ReadForType(JsonContract contract, Boolean hasConverter)\r\n at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.Deserialize(JsonReader reader, Type objectType, Boolean checkAdditionalContent)\r\n at Newtonsoft.Json.JsonSerializer.DeserializeInternal(JsonReader reader, Type objectType)\r\n at Newtonsoft.Json.JsonSerializer.Deserialize(JsonReader reader, Type objectType)\r\n at Newtonsoft.Json.Json
we are in a critical testing phase, please help investigate.
FYI, coolbe said 5/13 it was OK.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Tovi Wang** (2025-05-22):
@@Anson Cheung Please help to check this one.Thanks!
Log path :
\\172.16.183.201\localuser\support\20250521\CJLine-QA-20250521.zip
CC @@Joy Li
**Anson Cheung** (2025-05-22):
@@Tovi Wang Can you get the API_Gateway log, API_Gateway appsettings.json and BEAPI appsettings.json? Thanks
**Tovi Wang** (2025-05-22):
@@Anson Cheungexternal server log here.Please check.
CC @@Joy Li
**Anson Cheung** (2025-05-22):
@@Tovi Wang The error on 21/5 is caused by the API_Gateway appsettings.json is not set correctly. Seems this issue is fixed, this error has not occurred on 22/5. 
There is another error occurred in 22/5, please help to get 22/5 BEAPI sqlite log for further checking
**Tovi Wang** (2025-05-22):
@@Anson Cheung William说05-22（今天）拿Token的时候就有error.还没到create member这一步。
copying BEAPI log.
**Tovi Wang** (2025-05-22):
@@Anson Cheung22/5 BEAPI sqlite log for your further checking.
**Anson Cheung** (2025-05-22):
@@Tovi Wang 我在今天的API_Gateway log 看到拿token都是return 200 success
**Anson Cheung** (2025-05-22):
@@Tovi Wang beapi is not using the correct version, please update to BEAPI V2.2.4(build 641ef496)
**Tovi Wang** (2025-05-22):
@@Joy Li @@Ken Wang As Anson’s said.Please help to provide the BEAPI V2.2.4(build 641ef496) to Coach team.Thanks!
**Andrew_Au** (2025-10-08):
@@Tovi Wang  Please update the status
**Tovi Wang** (2025-10-09):
fixed,Please closed.

## 相關資訊

- Jira: [BE-1067](https://ctil.atlassian.net/browse/BE-1067)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
project: BE
title: "BE-1067: CS-1423 Callout from coolbe on CS2K QA env."
issue_key: BE-1067
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1067"
created: 2025-05-22
resolved: 
resolution: 
has_images: True
---

# BE-1067: CS-1423 Callout from coolbe on CS2K QA env.

## 問題描述

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

> 📎 **image-20250522-013726.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/356d7c44-0e51-41ed-88ce-bdc4da175738)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250522-013726.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/356d7c44-0e51-41ed-88ce-bdc4da175738)

## 相關資訊

- **Jira:** [BE-1067](https://ctil.atlassian.net/browse/BE-1067)
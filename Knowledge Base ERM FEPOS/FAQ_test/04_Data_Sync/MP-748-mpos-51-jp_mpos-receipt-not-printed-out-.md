---
project: MP
issue_key: MP-748
issue_type: Improvement
status: Closed
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-748"
created: 2025-02-26
resolved: 2025-05-02
resolution: Done
has_images: True
---

# MP-748: [MPOS-51] JP_mPOS Receipt Not Printed Out (Cloud IIS) -PrintHub Enhancement

> **類型:** Improvement | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.5
> **解決日期:** 2025-05-02
> **負責人:** Sherman tse
> **組件:** MPOS, MPOS API

## 問題描述


> 📎 **image-20250225-172030.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9dd9bc33-cccf-4761-8564-913dee76b563)（需 Jira 登入）

MPOS:

> 📎 **image-20250225-172052.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e22f0053-d09c-4d5e-b650-26174353ac3d)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250225-172030.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9dd9bc33-cccf-4761-8564-913dee76b563)
2. 📎 **image-20250225-172052.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e22f0053-d09c-4d5e-b650-26174353ac3d)


## Jira Comments

> **Cy Lau** (2025-02-26):
> svn://sanyosvn.ctil.com/svn/SvnPepository/branches/mPOS WebAPI/3.30.X

> **Cy Lau** (2025-02-26):
> isolation : GetPrintingAsync -  Reuse / new api : UpdatePrintJob Removal: CheckPrintHubConnection

> **Daniel Leung** (2025-03-04):
> 

> **Cy Lau** (2025-03-05):
>    public class NotificationMessage  {      [JsonProperty("action")]      public string Action { get; set; }      [JsonProperty("shoploc")]      public string ShopLoc { get; set; }      [JsonProperty("jobId")]      public string JobId { get; set; }      [JsonProperty("remarks")]      public string Remarks { get; set; }      [JsonProperty("payload")]      public string Payload { get; set; }  }

> **Cy Lau** (2025-03-07):
> Release - CloudPrintHubNotification  version 1.0.1 Location :  \\ds411\share\POS_MPOS_Release\CloudPrintHubNotification\20250307_1.0.0.1 Source - Git: http://172.16.138.42:3000/yeung/CloudPrintHubNotification.git CloudPrintHubNotification.exe.config: <appSettings>     <!-- Secret key for API authentication -->     <add key="SecretKey" value="Must Be aligned with MPOS_API Web.config" />     <add key="PrintHubId" value="API-Server" />  <!-- Assign Port for the self web host, aligned with MPOS_API Web.config -->         <add key="Port" value="9001" /> <!-- Timeout for a message sending to the hub -->         <add key="Timeout" value="3000" />     <add key="ByPassSSL" value="Y" />       <add key="IsUseHttps" value="N" /> <!-- Y for mini to auto system tray  -->       <add key="AutoMini" value=

> **Cy Lau** (2025-03-10):
> Updates : 1.0.0.2 \\ds411\share\POS_MPOS_Release\CloudPrintHubNotification\20250310_1.0.0.2 1) Bug fixing for if the worker is overnight running. The log for database file will be updated according to system date.

> **Daniel Leung** (2025-03-10):
>   MPOS API : \\ds411\share\POS_MPOS_Release\3.30.x\3.30.1-20250310.1 IPA : 3.30.1 -   

> **Sherman tse** (2025-03-10):
> For Mpos api, need to 2 new configs into web.config <add key="CloudPrintHubNotiWorkerPath" value="<http://172.16.138.247:9001/api/notification>"/>
> <add key="CloudPrintHubNotiWorkerSecretKey" value="YourSecretKeyHere"/>
>   <!--<add key="LicConfigDB" value="dbCoachLocal.db" />-->

> **Cy Lau** (2025-03-10):
>   Please generate a secretkey for them, just random A-z, 0-9 also remind the port   ,    once again many thanks for the tight timeline of this spirit

> **Cy Lau** (2025-03-10):
> Updates - 1.0.0.3 Owing to not able to distinguish between instance, mutex adding a suffix as region in config:  <add key="Region" value="18" /> \\ds411\share\POS_MPOS_Release\CloudPrintHubNotification\20250310_1.0.0.3

> **Bobby** (2025-03-12):
> Do we have any installation documents for the CloudPrintHubNotification?

> **Cy Lau** (2025-03-12):
> Updates - 1.0.0.4  Additional config :  \\ds411\share\POS_MPOS_Release\CloudPrintHubNotification\20250312_1.0.0.4

> **Sherman tse** (2025-03-12):
> Verified on QA test case attached

## 相關資訊

- **Jira:** [MP-748](https://ctil.atlassian.net/browse/MP-748)
- **解決方式:** Done
---
project: BE
issue_key: BE-1007
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- be
- error_exception
- faq
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1007
created: '2025-02-19'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
# BE-1007: SG QA Mpos打开sales 界面的时候出现报错fail to connect saleshub

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 8.5
> **負責人:** Daniel Leung
> **組件:** MPOS

## 問題描述

[1.SG](http://1.SG) QA Mpos打开sales 界面的时候出现报错fail to connect saleshub,请问可以帮忙看看是什么问题嘛。

SG QA PC是10.33.248.7

> 📎 **Image20250219215057.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b093b2db-0029-4403-93cf-ab011f4e881c)（需 Jira 登入）
2.web server是10.250.11.217

> 📎 **Image20250219215009.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4713df76-f980-4cfb-a586-5e0cf11a7f2d)（需 Jira 登入）
3.Till0 sales hub有error:

SalesHub Type: LocalOnly

Host URL: 10.33.248.7:9001/SalesHub

> 📎 **image-20250219-135253.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8b517f58-9d8c-4108-ae55-304aca26fee5)（需 Jira 登入）
Error detais:

14:45:29 : ServiceUnitIntraCommService Starts :19/02/2025 14:45:29
14:45:30 : ServiceUnitIntraCommService LocCode: OCQ92
14:45:30 : ServiceUnitIntraCommService RegionCode: 12
14:45:30 : SalesHub Mode: LOCALONLY
14:45:30 : SalesHub MPOSTillPrefix: M
14:45:30 : DayEnd is in process: False
14:45:31 : SalesHub host: 10.33.248.7:9001/SalesHub
14:45:32 : Ex: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.Net.HttpListenerException: Access is denied
   at System.Net.HttpListener.AddAllPrefixes()
   at System.Net.HttpListener.Start()
   at Microsoft.Owin.Host.HttpListener.OwinHttpListener.Start(HttpListener listener, Func`2 appFunc, IList`1 addresses, IDictionary`2 capabilities, Func`2 loggerFactory)
   at Microsoft.Owin.Host.HttpListener.OwinServerFactory.Create(Func`2 app, IDictionary`2 properties)
   --- End of inner exception stack trace ---
   at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)
   at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)
   at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)
   at Microsoft.Owin.Hosting.ServerFactory.ServerFactoryAdapter.Create(IAppBuilder builder)
   at Microsoft.Owin.Hosting.Engine.HostingEngine.StartServer(StartContext context)
   at Microsoft.Owin.Hosting.Engine.HostingEngine.Start(StartContext context)
   at Microsoft.Owin.Hosting.Starter.DirectHostingStarter.Start(StartOptions options)
   at Microsoft.Owin.Hosting.Starter.HostingStarter.Start(StartOptions options)
   at Microsoft.Owin.Hosting.WebApp.StartImplementation(IServiceProvider services, StartOptions options)
   at Microsoft.Owin.Hosting.WebApp.Start(StartOptions options)
   at Microsoft.Owin.Hosting.WebApp.Start[TStartup](StartOptions options)
   at Microsoft.Owin.Hosting.WebApp.Start[TStartup](String url)
   at SalesHubIntraCommServiceWPF.MainWindow.<DoLoad>d__19.MoveNext()



## 附件截圖

1. 📎 **Image20250219215057.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b093b2db-0029-4403-93cf-ab011f4e881c)
2. 📎 **Image20250219215009.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4713df76-f980-4cfb-a586-5e0cf11a7f2d)
3. 📎 **image-20250219-135253.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8b517f58-9d8c-4108-ae55-304aca26fee5)

## 相關資訊

- **Jira:** [BE-1007](https://ctil.atlassian.net/browse/BE-1007)
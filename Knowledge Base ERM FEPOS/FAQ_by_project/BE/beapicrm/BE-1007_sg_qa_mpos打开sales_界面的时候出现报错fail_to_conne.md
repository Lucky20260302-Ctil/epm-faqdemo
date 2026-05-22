---
tags: [faq, be, beapicrm]
component: "MPOS"
symptom: "[1.SG](http://1.SG) QA Mpos打开sales 界面的时候出现报错fail to connect saleshub,请问可以帮忙看看是什么问题嘛。"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: BE-1007
resolved: 
fix-version: ""
---

# BE-1007: SG QA Mpos打开sales 界面的时候出现报错fail to connect saleshub

## 問題

[1.SG](http://1.SG) QA Mpos打开sales 界面的时候出现报错fail to connect saleshub,请问可以帮忙看看是什么问题嘛。
SG QA PC是10.33.248.7
2.web server是10.250.11.217
3.Till0 sales hub有error:
SalesHub Type: LocalOnly
Host URL: 10.33.248.7:9001/SalesHub
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

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Tovi Wang** (2025-02-19):
@@Daniel Leung @@Bobby @@Cy LauAs talked in TMR teams meeting, I double checked the Xconfig setting and NOT found abnormal.Please help to double check and give some advice.Thanks!
**Andrew_Au** (2025-02-20):
@@Daniel Leung Please update the ticket status
**Cy Lau** (2025-02-20):
@@Tovi Wang  please help to inform them to check if the port 9001 has been granted on the machine
**Tovi Wang** (2025-02-20):
@@Cy Lau I has asked them granted the port 9001 to the machine and re-start MPOS,But error still.
**Cy Lau** (2025-02-20):
@@Tovi Wang
Please try to remote and rightclick the SalesHub.exe run as admin to see
**Tovi Wang** (2025-02-20):
sure
**Tovi Wang** (2025-02-20):
@@Cy Lau Follow capture for your reference.
**Tovi Wang** (2025-02-20):
@@Cy Lau @@Daniel Leung Neil re-installed the MPOS mannuallly,then Issue gone,We can ignore this issue first.Thanks!
**Cy Lau** (2025-02-21):
what about the sales hub error ?
**Tovi Wang** (2025-02-24):
Closed first.

## 相關資訊

- Jira: [BE-1007](https://ctil.atlassian.net/browse/BE-1007)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
project: BE
issue_key: BE-1060
issue_type: Bug PRD
status: Open
faq_score: 9.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1060"
created: 2025-04-28
resolved: 
resolution: 
has_images: True
---

# BE-1060: [CS-1416] Issue_CN_CRM API met 503 error on 26th

> **類型:** Bug PRD | **狀態:** Open
> **分類:** 錯誤與異常 | **FAQ 分數:** 9.5
> **負責人:** Cy Lau
> **組件:** API

## 問題描述

we had 2 times 503 error on 26th after around 17"00 HKT and each time it was persist around 180s.

Need your help on the root cause check.

1.

> 📎 **image-20250428-012823.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d5bb6e64-543e-4c86-80da-54e2d1b8db90)（需 Jira 登入）
2.APIGW-2025-04-26.log :

2025-04-26 16:53:09.5646 | bd07ac2b-accb-4768-bfc9-f516522837a7 |  |  | DEBUG | Ocelot.Errors.Middleware.ExceptionHandlerMiddleware | requestId: 80000f59-0000-d500-b63f-84710c7967bb, previousRequestId: no previous request id, message: ocelot pipeline finished
2025-04-26 c.5712 | bd07ac2b-accb-4768-bfc9-f516522837a7 |  |  | INFO | ApiGateway.Middleware.ClassReturnHandlerFePOS | Response body:  
2025-04-26 16:53:09.5712 |  | 2 | 2 | INFO | Microsoft.AspNetCore.Hosting.Diagnostics | Request finished HTTP/1.1 POST [https://cs2000aliweb.coach.com/BEGWCRM/api/v1/fepos/acxiom/member](https://cs2000aliweb.coach.com/BEGWCRM/api/v1/fepos/acxiom/member) application/json;+charset=utf-8 404 - 503 0 - 180240.4878ms 

> 📎 **image-20250428-013137.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c47e827f-6ab8-4b9f-99f3-57ea18db7c02)（需 Jira 登入）
3.u_ex.20250426.log

requestId: 80000f59-0000-d500-b63f-84710c7967bb, previousRequestId: no previous request id, message: Error Code: RequestTimedOutError Message: Timeout making http request, exception: Polly.Timeout.TimeoutRejectedException: The delegate executed asynchronously through TimeoutPolicy did not complete within the timeout.
       ---> System.Threading.Tasks.TaskCanceledException: A task was canceled.
         at Polly.Timeout.AsyncTimeoutEngine.ImplementationAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Func`2 timeoutProvider, TimeoutStrategy timeoutStrategy, Func`5 onTimeoutAsync, Boolean continueOnCapturedContext)          --- End of inner exception stack trace ---          at Polly.Timeout.AsyncTimeoutEngine.ImplementationAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Func`2 timeoutProvider, TimeoutStrategy timeoutStrategy, Func`5 onTimeoutAsync, Boolean continueOnCapturedContext)
         at Polly.AsyncPolicy.ExecuteAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext)          at Polly.Wrap.AsyncPolicyWrapEngine.<>c__DisplayClass3_0`1.<<ImplementationAsync>b__0>d.MoveNext()
      --- End of stack trace from previous location ---
         at Polly.CircuitBreaker.AsyncCircuitBreakerPolicy.<>c__DisplayClass8_0`1.<<ImplementationAsync>b__0>d.MoveNext()       --- End of stack trace from previous location ---          at Polly.CircuitBreaker.AsyncCircuitBreakerEngine.ImplementationAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext, ExceptionPredicates shouldHandleExceptionPredicates, ResultPredicates`1 shouldHandleResultPredicates, ICircuitController`1 breakerController)
         at Polly.CircuitBreaker.AsyncCircuitBreakerPolicy.ImplementationAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext)          at Polly.AsyncPolicy.ExecuteAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext)
         at Polly.Wrap.AsyncPolicyWrapEngine.ImplementationAsync[TResult](Func`3 func, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext, IAsyncPolicy outerPolicy, IAsyncPolicy innerPolicy)          at Polly.AsyncPolicy.ExecuteAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext)
         at Ocelot.Provider.Polly.PollyCircuitBreakingDelegatingHandler.SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
         at ApiGateway.Middleware.NoGzipDelegatingHandler.SendAsync(HttpRequestMessage request, CancellationToken cancellationToken) in D:\Project\Gateway\WebAPI\ApiGateway\Middleware\NoGzipDelegatingHandler.cs:line 20
         at System.Net.Http.HttpClient.<SendAsync>g__Core|83_0(HttpRequestMessage request, HttpCompletionOption completionOption, CancellationTokenSource cts, Boolean disposeCts, CancellationTokenSource pendingRequestsCts, CancellationToken originalCancellationToken)
         at Ocelot.Requester.HttpClientHttpRequester.GetResponse(HttpContext httpContext) errors found in ResponderMiddleware. Setting error response for request path:/ali/api/v1/fepos/acxiom/member, request method: POST
dbug: Ocelot.Errors.Middleware.ExceptionHandlerMiddleware[0]
      requestId: 80000f59-0000-d500-b63f-84710c7967bb, previousRequestId: no previous request id, message: ocelot pipeline finished
info: ApiGateway.Middleware.ClassReturnHandlerFePOS[0]
      Response body:
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished HTTP/1.1 POST [https://cs2000aliweb.coach.com/BEGWCRM/api/v1/fepos/acxi

## 附件截圖

1. 📎 **image-20250428-012823.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d5bb6e64-543e-4c86-80da-54e2d1b8db90)
2. 📎 **image-20250428-013137.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c47e827f-6ab8-4b9f-99f3-57ea18db7c02)
3. 📎 **image-20250428-013429.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2f79b398-cdfb-4311-9ae2-35a802d47f18)
4. 📎 **image-20250428-013742.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/357e0bc7-21c2-4df5-9049-1e9daeee3f88)

## 相關資訊

- **Jira:** [BE-1060](https://ctil.atlassian.net/browse/BE-1060)
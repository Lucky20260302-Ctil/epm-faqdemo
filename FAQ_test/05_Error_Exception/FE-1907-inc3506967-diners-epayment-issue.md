---
project: FE
issue_key: FE-1907
issue_type: Bug PRD
status: Open
tags:
- 05_error_exception
- error_exception
- faq
- fe
- payment
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1907
created: '2026-03-26'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1907: [INC3506967] Diner''s ePayment issue'
---
# FE-1907: [INC3506967] Diner's ePayment issue

## 問題描述

@@Sang Please help to take a look follow error.Thanks!

 

HK OCF1 till1  upgraded to win11.when staff press the payment button"E-Payment", card terminal A920 does not have response,refer to attached screenshot.

1.

> 📎 **image-20260326-080914.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/79c7bffc-57a3-406a-a012-e4109cbbb620)（需 Jira 登入）
2.

> 📎 **image-20260326-081116.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bddc3f5e-f9ed-40f2-9732-6753a172f905)（需 Jira 登入）
3.Checked T9 log found follow error:

[20260325 15:10:37 -1368]: Process_Payemnt_Type - Start : DC - E-Payme : Avail V.  Memory : 140731663.753
[20260325 15:10:37 -1378]: Process_Payemnt_Type - End : DC - E-Payme : Avail V.  Memory : 140731663.753
[20260325 15:10:41 -0343]: doCommit
[20260325 15:10:41 -0453]: PayWithECR_New2
[20260325 15:10:43 -2760]: [20260325 03:10:43]  : 
[20260325 15:10:43 -2760]: [20260325 03:10:43]  : Start init a pay request
[20260325 15:10:43 -2770]: [20260325 03:10:43]  : -------------------------
[20260325 15:11:05 -0838]: PayWithECR_EPay.Error: System.IO.IOException: 連結到系統的某個裝置失去作用。

 

   於 System.IO.Ports.InternalResources.WinIOError(Int32 errorCode, String str)
   於 System.IO.Ports.SerialStream.EndWrite(IAsyncResult asyncResult)
   於 System.IO.Ports.SerialStream.Write(Byte[] array, Int32 offset, Int32 count, Int32 timeout)
   於 System.IO.Ports.SerialPort.Write(String text)
   於 SanyoPOS.Pay.ECR.ECR_A920_SP.SendCommand(String pContent)
   於 SanyoPOS.Pay.ECR.ECR_A920_SP.PayWIthValidate(Decimal Amount, String EType, String InvNo)
   於 SanyoPOS.Pay.ECR.ECR_A920_SP.Pay(Decimal Amount, String EType, String InvNo)
   於 SanyoPOS.Pay.ECR.ECR_Base._Closure$__75-0._Lambda$__0()
   於 System.Threading.Tasks.Task`1.InnerInvoke()
   於 System.Threading.Tasks.Task.Execute()
--- 先前擲回例外狀況之位置中的堆疊追蹤結尾 ---
   於 System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   於 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   於 System.Runtime.CompilerServices.TaskAwaiter`1.GetResult()
   於 SanyoPOS.Pay.Module1.VB$StateMachine_0_TimeoutAfter`1.MoveNext()
--- 先前擲回例外狀況之位置中的堆疊追蹤結尾 ---
   於 System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   於 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   於 System.Runtime.CompilerServices.ConfiguredTaskAwaitable`1.ConfiguredTaskAwaiter.GetResult()
   於 SanyoPOS.Pay.ECR.ECR_Base.VB$StateMachine_75_Pay_Async.MoveNext()
[20260325 15:11:05 -4972]: Process_Payemnt_Type.Error: SanyoPos.Exceptions.Exception: 連結到系統的某個裝置失去作用。

 

   於 SanyoPos.Wpf.Service.PayWithECR_EPay(String CashierCode, clsPaymentInfo PayMethod, Decimal Amount, String InvoiceNo, Int32 InputSeq)
   於 SanyoPos.Wpf.Service._Lambda$__R626-10(String a0, clsPaymentInfo a1, Decimal a2, String a3, Int32 a4)
   於 SanyoPos.Wpf.Service.PayWithECR_New2(String CashierCode, clsPaymentInfo PayMethod, Decimal Amount, String InvoiceNo, Int32 InputSeq)
   於 SanyoPos.Wpf.Service.PayWithECR_New(String CashierCode, clsPaymentInfo PayMethod, Decimal Amount, String InvoiceNo, Int32 InputSeq)
   於 SanyoPos.Wpf.ViewModel.PaymentViewModel.Process_Payemnt_Type(clsPaymentInfo& Tender)
[20260325 15:11:08 -2762]: Refresh Vb6 Setting
[20260325 15:11:08 -3852]: Microsoft.VisualBasic.Devices.ComputerInfo
Operation System : Microsoft Windows 11 企業版 LTSC Win32NT

4.

1.物理连接正常，
device manager正常显示port口
2.COM口从7换到了3，致电用户测试，

①使用EPM-Epayment ，1950金额可以同步到刷卡机，刷卡机取消动作无法同步到CS2000FE
②DC-Epayme ，1950 金额无法同步到刷卡机且有如下error：“ELE.Payment:failure - storeid or termid was incorrect”

> 📎 **image-20260326-082958.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bc32ec24-0217-4753-bc46-c0b123bccfc7)（需 Jira 登入）

店铺提供了测试录屏：

> 📎 **OCF1tILL1.mp4** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/359f8966-1e44-4290-a591-9a33068cc0e0)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260326-080914.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/79c7bffc-57a3-406a-a012-e4109cbbb620)
2. 📎 **image-20260326-081116.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bddc3f5e-f9ed-40f2-9732-6753a172f905)
3. 📎 **image-20260326-082958.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bc32ec24-0217-4753-bc46-c0b123bccfc7)
4. 📎 **OCF1tILL1.mp4** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/359f8966-1e44-4290-a591-9a33068cc0e0)

## 相關資訊

- **Jira:** [FE-1907](https://ctil.atlassian.net/browse/FE-1907)
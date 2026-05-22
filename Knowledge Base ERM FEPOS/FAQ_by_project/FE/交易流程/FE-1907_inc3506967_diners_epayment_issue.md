---
tags: [faq, fe, 交易流程]
component: "Payment"
symptom: "@@Sang Please help to take a look follow error.Thanks!"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1907
resolved: 
fix-version: ""
---

# FE-1907: [INC3506967] Diner's ePayment issue

## 問題

@@Sang Please help to take a look follow error.Thanks!
HK OCF1 till1  upgraded to win11.when staff press the payment button"E-Payment", card terminal A920 does not have response,refer to attached screenshot.
1.
2.
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
店铺提供了测试录屏：

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2026-03-26):
@@Sang FE log here.Please help to further checking.
CC @@Joy Li
**Sang** (2026-03-26):
@@Tovi Wang @@Joy Li Seems CSPLUS fail to use Serial Port 7 (syscon_ECR_ComPort=7) to connect A920 terminal after upgrade to Win 11,  Please test COM port 7 is normal first
**Tovi Wang** (2026-03-26):
@@Sang
com口刚开始是7会报下面的error：
现在Com口从7换到了3之后,报下面这个error:
error：“ELE.Payment:failure - storeid or termid was incorrect”
**Sang** (2026-03-30):
@@Tovi Wang ①使用EPM-Epayment ，1950金额可以同步到刷卡机，刷卡机取消动作无法同步到CS2000FE
②DC-Epayme ，1950 金额无法同步到刷卡机且有如下error：“<span style="color:#ff5630">ELE.Payment:failure - storeid or termid was incorrect”</span>
PayMe Store ID and termid stored in tblconfig. A920PayMeStoreID and A920PayMeTermID,. These value should be matched with terminal setting.  Please check

## 相關資訊

- Jira: [FE-1907](https://ctil.atlassian.net/browse/FE-1907)
- Fix Version: 未記錄
- 解決日期: 未記錄

---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "We got callout from TW region v75 MPOS pilot store OC705, when they try  to add member through scann"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-782
resolved: 2025-07-09
fix-version: ""
---

# MP-782: [MPOS-102][INC3043100][INC3031690]TW MPOS - Cannot add member through scanning QR code from LINE app

## 問題

We got callout from TW region v75 MPOS pilot store OC705, when they try  to add member through scanning QR code from LINE app it will pop-up 'Invalid QR Code', this also able to reproduce in QA Env, kindly help to check.
**QA Testing info:**
IPA Version: v3.29.5-20250325.4
API Version: COACH_MPOSWebAPI_R3.29.5f
Testing machine: OCQ94(10.33.248.12) - connect to apawiqwposweb24, UI log already uploaded.
Testing VIP Line QR Code:
error message:
1.Dbtrans config
2.UI log error:URL:[https://10.250.11.217/sanyoservice.api.fe_14/api/v1/Members/QR?encryptValue=YVhaQWRYTmxaRFIwWVhCemRISjVQUT09M1VPQnhNT0FPS1R4Wi8rQ3d1Ym0zQjZxRHNYOEc0TGRVeGp2aXpZUXE1L1gzeDMvdG9UQmpoNjh1OEpJR0o0NmtTMVBpS29ob3NLdGttMDJlK296bmlNZnJwOUlXSmVtODNVSi9NSmR5aHpOdGVpWlpZVnVEOGYyVkRhQ01ZTGZFczhFUDNmeWE3TUdteGZpWVVlSjN6a21lTDhUazJDOWVia1JoVk0vMGMzZ2t3TFd3M2hBVm5xampMdjEvUXliU21LcEp4dEcrbHUyaGRHUDI5bDhUTENFUi9uM1A4dDkxRXJjcG56MnhSOD0=,](https://10.250.11.217/sanyoservice.api.fe_14/api/v1/Members/QR?encryptValue=YVhaQWRYTmxaRFIwWVhCemRISjVQUT09M1VPQnhNT0FPS1R4Wi8rQ3d1Ym0zQjZxRHNYOEc0TGRVeGp2aXpZUXE1L1gzeDMvdG9UQmpoNjh1OEpJR0o0NmtTMVBpS29ob3NLdGttMDJlK296bmlNZnJwOUlXSmVtODNVSi9NSmR5aHpOdGVpWlpZVnVEOGYyVkRhQ01ZTGZFczhFUDNmeWE3TUdteGZpWVVlSjN6a21lTDhUazJDOWVia1JoVk0vMGMzZ2t3TFd3M2hBVm5xampMdjEvUXliU21LcEp4dEcrbHUyaGRHUDI5bDhUTENFUi9uM1A4dDkxRXJjcG56MnhSOD0=,) timestamp: 20 June 2025 02:35:59 PM, timeInMillis: 1750401359032, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: API, methodName: responsehandling2, text: httpClient:985861166 API:StatusCode:500, timestamp: 20 June 2025 02:35:59 PM, timeInMillis: 1750401359801, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
{className: API, methodName: responsehandling2, text: httpClient:985861166 Error: [999] Invalid QR Code, timestamp: 20 June 2025 02:35:59 PM, timeInMillis: 1750401359802, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null}
{className: _SaleMemoIphoneState, methodName: _barcodeScanning, text: Error: [999] Invalid QR Code, timestamp: 20 June 2025 02:35:59 PM, timeInMillis: 1750401359802, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null}
{className: API, methodName: httpGetDataAsync, text: httpClient:705859089

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-09
### Jira Comments (6 則)
**Tovi Wang** (2025-06-20):
@@Cy Lau @@Daniel Leung QA store OCQ94 MPOS log & Till0 dbtrans here.Please help to further checking.Thanks!
CC @@Joy Li @@pierre.shi
**Tovi Wang** (2025-06-20):
@@Cy Lau T9 log here.Not found WA log.
**Tovi Wang** (2025-06-20):
@@pierre.shi 帮忙找一家TW生产环境 V72 的dbtrans.看下那2个config是什么值？截图并且把dbtrans file贴到这里。Thanks!
**Cy Lau** (2025-06-20):
RCA :
Since MPOS 3.29 support the dynamic token for Member QR Code,
as leaking of backward compactability , the MPOS API reject the QR Code as Invalid.
Difference between FEPOS and mPOS , FEPOS could determine the OnlineMemberType and Do the dynamic token validation via UI  while mPOS would depened on MPOS API
Bug fix:
3.29.5-20250620.1-b1
\\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20250620.1b1
Adding restriction towards the dynamic token validation only happens for OnlineMemberType == ACIXOM
@@Sherman tse  @@Joy Li  It is recommended to add test case on this one for all region may using QRCode member
**Joy Li** (2025-07-09):
The issue is fixed in MPOS API 3.29.6 and release on Jul 8.
@@Sherman tse  Please update the test case.
**Sherman tse** (2025-07-09):
Verified on QA
test case attached

## 相關資訊

- Jira: [MP-782](https://ctil.atlassian.net/browse/MP-782)
- Fix Version: 未記錄
- 解決日期: 2025-07-09

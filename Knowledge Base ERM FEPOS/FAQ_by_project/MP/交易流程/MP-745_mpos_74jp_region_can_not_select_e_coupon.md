---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "after deploy the patch COACH_MPOSWebAPI_R3.29.5d, we did testing for JP region, we found that in MPO"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-745
resolved: 2025-05-02
fix-version: ""
---

# MP-745: [MPOS-74]JP Region, can not select E-Coupon even the member we selected have available ecoupon

## 問題

after deploy the patch COACH_MPOSWebAPI_R3.29.5d, we did testing for JP region, we found that in MPOS, even the member we selected have available e-coupon, e-coupon will show as blank when we trying to select it. kindly help to check.
Testing info:
CS2K Testing machine ip: 172.24.253.20(J805)
IPA Version: 3.29.5-20250108.2
API: COACH_MPOSWebAPI_R3.29.5d ( connect to apawiqwposweb24)
Testing vip no#: J101WJ00051712/OCQ92WJ01356793

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (18 則)
**Cy Lau** (2025-02-11):
waiting @@Tovi Wang  and @@Jason Wu  for log
**Jason Wu** (2025-02-11):
@@Cy Lau logs copied and attached in ticket
**Cy Lau** (2025-02-12):
Select Ecoupon sql : 
Select top (100) vip.*, HasCoupon from vip  with (NoLock)  Left Join (select distinct ecoupon_vip_no, 'Y' as HasCoupon from ecoupon where ecoupon_date <= '2025/02/11' AND ecoupon_exp_date >= '2025/02/11' ) as VipEcpn  On vip.vip_no = VipEcpn.ecoupon_vip_no  left join vip_flag On vip.vip_no = vip_flag.vip_no  where  vip_flag.vip_active_flag='Y'  AND ( vip.vip_no='J101WJ00051712') AND (vip_status<>'C'  or vip_status is null) Order by HasCoupon Desc, vip.vip_no
**Cy Lau** (2025-02-12):
@@Tovi Wang  Please confirm that :
There’s empty for the result
**Cy Lau** (2025-02-12):
@@Daniel Leung
Please check why the API return 124 coupons but the screen is empty :
709033.txt
[https://ios.ctil.com/mpos/log/web3/](https://ios.ctil.com/mpos/log/web3/)
**Tovi Wang** (2025-02-12):
Please confirm that :There’s empty for the result
-->I found web server resource logs just is empty on 02-11.
**Cy Lau** (2025-02-12):
@@Tovi Wang  it wont make sense for the logs of API would be empty. Since the MPOS calling the API with also the response, so it shall have current logging. Would you mind checking another apawiqwposweb which it may connect to ?
The API did received the request for
**Tovi Wang** (2025-02-12):
@@Cy Lau OK,Noted.Let me double check web23 server if have the logs.wait sec please.
**Daniel Leung** (2025-02-12):
@@Tovi Wang Can you upload the screen recording?
**Tovi Wang** (2025-02-12):
@@Daniel Leung @@Cy Lau
I has re-copied the API log and the log have records now,Please double check.
**Daniel Leung** (2025-02-12):
@@Tovi Wang Do you have screen recording? Coupons can be displayed normally with the response in logs. I would like to have the video recording to see the actual behavior for further investigation
response in logs
Hardcode response
**Tovi Wang** (2025-02-12):
@@Daniel Leung  up video for your further checking.
**Cy Lau** (2025-02-13):
@@Daniel Leung  , Please update the status
**Daniel Leung** (2025-02-14):
fixed version has been uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)  - 3.29.5-20250212.1
**Cy Lau** (2025-02-16):
@@Daniel Leung  Please report the affected versions
Since which version having this issue
**Cy Lau** (2025-02-24):
@@Joseph_Hu  Please update if it could meet the schedule 25-feb
**Joseph_Hu** (2025-02-24):
@@Cy Lau Yes it could
**Sherman tse** (2025-02-24):
Verified on QA
test case attached

## 相關資訊

- Jira: [MP-745](https://ctil.atlassian.net/browse/MP-745)
- Fix Version: 未記錄
- 解決日期: 2025-05-02

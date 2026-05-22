---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "PRC region POSV75"
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: FE-1683
resolved: 
fix-version: ""
---

# FE-1683: [CS-1430][INC2933217]PRC region POSV75 扫描顾CDP礼券的核销码,显示"parse coupon QR code error"

## 問題

PRC region POSV75
升级之前，POSV72在支付页面点击会员电子优惠券之后可以扫描顾客手机上CDP礼券的核销码选中优惠券，但现在升级到V75以后，扫描核销码会显示"parse coupon QR code error"，无法通过扫描选中，只能手动选择优惠券。
检查日志，扫描核销码以后，生成的是一大串字符，并不是对应的coupon核销码，并且有error：parse coupon QR code error。
对应当天的日志已经上传。

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Sang** (2025-04-30):
@@pierre.shi  FE was not able to get CDP_QRCode_Key_1 value from db DB. Please check BE DB dbconfig table setting.
**pierre.shi** (2025-05-06):
Hi@@Sang 这个值每个公司都不一样的吗？还是说是一个固定值，如果是固定值的话，应该是多少的？
**Sang** (2025-05-07):
@@Sang This value should be provided by Coach.  Encrypted QR Code and Decrypted QR code Algorithm and key should be one set.
**Tovi Wang** (2025-05-08):
@@Sang @@Cy Lau Please further advice.
Dbconfig_long Value:
4LHXI4EdLATfbkKhh9HYqBa2v9JGMgo8UvBnWxpuYqvLYtFbouMYnRlbU85LOcgtfplEShSdafBkaJoHSEXvAUM1gIN3Lf8icOEfu1R2/bvz/gApXe1xFn6U73/AJD4TxTaC2pStWQ5AkgONbmxcoM1xj2MqgiamU+/z+bm7kpBQIoEYFGOuSoKESxXrDnwy/dcNtamNSrOLeair9frZNGh5QT+WSJggXWQhHx7KqbpwwnkTv7h6fYw2sM7szrZAjlYxypfuvZ7izonB2nfq7q3wKTZzS2hxuZWPJ4xLMpiatxbF4SMj48Gw5NXgdNup6pxYo1CipbIO397vmspchw==
CC @@pierre.shi @@Joy Li
**Tovi Wang** (2025-05-08):
@@Sang @@Cy Lau FE Dbtrans CDP_QRCode_Key_1 config value is blank.
**pierre.shi** (2025-05-09):
@@Tovi Wang  @@Sang  QA测试也无法扫描
**Tovi Wang** (2025-05-09):
@@Sang @@Cy Lau 我怀疑是QA 和Pro Xconfig CDP coupon QR code  Key value不知道从什么时候丢了。因为客户也很少用，然后也没人提过.这次是Pro有一个客户用了才发现了这个问题。
CC @@Bobby @@Joy Li @@pierre.shi
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi  Please update the ticket status
**Tovi Wang** (2025-08-29):
Can be closed.Not need any change first.

## 相關資訊

- Jira: [FE-1683](https://ctil.atlassian.net/browse/FE-1683)
- Fix Version: 未記錄
- 解決日期: 未記錄

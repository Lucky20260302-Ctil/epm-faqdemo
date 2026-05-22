---
tags: [faq, web, web服務]
component: "WEB Enquiry"
symptom: "1、POS Payment key button control"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: WEB-352
resolved: 2024-08-30
fix-version: ""
---

# WEB-352: POS Payment Key Button Control：Currency code input ’PAY‘，F1 input ’PAY‘  click  save，提示invalid Payment Code

## 問題

1、POS Payment key button control
2、create数据，currency code选择pay，F1选择Pay
3、点击save
实际现象如下图所示：

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-08-30
### Jira Comments (3 則)
**Andrew_Au** (2024-07-05):
Should select HKD base currency for this company payment.
**ryan** (2024-07-09):
[https://172.16.138.95/ChainStorePlus_LandsD_QA](https://172.16.138.95/ChainStorePlus_LandsD_QA)介个环境上，没有这个bug了
**Sherman tse** (2024-07-09):
@@ryan Seems no any payment methods under this “PAY“, so system not allow to save the creation & pop up the error
You may check relateionship between payment method & currency code in Payment Type Information (MF0009) [https://172.16.138.95/ChainStorePlus_LandsD_QA/mf0009](https://172.16.138.95/ChainStorePlus_LandsD_QA/mf0009)

## 相關資訊

- Jira: [WEB-352](https://ctil.atlassian.net/browse/WEB-352)
- Fix Version: 未記錄
- 解決日期: 2024-08-30

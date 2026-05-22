---
project: MP
title: "MP-523: ZebraPrinter ZQ310, ZQ320"
issue_key: MP-523
issue_type: Task
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-523"
created: 2022-05-05
resolved: 2024-07-10
resolution: Done
has_images: False
---

# MP-523: ZebraPrinter ZQ310, ZQ320

## 問題描述

### Investigations on zebrautility: ^0.0.38

It has been reported as following issues:

1. After integrating this plugin into your flutter project, you MUST add the `libZSDK_API.a` file into your xcode project, or you would not pass the iOS building.(BlackBox for the executable)

2. Characters in utf8 encoding can not be printed on iOS, you MUST modify the implementation code under iOS folder. And sadly, this would not be an easy job for non-native devs. (TBC)

3. ~~The channel apis were NOT implemented correctly on Android. So, when you call some apis on Android, your app may crash. And codes under ~~`onMethodCall`~~ function in ~~`Printer.java`~~ must be updated. This issue is mentioned in ~~~~[#8](https://github.com/MythiCode/zebra_utlity/issues/8)~~~~ .~~(Ignore first)

4. The result from `onPrinterFound` callback is NOT reliable. This plugin will return the previously discovered printers when you call `discoveryPrinters`. So you will notice that when you discovered a printer, it still appears in your found list when you rescan printers event you turn the printer's power off.(Fatal)

5. Printers may disconnect after several seconds on iOS. This might be a serious bug with the Zebra SDK. So, DO NOT use it on iOS.(Fatal)



## 相關資訊

- **Jira:** [MP-523](https://ctil.atlassian.net/browse/MP-523)
- **解決方式:** Done
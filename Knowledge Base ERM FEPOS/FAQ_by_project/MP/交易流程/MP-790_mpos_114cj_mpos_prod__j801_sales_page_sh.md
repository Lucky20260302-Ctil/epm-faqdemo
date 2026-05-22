---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Issue :White button displays on mPOS(Confirmed other pilot stores does not have this issue)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-790
resolved: 2025-08-20
fix-version: ""
---

# MP-790: 【MPOS-114】CJ MPOS Prod_ J801 Sales page show null ''button''

## 問題

Issue :White button displays on mPOS(Confirmed other pilot stores does not have this issue)
The issue occurs only at J801 after we updated the version(Ver 3.30.3) on 8/6 evening
J801 uploaded the log at 14:40pm on 8/10
Occurs with unspecified users.
The number of white buttons varies depending on the person.
Pressing the buttons does nothing.
The issue disappears after logging off and logging back in.
Reinstalling the app does not resolve the issue—it still occurs.
FE POS version ：75.004.1305.0001
MPOS IPA: 3.30.3(Local IIS)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-08-20
### Jira Comments (6 則)
**Tovi Wang** (2025-08-11):
@@Daniel Leung Please help to take a look this issue first.J801 MPOS all logs for your further checking.Thanks!
CC @@Joy Li @@Cy Lau
**Joy Li** (2025-08-14):
@@Cy Lau @@Daniel Leung  Please check my update below. Thanks.
@@Tovi Wang  Please check the command . let me know if any missing. Thanks.
<u>**Recap from Tapestry Meeting: **</u>
MPOS 3.30.3(20250703)
- 
- 
Then user see the null button in screen suddenly.
**Tovi Wang** (2025-08-14):
Let me add more info from SOG team:
Please kindly check store feedback.
Issue Report: Unresponsive White Button on mPOS Sales Screen
1.Occurrence Scenario
When accessing the "Sales" screen from the mPOS home page (by tapping the "Sales" button), a white button suddenly appears without any user interaction.
The button tends to appear after leaving the screen idle for a period during active use.
2.Impact on Operations
Other functions (e.g., SKU search, member registration, proceeding to payment, returning to home screen) remain operational.
The white button does not respond to touch, potentially blocking navigation.
Workaround: Force-closing the app (swiping it away from recent apps) removes the button, but the issue may recur upon reopening.
Note: While the button can also be dismissed via Safari, this is impractical during customer interactions.
Additional Concern: Frequent app restarts may accelerate battery drain.
3.Re-entering the Sales Screen
The issue persists until the app is fully terminated. Reopening the Sales screen without a restart triggers the same problem.
1. 
2.
**Daniel Leung** (2025-08-18):
New version uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/) 
3.29.6-20250818.1
3.30.3-20250818.2
@@Joy Li @@Sherman tse
**Sherman tse** (2025-08-19):
Verified on QA
Test case attached
**Joy Li** (2025-08-20):
released to TP on 2025-08-20 by joy

## 相關資訊

- Jira: [MP-790](https://ctil.atlassian.net/browse/MP-790)
- Fix Version: 未記錄
- 解決日期: 2025-08-20

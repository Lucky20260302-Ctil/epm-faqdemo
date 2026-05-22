---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Copy from ticket:"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1944
resolved: 
fix-version: ""
---

# FE-1944: [CS-2771][INC3564250] OC09 till 0 pos slow issue 

## 問題

Copy from ticket:
Symptom:
till 0 pos出單非常慢，需要30秒-1分鐘，之前是一按就會出單。
4/29號user給的時間是9pm左右，告知這個問題不是第一次發生。
五一黃金周就要來了，user要求儘快查看這個問題並解決。
till 0 pos version:V75
Troubleshooting:
1.restart pos, issue stills
Device information:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Joy Li** (2026-05-05):
T9
[20260429 19:06:34 -7874]: Save Memo End:S.OC09.00212541 : Avail V.  Memory : 140729702.433
[20260429 19:06:34 -7884]: Save Memo [00212541]: Success
[20260429 19:06:34 -7904]: PCD.Start
[20260429 19:06:34 -7924]: Write PCD STart:S.OC09.00212541 : Avail V.  Memory : 140729702.433
[20260429 19:06:36 -9418]: PCD.End
[20260429 19:06:36 -9428]: Write PCD End : Avail V.  Memory : 140729706.627
[20260429 19:06:36 -9438]: Drawer.Start
[20260429 19:06:36 -9488]: Open Drawer With C
[20260429 19:06:36 -9518]: CallDrawer.Start()
[20260429 19:06:36 -9974]: Drawer.End
<span style="color:#ff5630">[20260429 19:06:36 -9984]: Print.Start</span>
<span style="color:#ff5630">[20260429 19:06:37 -0004]: doPrint_Memo.Start</span>
<span style="color:#ff5630">[20260429 19:06:50 -0317]: After Print : Avail V.  Memory : 140729691.251</span>
<span style="color:#ff5630">[20260429 19:06:50 -0327]: Print.End</span>
[20260429 19:06:50 -0337]: DrawerClose.Start
**Joy Li** (2026-05-05):
After checking Till 0, we found that the memo issuance time (after survey input to memo printing) normally takes 12–22 seconds. However, we identified five extreme cases where the processing time exceeded 25 seconds, with the longest taking up to 103 seconds. We are currently tracing these cases.
Please note that the user reported that memo printing on April 29 took 30 seconds to 1 minute. However, based on our checks, the maximum memo processing time on April 29 was 22 seconds.
Summary of memo processing times:
2026‑04‑29 – 65 memos, Min: 12 sec / Max: 22 sec
2026‑04‑30 – 67 memos, Min: 12 sec / Max: 103 sec
2026‑05‑01 – 94 memos, Min: 12 sec / Max: 15 sec
2026‑05‑02 – 113 memos, Min: 12 sec / Max: 20 sec
Below is the sample for 2026-04-30
**Joy Li** (2026-05-05):
@@Joy Li
**Tovi Wang** (2026-05-14):
Hi @@Sang @@Joy Li May I know anything update for this issue?
**Tovi Wang** (2026-05-20):
@@Sang Please help to further checking this case and give me some update.Thanks!
**Sang** (2026-05-20):
@@Tovi Wang Please check the laser printer is network connection or direct connect to PC ?
**Tovi Wang** (2026-05-21):
@@Sang 和SOG team确认到，小票打印机型号是HP M211， 是USB直连打印机不是网络连接。因为Till0出单慢，所以现在店铺已经不用till0做销售了。顺便还确认到OC09 其它Till出小票要比till0明显快很多。

## 相關資訊

- Jira: [FE-1944](https://ctil.atlassian.net/browse/FE-1944)
- Fix Version: 未記錄
- 解決日期: 未記錄

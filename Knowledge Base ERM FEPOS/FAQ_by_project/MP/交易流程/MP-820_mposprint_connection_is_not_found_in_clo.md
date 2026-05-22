---
tags: [faq, mp, 交易流程]
component: "MPOSPrint.exe"
symptom: "“F-ShopPrinter Not On the list”"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: MP-820
resolved: 
fix-version: ""
---

# MP-820: MPOSPrint connection is not found in CloudHub

## 問題

“F-ShopPrinter Not On the list”
After support team investigation from the log,
HeartBeat is working up to
“Slow Connection”
Suspected that zombie connection

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Cy Lau** (2026-03-26):
SignalR classic uses (in order, negotiated):
1. 
2. 
3. 
Each has **its own keep‑alive behavior**, controlled by **SignalR**, not the raw WebSocket heartbeat.
SignalR:
- 
- 
- 
---
|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
This is **by design** in SignalR classic and is **not a bug**, but a limitation.
---
# Root Cause Analysis (Most likely → less likely)
# RCA‑1: Client timer starvation / blocked SynchronizationContext ✅ **Most common**
SignalR client **depends on timers** to:
- 
- 
- 
In **WinForms/WPF**, if **any** of these occur:
- 
- 
- 
- 
- 
👉 SignalR’s internal timers **do not fire** 👉 Heartbeat stops silently 👉 No `Disconnected` raised
**Result:**
- 
- 
---
# RCA‑2: Transport fallback + proxy / load balancer interference
If **WebSocket drops silently**:
- 
- 
- 
Especially common with:
- 
- 
- 
- 
**Server side** sees inactivity → marks as slow → disconnects **Client side** sees nothing → stays “Connected”
---
# RCA‑3: IIS / AppPool idle or recycle (server)
If IIS:
- 
- 
- 
You may see:
- 
- 
---
# RCA‑4: KeepAlive / Timeout mismatch (server config)
Defaults (SignalR classic):
KeepAlive = 10s
ClientTimeout = 30s
DisconnectTimeout = 30s
If:
- 
- 
👉 Server kicks client earlier than client expects
---
# RCA‑5: GC pauses in .NET Framework 4.6
Long GC pause:
- 
- 
- 
This happens more often than people expect under memory pressure.
---
# Concrete, battle‑tested solutions
# ✅ Solution 1: Treat “Slow Connection” as terminal (Server‑side)
On Hub side:
- 
- 
This avoids ghost sessions.
---
# Solution 2: Enable client‑side watchdog independent of SignalR
**DO NOT rely on SignalR events alone**
Implement:
- 
- 
- 
Example (conceptual):
If DateTime.UtcNow - lastHubMessageTime > TimeSpan.FromSeconds(60) Then
ForceReconnect()
End If
🔑 Key:
- 
- 
---
# Solution 3: Hook into `Reconnecting`, not just `Disconnected`
Many people miss this.
Client:
AddHandler connection.Reconnecting, Sub()
Log("SignalR reconnecting")
End Sub
AddHandler connection.Reconnected, Sub()
Log("SignalR reconnected")
End Sub
If `Reconnecting` never fires → timers stalled → watchdog must intervene.
---
# Solution 4: Avoid blocking the UI / main thread
Mandatory rules:
- 
- 
- 
- 
If UI is blocked → SignalR dies quietly.
---
# Solution 5: Increase server‑side tolerance (but not too much)
On server startup:
GlobalHost.Configuration.KeepAlive = TimeSpan.FromSeconds(30);
GlobalHost.Configuration.ClientTimeout = TimeSpan.FromSeconds(90);
GlobalHost.Configuration.DisconnectTimeout = TimeSpan.FromSeconds(90);
This:
- 
- 
⚠️ Do not blindly increase without watchdog (Solution 2).
---
# Solution 6: Prefer WebSockets explicitly
Force WebSockets (if infrastructure supports):
app.MapSignalR(new HubConfiguration
{
EnableDetailedErrors = true,
EnableJSONP = false
});
Ensure:
- 
- 
- 
---
# Diagnostic steps you should run **now**
1. 
2. 
3. 
SignalRTracing.Enable = true;
1. 
2. 
If issue reproduces → RCA‑1 confirmed.
**Cy Lau** (2026-03-26):
@@Joy Li  Please attach the log of MPOSPrint.exe
**Automation for Jira** (2026-03-26):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Cy Lau** (2026-04-08):
Release: 
\\ds411\share\POS_FE_Release_64\20260408 Coach v750.04R24
1) Handle slow connection as disconnected
2) enhanced watchdog for network monitoring
**Sherman tse** (2026-04-16):
Verified Ok on QA

## 相關資訊

- Jira: [MP-820](https://ctil.atlassian.net/browse/MP-820)
- Fix Version: 未記錄
- 解決日期: 未記錄

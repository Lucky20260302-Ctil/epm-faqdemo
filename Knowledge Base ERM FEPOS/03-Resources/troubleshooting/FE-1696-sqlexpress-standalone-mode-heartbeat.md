---
tags: [bug, production, hotfix]
component: Front End
symptom: "OCF47 Till0 SQL Express service timeout during counter balance query causing standalone mode failure"
root-cause: "SQL Express service on till enters idle/sleep state and fails to respond within timeout when POS queries current day sales data from Dbhist"
solution: "Added SQLExpressMonitor heartbeat checker module that periodically pings the service before main program starts, with configurable monitoring period and awaken frequency"
jira: FE-1696
resolved: 2025-05-30
---

# FE-1696: [CS-1420] SQL Express Standalone Mode — Service Heartbeat Monitor

## 問題

After upgrading to V75, OCF47 store still experiences standalone mode failure. During the first "櫃台餘額查詢" (counter balance query) of Till0, the POS calls the till0 SQL Express service to retrieve the current day's sales data from `Dbhist`, but the service does not respond within the configured timeout period, resulting in a T9 log timeout error.

The root cause from CS-1221 was previously thought to be resolved in V75, but OCF47 continued to exhibit the issue.

Affected store: OCF47

## 根因

After extensive testing, the team found that the SQL Express service on Till0 enters an idle/sleep state. When the POS initiates a query for current-day sales data from `Dbhist`, the SQL Express service fails to respond within the specified timeout window.

Key observations:
- The issue only occurs on **specific tills** where SQL Express has been idle
- Keeping Till0 SQL Express **continuously open** prevents the issue — the service stays online and responsive
- The timeout error is recorded in the T9 log

## 解法

A new **SQLExpressMonitor** heartbeat checker module was introduced:

1. **Mechanism**: A lightweight executable (`SQLExpressMonitor.exe`) that periodically monitors the SQL Express service and attempts to wake it if unresponsive
2. **Trigger**: Called once when the `Chainstoreplus` icon is clicked, **before** the main POS program starts
3. **Configuration**: Monitoring period and awaken ping frequency are configurable

**Workaround** (before patch): Keep OCF47 Till0 SQL Express continuously open to avoid the service entering idle state.

**Release**: `\\ds411\share\POS_FE_Release_64\20250515 Coach v750 SQLExpressMonitor\1_0_0`

**Deployment**: Place `SQLExpressMonitor.exe` into the `CSPLUS` folder for integration testing.

## 相關問題

- [[FE-1696|CS-1221]] — Original standalone mode issue (V75)

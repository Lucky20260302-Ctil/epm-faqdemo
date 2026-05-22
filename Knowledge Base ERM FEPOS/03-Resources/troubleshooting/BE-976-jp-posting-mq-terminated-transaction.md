---
tags: [bug, production]
component: Backend
symptom: "COACH JP Posting MQ_A and MQ_01 terminated with TRX.ROLLBACK error — ExecuteReader requires the command to have a transaction"
root-cause: "Posting process executes a database command without an associated transaction context, causing ExecuteReader to fail when the connection has a pending transaction"
solution: "Fix prj_ic8006.dll to ensure ExecuteReader commands are properly associated with the active transaction"
jira: BE-976
resolved: 2025-05-02
---

# BE-976: COACH JP Posting MQ Terminated — Transaction Context Missing

## 問題

COACH JP posting processes (`MQ_01` and `MQ_A`) terminated with a rollback error. The posting was interrupted, causing transaction data to not be properly processed.

**Error details:**
```
Error code: TRX.ROLLBACK
Error msg: ExecuteReader requires the command to have a transaction when the connection is assigned to a pending transaction
```

**Affected file**: `prj_ic8006.dll`

## 根因

The posting process executes a database command via `ExecuteReader` while the database connection already has a **pending transaction** assigned. When `ExecuteReader` is called without explicitly associating it with the existing transaction, it throws an error because the connection is not in a state to handle a new command outside the transaction context.

This typically occurs when:
1. A transaction is started on the connection
2. A new query is attempted via `ExecuteReader` without passing the transaction object
3. The system detects the connection is in a transaction and rejects the unassociated command

## 解法

The fix was applied to `prj_ic8006.dll` to ensure that `ExecuteReader` commands are properly associated with the active transaction when executed within a transaction scope.

_See Jira ticket for resolution details._

## 相關問題

- [[CS-1336]] — Coach Jira reference

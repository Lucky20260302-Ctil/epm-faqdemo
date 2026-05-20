---
tags: [bug, production, hotfix]
component: MPOS
symptom: "Queue Busting order in MPOS fails to close after POS completes the transaction — order remains visible"
root-cause: "MPOS Queue Busting order status not properly updated when POS retrieves and completes the order from a different register"
solution: "Fix Queue Busting order status update to properly close/remove orders after POS completes the transaction"
jira: MP-426
resolved: 2021-05-17
---

# MP-426: Queue Busting — Fail to Close Order After Transaction Complete

## 問題

CJ #130 — Queue Busting module in MPOS fails to close an order after the transaction has been completed by the Front End POS.

**Reproduce steps:**
1. J805 uses MPOS to create orders in Queue Busting: "Order_A" and "Order_B"
2. POS retrieves "Order_A" and completes the sales memo → Order_A disappears (normal)
3. MPOS retrieves "Order_B" and completes the sales memo → Order_B **remains visible** (bug)

## 根因

The Queue Busting order status update has a timing/sequencing issue. When the order is completed via POS on the same register, the status update works correctly. However, when the order is completed through the **MPOS-originated flow**, the signal to close the order is not properly processed.

The root cause is in the order lifecycle management — the Queue Busting module does not consistently mark orders as complete when the transaction is finalized through different completion paths.

## 解法

Fix applied in **3.9.2a (HOTFIX)** to ensure Queue Busting orders are properly closed/removed from the queue after the transaction is completed, regardless of the completion path.

## 相關問題

- [[MP-499]] — Related MPOS state management (day end restart)

---
project: FE
title: "FE-1833: Handle Rounding rule of Cash Payment in Tapestry ANZ"
issue_key: FE-1833
issue_type: Improvement
status: Open
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1833"
created: 2025-12-15
resolved: 
resolution: 
has_images: False
---

# FE-1833: Handle Rounding rule of Cash Payment in Tapestry ANZ

## 問題描述

**Australia vs New Zealand money**

 

| **Aspect** | **Australia** | **New Zealand** | 
| Currency | Australian dollar (AUD) | New Zealand dollar (NZD) | 
| Subunit | 1 dollar = 100 cents   | 1 dollar = 100 cents   | 
| Smallest coin | 5 cents | 10 cents | 
| Typical price display | Dollars and cents (e.g. $3.75) | Dollars and cents (e.g. $3.75) | 
| Cash rounding step | Nearest 5 cents | Nearest 10 cents | 

 

**Rounding rule for Australia (cash only)**

Australia applies rounding only to the final cash total, not to the unit price, because there are no 1c and 2c coins. The commonly accepted rule for cash totals is:

**Generic rounding formula**

For <u>a normal sales amount </u>10.99:

- Nearest 5 cents (0.05) for Australia:
rounded=0.05 × round(10.99/0.05) = 11.00

This gives the standard Australian 5c behavior:

- 1c or 2c → round down to 0c

- 3c or 4c → round up to 5c

- 6c or 7c → round down to 5c

- 8c or 9c → round up to 10c

So 10.99 ends in 9 cents, which rounds up to 11.00 for a cash transaction.

 

For <u>a cash refund</u>, the usual approach is to apply the *same rounding logic* to the refund amount, so the customer effectively gets back what they physically paid, rounded to the nearest 5 cents.

**Conceptual rule**

- Legally/consumer‑law wise, refunds are meant to be in the same form and amount as the original payment, subject to the same cash‑rounding rules.

- GST and the “book” sale remain at 10.99; rounding is only about the physical cash exchanged and is treated as a small rounding gain/loss in your accounts.

**Applying it to the example**

Original sale (cash):

- Tax invoice amount: 10.99

- Cash rounding on payment: +0.01 → cash payable 11.00

- Customer tenders: 12.00 → change 1.00; rounding gain 0.01 to merchant.

Full cash refund of that sale:

- Base refund amount: 10.99

- Apply same 5c rounding rule to the refund total: 10.99 rounds to 11.00

- Cash refund to customer: 11.00

Accounting-wise:

- You reverse the 10.99 sale and GST as normal.

- You post a −0.01 rounding adjustment (Misc_amt) on the refund, which offsets the +0.01 rounding you gained on the original sale (Misc_amt), so your net rounding over both transactions is zero.

This is also how many modern POS platforms model it internally: they store the unrounded amounts and GST for reporting, and maintain a separate “cash rounding adjustment (Misc_amt)” on both payments and refunds.

 

**Calculation**

- Compute rounded_total = 0.05 * ROUND(original_total / 0.05, 0).

- rounding_adjustment  (misc_amt)  = rounded_total - original_total.

- Apply this only when tender type = Cash; otherwise use original_total for card/eftpos.

Example:

- Original total = 10.99

- rounded_total = 0.05 × round(10.99 / 0.05) = 0.05 × round(219.8) = 0.05 × 220 = 11.00

- rounding_adjustment (misc_amt) = +0.01

 



## 相關資訊

- **Jira:** [FE-1833](https://ctil.atlassian.net/browse/FE-1833)
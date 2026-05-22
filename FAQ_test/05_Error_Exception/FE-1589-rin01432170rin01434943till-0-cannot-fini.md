---
project: FE
issue_key: FE-1589
issue_type: Bug DEV
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v750.01r01a
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1589
created: '2024-12-23'
resolved: '2025-04-29'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1589: [RIN01432170/RIN01434943]Till 0 cannot finish dayend, showing ''Conversion from string 19/12/2024'' to type Date is not valid'''
---
# FE-1589: [RIN01432170/RIN01434943]Till 0 cannot finish dayend, showing "Conversion from string 19/12/2024" to type Date is not valid"

## 問題描述

the POS keeps showing the error "Conversion from string 19/12/2024" to type Date is not valid" when she did dayend, and the POS still remained in the dayend page. The consolidation report was not printed out. 

user informed:

Starting from the 17 Dec, there was a daily dayend failure after the POS system upgraded.

1）The result of dayend can’t be found after the Till 0 dayend, do you want to continue consolidated? Then another morning, the pos system of Till 1 & Till 3 could not start normally.
2）We entered our employee number to prepare the daily settlement, but the pos system prohibited us from making the dayend because the system date jumped to the next day, so the daily settlement failed.
3）When we finished the daily settlement in Till 0, there were 3 days consecutive dailyend and a lot of paper printed out.

Logs link:[20241123-FE-1589](https://ctil00046-my.sharepoint.com/:f:/g/personal/jason_wu_ctil00046_onmicrosoft_com/Em0RUFn9sdxJoMFS7LtJNrUBlt1fGFGdSVBlAMFdyyt5yw?e=2YqPZf)

Joy copied file:[20241123-FE-1589](https://ctil00046-my.sharepoint.com/:f:/g/personal/jason_wu_ctil00046_onmicrosoft_com/Em0RUFn9sdxJoMFS7LtJNrUBlt1fGFGdSVBlAMFdyyt5yw?e=2YqPZf)\OC507till0\retdata6\20241222



## 相關資訊

- **Jira:** [FE-1589](https://ctil.atlassian.net/browse/FE-1589)
- **解決方式:** Done
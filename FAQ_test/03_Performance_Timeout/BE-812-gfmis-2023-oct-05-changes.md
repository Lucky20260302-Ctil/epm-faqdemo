---
project: BE
title: "BE-812: GFMIS 2023-OCT-05 changes"
issue_key: BE-812
issue_type: Improvement
status: Closed
faq_score: 4.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-812"
created: 2023-10-05
resolved: 2023-11-02
resolution: Done
has_images: False
---

# BE-812: GFMIS 2023-OCT-05 changes

## 問題描述

1. FPS will be hardcoded into the program.

2. remove space in revenue code display.

3. only include below payment type and exclude all other payment type.

- Cash

- Octopus

- Credit card

- Cheque

- SVF (Except Octopus)

- FPS (new added)

4. map location code to 4 digits.

| Collection Center Code | Outlet | Location | 
| 0002 | Sales/K | LMK | 
| 0001 | Sales/HK | LHQ | 
| 0161 | DSO/HK | LHK | 
| 0020 | DSO/Is | LIS | 
| 0121 | DSO/K | LKL | 
| 0091 | DSO/N | LNR | 
| 0011 | DSO/SK | LSK | 
| 0009 | DSO/ST | LST | 
| 0006 | DSO/TP | LTP | 
| 0003 | DSO/TW&KT | LTK | 
| 0019 | DSO/TM | LTM | 
| 0005 | DSO/YL | LYL | 



## 相關資訊

- **Jira:** [BE-812](https://ctil.atlassian.net/browse/BE-812)
- **解決方式:** Done
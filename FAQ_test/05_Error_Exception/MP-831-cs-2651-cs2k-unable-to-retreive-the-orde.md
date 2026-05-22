---
project: MP
title: "MP-831: [CS-2651] CS2K Unable to retreive the order upload by MPOS"
issue_key: MP-831
issue_type: Bug QA
status: Release
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-831"
created: 2026-04-28
resolved: 
resolution: 
has_images: False
---

# MP-831: [CS-2651] CS2K Unable to retreive the order upload by MPOS

## 問題描述

we did testing with CS2K version: v75.004.2400.0000 and MPOS 3.30.8, during testing we found that CS2K unable to retreive the order upload via MPOS first time.

Testing machine IP: 10.34.103.3(KR Region - OCQ96), connecting to web24.

Reproduce steps:

| 1 | Go to MPOS Sales->Sales->Create New, input item code then search | 
| 2 | Search below Item:
18020 SV/DB | 
| 3 | Slide to left, click 'Member' | 
| 4 | Select 'vip No' then input vip no: J101WJ00054065 to search | 
| 5 | Click Pay button | 
| 6 | Click ↑ button | 
| 7 | Input 'Remarks', 'Name', 'Email', 'Mobile', 'Title' | 
| 8 | Then click  √ | 
| 9 | Check saved transaction in CS2K POS: Sales->Issue sales->More->Retrive Order | 

**Then nothing showing in CS2K**, from MPOS we modify the draft and upload again, then able to trigger:

| 10 | Go back to MPOS, Slide to left to check 'Queue Busting' | 
| 11 | Click the transaction | 
| 12 | Delete the item we select before | 
| 13 | Search below Item:
50013 LICHT | 
| 14 | Click Pay button | 
| 15 | Click ↑ button | 
| 16 | Then click  √ | 
| 17 | Check saved transaction in CS2K POS: Sales->Issue sales->More->Retrive Order | 
| 18 | Double click to trigger the order | 



## 相關資訊

- **Jira:** [MP-831](https://ctil.atlassian.net/browse/MP-831)
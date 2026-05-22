---
project: BE
issue_key: BE-1032
issue_type: Improvement
status: Closed
tags:
- 05_error_exception
- api
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1032
created: '2025-03-19'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-1032: [ACU-122] Email field (When search customer) should have validation in backend'
---
# BE-1032: [ACU-122] Email field (When search customer) should have validation in backend

## 問題描述

Add verification with the format of "Email", 

if input value is not a valid email format, 

show error message to the POS terminal, without calling API to search member.

### Consider about searchExact only

Sample :

```
public class EmailValidator
{
    public static bool IsValidEmail(string email)
    {
        if (string.IsNullOrWhiteSpace(email))
        {
            return false;
        }

        string pattern = @"^[^@\s]+@[^@\s]+\.[^@\s]+$";
        return Regex.IsMatch(email, pattern);
    }
}

```



## 相關資訊

- **Jira:** [BE-1032](https://ctil.atlassian.net/browse/BE-1032)
- **解決方式:** Done
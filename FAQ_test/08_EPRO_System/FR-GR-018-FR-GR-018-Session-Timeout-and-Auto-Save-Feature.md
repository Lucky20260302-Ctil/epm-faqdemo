---
title: "FR-GR-018: FR-GR-018: Session Timeout and Auto-Save Feature"
tags: [epro, EPRO_System]
---

# FR-GR-018: FR-GR-018: Session Timeout and Auto-Save Feature

## 需求描述

Requirement ID:	FR-GR-018	Requirement Type:	General Requirements
Parent Requirement #:
None
Description:
    - **3.1.21** The Platform shall allow configuration of timeout duration, automatically logging out the user after a period of inactivity, this timeout duration may be different for various activities in the Platform if applicable. Auto-save function shall be applied to save all inputted / uploaded information before automatically logging out the user.
Rationale:
None
Acceptance / Fit Criteria:
The Platform should enforce session timeouts, automatically terminating inactive sessions after a specified period of inactivity:
Note: The session timeout settings can be configured by System admin users.
All e-Forms are automatically saved to prevent data loss in case of a session timeout.
For long uploading files, the session timeout will not be caused because the file upload function utilizes 10MB file chunks to upload pieces of the file. As a result, the session will remain active without experiencing a session timeout after uploading a large file.
The Platform to track and monitor session timeouts in the system logs.
The Platform shall successfully perform all the actions outlined in the Use Case 12.1 and Use Case 18.
Dependencies:
None
Tailoring Guidelines:
None
Change History:
None
---
project: EPRO_TDC
title: EPRO 系统中"我的任务"（My Task）功能包括哪些操作？
category: 仪表盘与任务管理
source: Internal User Manual Section 4.2.2 Page 13-45
tags:
  - epro
  - user-manual
  - faq
  - 我的任务
  - My Task
  - 任务管理
  - 草稿
  - draft
quality: complete
created: '2026-05-26'
---

4.2.2  My Task


All system operations in EPRO are initiated and managed through individual e-Form listed
under “My Task”.

This section serves as the central workspace for users to perform actions such as drafting,
submitting, reviewing and approving e-Forms.





     4.2.2.1 My Task – New Requests


All e-Forms can be searched under the “New Requests” section. ,Users can create new e-Forms
based on the provided descriptions, or filter available e-Forms using search criteria to locate
specific request types efficiently.







4.2.2.1.1    e-Form Identification


Each e-Form is created with a unique request number and includes brief information to help
users identify and track the request efficiently.


     4.2.2.1.2    User Roles in e-Form Access





Initiator: The User who creates the e-Form.
Unsubmitted drafts will be stored under "My Task" > "Drafts" .
Requestor: The User who requests for the e-Form.
The e-Form will be stored under "My Task" > "Other Pending Actions".
Co-editor(s): Users who are granted permission to review, edit and submit the e-Form, with
the same level of access as the Initiator/ Requestor.

View-only User(s): Users assigned read-only access to the e-Form.

Relevant e-Forms can be accessed from the “Sourcing” section.



**Only users assigned as Initiator/ Requestor/ Co-editor(s)/ View-only User(s) can access to
the corresponding e-Form.





4.2.2.1.3    e-Form Process Stages

e-Form will be proceeded by 4 stages as follows:

    1.  Draft: All fields are editable. Users can input and update information before submission.





    2.  Review and Validate: The e-Form becomes read-only. The system performs validation
       checks to identify any missing or incorrect data.





    3.  Confirm: Users must read and confirm the terms and conditions. The e-Form can only
      be submitted after all required checkboxes are checked.





    4.  Submission: It displays the submission confirmation page. It services a record of the
      completed e-Form submission.



4.2.2.2 My Task – Drafts


All incomplete e-Forms, including those created but not yet filled in, are saved under “Drafts”
for both the Requestor and Co-editor(s). Users can filter relevant e-Forms using search criteria
to quickly locate and resume draft requests.






4.2.2.2.1     Approval Route Setting


Approval route setting is available for e-Forms that require approval. Up to six (6) levels of
approval can be defined, with each level assigning either:

        Multi-level approval (sequential); or
        Parallel approval (multiple approvers acting simultaneously).

Special Conditions in the following are mandatory only for specific request types, depending on
the nature and scope of the procurement:-

       Level 5 Approvers (F&A users);and
       Level 6 Approvers (Tender Board)






4.2.2.2.2     Approval Route Selection


The Requestor selects the appropriate approval route setting from a drop-down list and
specifies the approval method, such as multi-level or parallel approval, based on the
requirements of the e-Form.





     4.2.2.2.3     Offline Approval Method (Available in a later phase)


For e-Forms using the offline approval method, the following are required:-

        Offline approval date
       Supporting document(s)
      Assigned approvers for each approval level

This method is applicable only when approvals are conducted outside the system and later
recorded in the EPRO platform.






4.2.2.2.4     Draft Status Update


Upon submission of an e-Form, its status will be immediately updated as “Finished”, indicating
the completion of the drafting phase.





     4.2.2.2.5     Tender Board Assignment Process


The Level 6 approver (Tender Board) will be assigned by an F&A user upon the completion of
Level 5 approval.

A draft of the Tender Board Assignment will be auto-generated for the last approver of level 5,
and stored under “Drafts”

(Note: This does not apply to the offline approval method.)


     4.2.2.2.6     Tender Board Approval Submission


After assigning the Tender Board approver, the User submits the e-Form. An email notification
is automatically sent to assigned approver to proceed with the approval process.





4.2.2.2.7    e-Form Interface Features


An action button is available at the bottom of each e-Form page, allowing users to perform
actions such as save, submit, or cancel.


     4.2.2.2.8     System Auto-Save Function


The system monitors user activity and performs an auto-save cycle for every 30 seconds, The
latest record date and time is displayed to confirm the most recent save.





     4.2.2.2.9    e-Form Action Buttons


The following action buttons are available to support user operations throughout the e-Form
process;-

Abandon Changes: User is able to revert the e-Form to the last save date by discarding any
changes that have not been manually saved or auto saved.

Discard E-Form: Deletes the draft entirely from the “Drafts” section. This action is irreversible.

Save & Edit Later: Manually saves the current updates and closes the form for future editing.

Review & Validate: User submits the e-Form manually for system validation, checking for
missing or incorrect data.

(As referenced in section 4.2.2.1)





4.2.2.3 My Task – Other Pending Actions


User with Requestor role can search and view e-Forms under “Other Pending Actions” section,
including:-

       Drafted e-Forms
      Submitted e-Forms pending approval
      Returned e-Forms requiring revision .

Relevant e-Forms can be filtered using search criteria to help users locate and manage their
pending tasks efficiently.






4.2.2.4 My Task – Pending Approvals


Users assigned with the Approver role can review all outstanding approval requests under the
“Pending Approvals” section. This section allows approvers to review, validate and proceed
with e-Form approvals as required.





Approval details:







4.2.2.4.1     Approval action:


     4.2.2.4.2     Clarification tool
      Approver can raise a new clarification during the approval process, to address minor
       issues or questions before proceeding.

Clarification Steps:

Step 1: Click “New Clarification”





Step 2: Fill in the clarification details as follows:

 Details Fields      Mandatory / Optional   Purpose
 Title             Mandatory             Creates a discussion threadand separates different issues.

 Target Resolved   Mandatory            Sends reminder emails to recipient if the issue has not
 Date                                        yet resolved by the target date.
 Recipient(s)       Mandatory             Selected recipients receive email notification after
                                              issuance.
 Details           Mandatory             Describes the issue and provides relevant information.
 Attachment        Optional             Allows additionals supporting documents to be uploaded.






Step 3: Submit the clarification after filling the information.





      Once submitted. the clarification status is updated.
      The e-Form cannot further proceed to approval until the clarification is resolved.
      Email notifications are sent to the recipient.
      Other approvers are notified via system notifications and can review the clarification
       record in their approval process or under “Completed Tasks” (for previous approvers).



Recipient Actions:

Step 4: Recipient logs in to EPRO and accesses the e-Form from “Other Pending Actions”. Click
“View Clarification” button to expand the history.






Step 5: Click to expand the clarification details.

     A response is required for recipient, either by typing a reply in text or uploading an
       attachment.






- Once submitted, the clarification status updates and the approver who raised this
clarification receives an email notification. Other approvers remains notified via system
notifications only.

Follow-up actions by Approver:

Step 6: Approver logs in to system after receiving the email notification and reviews the
clarification from “Pending Approvals”. The recipient’s response must be read before
proceeding to approval.






Step 7: Expand the clarification details.






Step 8: Click the refresh button (    )to update the system read time.  If not refreshed, the
approval remains frozen and cannot proceed.






4.2.2.4.3    Amend e-Form
      Approver can revise minor mistakes, e.g. typos, during the approval process using the
     “Amend e-Form" function. Edits are limited primarily to text fields, and the approval
       route remains unchanged and non-editable


Step 1: Click “Amend E-Form” after review the e=Form.





Step 2: The System retrieves the original e-Form for editing.Editable fields are marked with

and edit icon(   button). Approver can update the necessary details, or click “Abandon
Changes” to discard the updates.







The approval route remains unchanged and non-editable.





Step 3: Click “Review and Validate” after completing the amendments.





Step 4: Click “Confirm & Submit” after reviewing all the revised details.







Step 5: Provide the reason(s) for changes, confirm the terms and conditions and click “Yes,
proceed with submitting the e-Form”.





The e-Form will be submitted with a submission record and the history can be tracked under
“Completed Tasks” section. Updated details will be reflected in the pending approval task for
subsequent approvers.






4.2.2.4.4    e-Form Return Process (Approver)


Approver can return an e-Form to the Requestor for editing and re-submission.

Step 1: Click “Return” on the e-Form if changes are needed.





Step 2: To provide a reason for return for the following:-

      Mandatory: Enter a comment explaining the reason.
       Optional: Upload a supporting document if necessary

Click “Submit Feedback” to proceed.






Once submitted, the e-Form status changes to “Return to requestor”.





The Requestor can edit and resubmit the e-Form following the original pre-set approval route
upon resubmission.






4.2.2.4.5    e-Form Rejection Process (Approver)


Approvers can reject an e-Form if necessary, especially involving a conflict of interest.

Step 1: Click “Continue to Approval” to begin the review process.





Step 2: Declare conflict of interest.

The system defaults the declaration as “No” conflict of interest.






If a potential conflict of interest in declared in the HR system and approved, the Approver is
required to upload the supporting document under the “Action” section.






Approver can only reject the approval request if pre-approval is not yet obtained through HR
system in advance.







Step 3: To reject the request, click “Reject” and provide a reason for rejection(mandatory).
Optionally, Approver can attach upporting document for reference. And Approver clicks
“Submit Reject” to proceed.





After submission, the Requestor receives and email notification of rejection, and no further
updates and resubmission allowed for rejected request.






4.2.2.5 My Task – Completed Task


User with the Requestor role (or those assigned as View-only user for specific e-Form) can
search and view all e-Form that submitted and/or pending for approval.





E-Form related history can be tracked with completed e-Form details, and details of approval
history and actions taken.

---
title: "FR-GR-002: FR-GR-002: System Architecture of the Platform"
tags: [epro, EPRO_System]
---

# FR-GR-002: FR-GR-002: System Architecture of the Platform

## 需求描述

Requirement ID:	FR-GR-002	Requirement Type:	General Requirements
Parent Requirement #:
None
Description:
    - **3.1.1** The Platform shall be built in a microservice architecture that will allow the addition and/or integration of other functional modules, either developed by the Contractor or other HKTDC's engaged suppliers, without impacting the overall platform functionality.
Rationale:
None
Acceptance / Fit Criteria:
The Platform consists of the following major function blocks:
Web Layer
The Web Layer serves as the front-end of ProSmart, providing user interfaces for different user roles such as administrators, suppliers, and tender evaluators. It is built using a web framework (Vue) and interacts with the backend services through HTTP/HTTPS requests. The Web Layer communicates with the API Gateway to access different backend services, ensuring secure and efficient handling of user requests.
Blob Storage
Blob Storage is used to store large unstructured data such as documents, images, videos, and other files related to tenders and suppliers. This component supports functionalities like uploading, downloading, and securely storing files. It integrates with the File Service to manage access and retrieval, and the File Conversion Service to handle file format conversions when needed.
API Gateway
The API Gateway acts as a single-entry point for all client requests for the backend services. It provides routing, load balancing, and protocol translation, ensuring that requests are directed to the appropriate microservice. It also enforces security policies, such as rate limiting, IP whitelisting, and SSL termination, and integrates with the Authorization and Authentication Service to validate user credentials.
Message Broker
The Message Broker facilitates asynchronous communication between different services in the architecture, supporting event-driven communication patterns. It is used to handle events such as supplier registration, tender submissions, and workflow transitions. The Message Broker ensures reliable message delivery and decouples the services, enhancing the system's scalability and fault tolerance.
Searching Service
The Searching Service provides advanced search capabilities across different datasets within the system, such as supplier information, tender documents, and historical data. It is implemented using a search engine (e.g., Elasticsearch) to offer full-text search, filtering, and sorting functionalities. This service integrates closely with the Web Layer and API Gateway to support quick and efficient data retrieval.
Authorization, Authentication, and User Service
This service is responsible for managing user identities, authentication processes, and access control. It supports multi-factor authentication (MFA), single sign-on (SSO), and role-based access control (RBAC) to ensure secure access to the system. The service integrates with external identity providers and handles user sessions and tokens, ensuring secure communication between users and services through the API Gateway.
Logging Service
The Logging Service collects, stores, and analyzes logs from various components within the system. It provides centralized logging and monitoring capabilities, essential for troubleshooting, performance monitoring, and security audits. The Logging Service integrates with the API Gateway, Workflow Services, and other backend services to capture relevant events and activities.
Workflow Services
Workflow Services manage the business processes and workflows within ProSmart. These services automate processes such as tender creation, submission, evaluation, and approval. They support dynamic workflow definitions and integrate with other services like Notification, Supplier, and Tendering Services to trigger events and actions based on workflow states and transitions.
Form Designer Service
The Form Designer Service allows users to create and customize forms for data collection, such as tender applications, supplier registration, and evaluation forms. It provides a user-friendly interface for designing forms and integrates with the Workflow Services to link forms with specific workflows and business processes.
Supplier Service
The Supplier Service manages all functionalities related to suppliers, including registration, profile management, performance tracking, and compliance verification. It integrates with the Workflow Services for onboarding processes and the Reporting Service to generate supplier performance reports.
Tendering Service
The Tendering Service handles the entire lifecycle of tenders, from creation to award. It provides functionalities for tender publishing, bid submission, bid evaluation, and award management. This service interacts with the Supplier Service, Workflow Services, and Notification Service to manage tender-related communications and processes.
Reporting Service
The Reporting Service generates various reports based on the data stored in the system. It provides insights into tender processes, supplier performance, and system usage. The service integrates with Blob Storage for report storage and the Web Layer for report access and visualization.
Scheduler Service
The Scheduler Service manages scheduled tasks and background jobs, such as periodic data cleanup, report generation, and notification dispatch. It ensures that scheduled tasks are executed reliably and integrates with other services to trigger events or actions based on predefined schedules.
Notification Service
The Notification Service is responsible for sending notifications to users via different channels such as email, SMS, and push notifications. It integrates with the Workflow Services to trigger notifications based on workflow events and with the Scheduler Service for scheduled notifications.
File Conversion Service
The File Conversion Service handles file format conversions required by the system. It supports converting documents, images, and other file types into required formats for processing or viewing. This service integrates with the Blob Storage and File Service to manage file operations securely and efficiently.
File Service
The File Service provides an API for managing files stored in Blob Storage. It handles file uploads, downloads, versioning, and access control. The service integrates with the Blob Storage for physical storage and the API Gateway to expose file management functionalities to the Web Layer.
External Integration Service
The External Integration Service manages communication with external systems, such as ERP systems, regulatory databases, and third-party services. It handles data exchange and ensures data consistency and integrity across systems. This service integrates with other components like Supplier Service and Tendering Service to facilitate seamless integration and data flow.
Internet Gateway
The Internet Gateway acts as a bridge between the internal network of ProSmart and the internet. It provides secure access to external services and resources and applies security measures such as firewalls, intrusion detection, and prevention systems to protect the internal network from external threats.
Overall Architecture Interaction Flow
User Interaction: Users interact with the system via the Web Layer, which routes requests through the API Gateway.
API Gateway: The API Gateway forwards requests to appropriate backend services, enforcing security policies.
Service Coordination: Services like Supplier, Tendering, and Workflow Services coordinate to manage business processes.
Asynchronous Communication: The Message Broker facilitates asynchronous communication between services, ensuring reliable event handling.
Data Storage and Management: Blob Storage, File Service, and File Conversion Service manage document storage, access, and conversion.
External Integration: The External Integration Service ensures seamless communication with external systems and services.
Search and Reporting: The Searching and Reporting Services provide data retrieval and reporting capabilities to users and administrators.
Security and Monitoring: The Authorization, Authentication, and User Service ensures secure access, while the Logging Service provides system monitoring and auditing.
Dependencies:
FR-GR-028 Customization Requirements to the Platform
Tailoring Guidelines:
None
Change History:
None
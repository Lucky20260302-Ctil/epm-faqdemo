---
project: MP
issue_key: MP-786
issue_type: Improvement
status: Open
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-786"
created: 2025-07-18
resolved: 
resolution: 
has_images: True
---

# MP-786: [Stability, Tech Debt] SignalR plugin development

> **類型:** Improvement | **狀態:** Open
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **負責人:** Daniel Leung
> **組件:** MPOS

## 問題描述

In order to have stability for the signalR connection for MPOS, a development on flutter shall be needed.

Currently the plugin using are riding on a webview making use of signalR.js 

### Architecture Overview

The implementation follows a three-tiered architecture that maximizes platform capabilities while ensuring seamless Flutter integration. The foundation consists of native libraries that directly interface with platform-specific networking APIs, providing optimal performance for WebSocket connections and SignalR protocol handling.

> 📎 **image-20250718-062245.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/925166f9-d959-4819-85d5-bd76e23d65c4)（需 Jira 登入）

### Implementation Strategy

### Phase 1: iOS Native Library Development

The iOS implementation utilizes Apple's URLSession framework for WebSocket connectivity, providing native integration with iOS networking capabilities. The core `SignalRManager` class handles connection lifecycle, message routing, and protocol compliance.

**Key Technical Components:**

- **Connection Negotiation**: Implements SignalR's negotiation protocol to establish optimal transport

- **WebSocket Management**: Leverages URLSessionWebSocketTask for efficient bidirectional communication

- **Protocol Handling**: Manages SignalR Hub Protocol message formatting and parsing

- **Lifecycle Integration**: Proper memory management and iOS app lifecycle awareness

The implementation prioritizes thread safety through careful queue management, ensuring UI responsiveness while maintaining reliable background connectivity. Error handling encompasses network failures, protocol violations, and resource constraints specific to iOS environments.

### Phase 2: Android Native Library Development

The Android implementation leverages OkHttp's WebSocket capabilities, providing robust connectivity with built-in connection pooling and retry mechanisms. The architecture embraces Kotlin coroutines for asynchronous operations while maintaining Java compatibility.

**Core Architecture Elements:**

- **Coroutine-Based Connectivity**: Asynchronous connection management without blocking UI threads

- **Lifecycle Awareness**: Integration with Android's component lifecycle for optimal resource management

- **Network Adaptation**: Automatic handling of network changes and cellular transitions

- **Battery Optimization**: Efficient reconnection strategies to minimize power consumption

The Android implementation addresses platform-specific challenges including background execution limitations, network security policies, and diverse device capabilities across the Android ecosystem.

### Phase 3: Flutter Plugin Bridge Implementation

The Flutter bridge unifies native implementations through platform channels, providing a consistent API regardless of underlying platform differences. The architecture employs both MethodChannel for request-response operations and EventChannel for streaming message delivery.

**Integration Architecture:**

- **Unified API Surface**: Consistent method signatures across platforms

- **Bidirectional Communication**: Efficient message routing from native to Flutter

- **Error Harmonization**: Standardized error handling and reporting

- **Performance Optimization**: Minimal serialization overhead for high-frequency messaging

The bridge implementation ensures data consistency across platform boundaries while maintaining the performance characteristics of native implementations.

### 

---

### iOS Native Library Architecture

The iOS implementation embraces Swift's modern concurrency model while maintaining compatibility with UIKit application lifecycles. The core architecture separates transport concerns from protocol handling, enabling future transport method additions without architectural changes.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8d019886-6397-4314-bea2-2078ebd6f302)（需 Jira 登入）
**Key Implementation Highlights:**

- **URLSession Integration**: Native WebSocket support with automatic HTTP/2 upgrade capabilities

- **Negotiation Protocol**: Full SignalR negotiation sequence with transport selection

- **Memory Management**: Careful use of weak references to prevent retain cycles

- **Error Recovery**: Comprehensive error handling with exponential backoff reconnection

### Android Native Library Architecture

The Android implementation leverages modern Kotlin features while maintaining broad compatibility across Android versions. The architecture emphasizes lifecycle awareness and network resilience.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ccce9f72-c280-422a-b2ef-75cfdf802052)（需 Jira 登入）
**Implementation Characteristics:**

- **OkHttp WebSocket**: Industrial-strength WebSocket implementation with connection pooling

- **Coroutine Integration**: Structured concurrency for reliable connection management

- **Lifecycle Awareness**: Proper handling of app backgrounding and network changes

## 附件截圖

1. 📎 **image-20250718-062245.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/925166f9-d959-4819-85d5-bd76e23d65c4)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8d019886-6397-4314-bea2-2078ebd6f302)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ccce9f72-c280-422a-b2ef-75cfdf802052)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/11c209c2-45ec-42c0-9d33-22c7b09f535a)

## 相關資訊

- **Jira:** [MP-786](https://ctil.atlassian.net/browse/MP-786)
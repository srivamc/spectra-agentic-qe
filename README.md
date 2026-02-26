# SPECTRA: Spec-driven, Platform-agnostic, Extensible, Cloud-ready Test Runner with Agentic AI

> **The "CEO of Quality" for the Modern SDLC.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://python.org)
[![MCP Protocol](https://img.shields.io/badge/MCP-Enabled-purple.svg)](https://modelcontextprotocol.io)

---

## What is SPECTRA?

**SPECTRA** is a fully generic, spec-driven agentic test automation framework designed to test **UI applications** and **backend REST/GraphQL APIs** using a multi-layer AI agent architecture powered by the **Model Context Protocol (MCP)**.

Unlike traditional test automation tools tied to a proprietary platform, SPECTRA is:

- **Spec-driven** – Ingests OpenAPI 3.x, Postman collections, AsyncAPI, or custom YAML specs to auto-generate tests.
- **Platform-agnostic** – No vendor lock-in; runs on any CI/CD system (GitHub Actions, GitLab CI, Jenkins, Azure DevOps).
- **AI-first** – Uses a 3-layer multi-agent architecture (18 specialized agents) to autonomously generate, execute, and heal tests.
- **Dual-mode** – Covers both UI (browser via Playwright) and Backend API (REST/GraphQL/gRPC) testing from the same framework.
- **Zero-migration** – Works alongside existing test suites; does not break existing tests.

### Why SPECTRA?

In an enterprise world of thousands of microservices, "testing" isn't enough. You need **Contract-Driven Intelligence**.

1. **Spec-as-Truth:** Unlike generic AI testers, SPECTRA uses your API specs (OpenAPI, AsyncAPI, etc.) as the absolute source of truth.
2. **Autonomous Reasoning:** It doesn't just run scripts; it reasons about contract violations, identifies infrastructure bottlenecks, and executes complex end-to-end flows.
3. **Governance-First:** It speaks the language of leadership—reporting quality in terms of compliance, revenue-at-risk, and service-level objectives (SLOs).

---

## 3-Layer Agent Architecture

### Layer 0: Strategic (Management)
- **Test Orchestrator Agent:** The "Project Manager" that assigns tasks to specialist agents.
- **Analysis Agent:** Provides root cause analysis and executive summaries.

### Layer 1: Specialist (Execution)
- **API Testing Specialist:** Autonomous REST/GraphQL validation.
- **Security Testing Specialist:** OWASP Top 10 automated scanning during functional flows.
- **Performance Testing Specialist:** Validates SLAs, latency, and throughput.
- **Code Review Specialist:** Intelligent PR analysis for testability.

### Layer 2: Foundation (Core Skills)
- **Spec Analyzer Agent:** Ingests and enforces the contract.
- **Discovery Agent:** Identifies "Shadow APIs" not present in documentation.
- **Healing Agent:** Predictive self-healing that generates code refactoring PRs.

---

## Model Context Protocol (MCP) Integration

SPECTRA is **MCP-Native**. This allows our agents to:
- **Persist Memory:** Context travels across test sessions.
- **Connect Silos:** Functional agents share state with Security agents in real-time.
- **Deep Visibility:** Agents access server logs and infra state to verify "why" a contract failed.

---

## Getting Started

### 1. Installation
```bash
pip install spectra-qe
```

### 2. Configure MCP
Create a `.mcp.json` in your project root to enable cross-session intelligence.

### 3. Run Your First Validation
```bash
python run_spectra.py --spec https://api.yoursite.com/openapi.json
```

---

## Strategic Roadmap
- **Phase 1 (Q1 2026):** Foundation – 3-Layer Architecture & MCP Support (Current).
- **Phase 2 (Q2 2026):** Zero-Touch Discovery – Autonomous spec crawling and Shadow API detection.
- **Phase 3 (Q3 2026):** IDE-Native – VS Code and IntelliJ plugins for real-time validation.
- **Phase 4 (Q4 2026):** Enterprise Scale – Swarm orchestration for 1000+ parallel agents.

---

## License
SPECTRA is open-source software licensed under the [Apache 2.0 License](LICENSE).

---
*“SPECTRA: Where the Spec meets the Speed of AI.”*

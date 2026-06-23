# Unified Cybersecurity Automation & Defensive Suite (v1.0)

A terminal-based console application built in Python to automate core security tasks. This project integrates functional utilities for basic network mapping, cryptographic data handling, defensive input sanitization, and real-time log analysis into a single, interactive dashboard. 

---

## CORE SECURITY MODULES

### 1. Password Entropy Auditor
* **Focus Area:** Identity & Access Management (IAM)
* **How it works:** Uses regular expressions (`re`) to evaluate a password's strength beyond simple character length. It audits structural complexity—checking for a mix of uppercase, lowercase, numbers, and special symbols—to flag strings vulnerable to brute-force or dictionary attacks.

### 2. TCP Port Surface Mapper
* **Focus Area:** Network Security & Reconnaissance
* **How it works:** Built using Python’s native `socket` library. It conducts basic connection sweeps (`connect_ex`) against a target host using strict timeout throttling to identify open, listening TCP ports. This maps out network entry points within a safe testing sandbox.

### 3. Input Sanitizer (XSS Mitigation)
* **Focus Area:** Application Security (OWASP Top 10)
* **How it works:** Mimics basic Web Application Firewall (WAF) input filters by encoding raw user strings into safe HTML entities using the `html` library. By neutralising dangerous tags like `<script>`, it prevents reflected Cross-Site Scripting (XSS) attacks from executing in a browser environment.

### 4. Symmetric Key Cipher
* **Focus Area:** Data Cryptography at Rest
* **How it works:** Implements symmetric text encryption using the industry-standard Fernet schema (built on AES-128 in CBC mode). The tool handles runtime key generation to instantly obscure plain-text variables into safe ciphertext strings, demonstrating data confidentiality principles.

### 5. Brute-Force Intrusion Log Parser
* **Focus Area:** Incident Response & Log Analytics
* **How it works:** A pattern-matching log analyzer that parses a continuous system authentication buffer. It tracks consecutive login failures (`AUTH_FAILURE`) linked to unique user IDs. If failure volumes exceed a set threshold, it throws an incident alert to flag automated brute-force attempts.

---

## 🚀 Deployment & Local Execution

Ensure you have your environment set up properly, then run the central dashboard:

```bash
pip install cryptography
python main.py

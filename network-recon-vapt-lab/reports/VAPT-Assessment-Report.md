# Enterprise Network Configuration Audit & VAPT Report
**Generated (UTC):** 2026-11-22 14:13:51
**Target Scope:** `172.28.0.0/24` (3-Tier Corporate Lab Subnet)

## 1. Executive Risk Summary (Baseline - Before Hardening)
| Target Host | Port | Service Fingerprint | CVSS v3.1 Severity | Finding |
| :--- | :--- | :--- | :--- | :--- |
| `172.28.0.10` | `80/tcp` | http nginx 1.31.9 | **5.3 (MEDIUM)** | Cleartext HTTP Listener & Server Version Banner Disclosure |
| `172.28.0.20` | `8080/tcp` | http SimpleHTTPServer 0.6 | **7.5 (HIGH)** | Unencrypted Internal HTTP Microservice Exposed Without Segmentation |
| `172.28.0.30` | `6379/tcp` | redis Redis key-value store 7.4.12 | **9.8 (CRITICAL)** | Unauthenticated Backend Redis Service Exposed on Shared Subnet |

## 2. Detailed Findings & Remediation Plan
### 1. Cleartext HTTP Listener & Server Version Banner Disclosure (`172.28.0.10:80`)
- **Severity:** 5.3 (MEDIUM)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`
- **Service:** `http nginx 1.31.9`
- **Remediation:** Disable server_tokens in Nginx and enforce defensive HTTP security headers (X-Frame-Options, X-Content-Type-Options).

### 2. Unencrypted Internal HTTP Microservice Exposed Without Segmentation (`172.28.0.20:8080`)
- **Severity:** 7.5 (HIGH)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`
- **Service:** `http SimpleHTTPServer 0.6`
- **Remediation:** Isolate internal-app from the edge subnet and route traffic strictly through an authenticated reverse proxy.

### 3. Unauthenticated Backend Redis Service Exposed on Shared Subnet (`172.28.0.30:6379`)
- **Severity:** 9.8 (CRITICAL)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
- **Service:** `redis Redis key-value store 7.4.12`
- **Remediation:** Enforce requirepass authentication and isolate backend-db inside an internal-only segmented network.

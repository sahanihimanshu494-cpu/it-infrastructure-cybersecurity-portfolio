#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

RISK_RULES = {
    "6379": {
        "title": "Unauthenticated Backend Redis Service Exposed on Shared Subnet",
        "cvss": "9.8 (CRITICAL)",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        "remediation": "Enforce requirepass authentication and isolate backend-db inside an internal-only segmented network."
    },
    "8080": {
        "title": "Unencrypted Internal HTTP Microservice Exposed Without Segmentation",
        "cvss": "7.5 (HIGH)",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
        "remediation": "Isolate internal-app from the edge subnet and route traffic strictly through an authenticated reverse proxy."
    },
    "80": {
        "title": "Cleartext HTTP Listener & Server Version Banner Disclosure",
        "cvss": "5.3 (MEDIUM)",
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N",
        "remediation": "Disable server_tokens in Nginx and enforce defensive HTTP security headers (X-Frame-Options, X-Content-Type-Options)."
    }
}

tree = ET.parse("scans/02-baseline-audit.xml")
root = tree.getroot()
findings = []

for host in root.findall("host"):
    ip = host.find("address").attrib.get("addr", "unknown")
    for port in host.findall(".//port"):
        if port.find("state").attrib.get("state") != "open":
            continue
        portid = port.attrib.get("portid")
        svc_el = port.find("service")
        if svc_el is not None:
            name = svc_el.attrib.get("name", "")
            product = svc_el.attrib.get("product", "")
            version = svc_el.attrib.get("version", "")
            svc = f"{name} {product} {version}".strip()
        else:
            svc = "unknown"
        rule = RISK_RULES.get(portid, {
            "title": f"Exposed Service ({svc})",
            "cvss": "4.3 (MEDIUM)",
            "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N",
            "remediation": "Restrict via firewall ACLs."
        })
        findings.append((ip, portid, svc, rule))

now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
lines = [
    "# Enterprise Network Configuration Audit & VAPT Report",
    f"**Generated (UTC):** {now_str}",
    "**Target Scope:** `172.28.0.0/24` (3-Tier Corporate Lab Subnet)\n",
    "## 1. Executive Risk Summary (Baseline - Before Hardening)",
    "| Target Host | Port | Service Fingerprint | CVSS v3.1 Severity | Finding |",
    "| :--- | :--- | :--- | :--- | :--- |"
]
for ip, portid, svc, rule in findings:
    lines.append(f"| `{ip}` | `{portid}/tcp` | {svc} | **{rule['cvss']}** | {rule['title']} |")

lines.append("\n## 2. Detailed Findings & Remediation Plan")
for i, (ip, portid, svc, rule) in enumerate(findings, 1):
    lines.extend([
        f"### {i}. {rule['title']} (`{ip}:{portid}`)",
        f"- **Severity:** {rule['cvss']}",
        f"- **Vector:** `{rule['vector']}`",
        f"- **Service:** `{svc}`",
        f"- **Remediation:** {rule['remediation']}\n"
    ])

with open("reports/VAPT-Assessment-Report.md", "w") as f:
    f.write("\n".join(lines))

print("[+] Report generated successfully!")

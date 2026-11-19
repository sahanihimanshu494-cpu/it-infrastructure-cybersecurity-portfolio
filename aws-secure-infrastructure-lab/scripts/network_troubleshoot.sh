#!/bin/bash
# Automated Network & Cloud Endpoint Diagnostics Script
# Author: Himanshu Sahani

echo "============================================================"
echo "  AWS & NETWORK INFRASTRUCTURE DIAGNOSTIC REPORT"
echo "  Timestamp: $(date)"
echo "============================================================"

echo -e "\n[1] Active Network Interfaces & IP Configuration:"
ip -brief addr show

echo -e "\n[2] Default Gateway & Routing Table:"
ip route show | head -n 5

echo -e "\n[3] DNS Resolution Verification:"
getent hosts github.com || echo "DNS check fallback triggered"

echo -e "\n[4] LocalStack Cloud Gateway & Service Health (Port 4566):"
curl -s http://localhost:4566/_localstack/health | grep -oE '"(ec2|iam|s3|sns)": "[^"]+"'

echo -e "\n[5] Deployed AWS VPC & EC2 Endpoint Audit:"
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test AWS_DEFAULT_REGION=ap-south-1 \
aws --endpoint-url=http://localhost:4566 ec2 describe-security-groups \
--query "SecurityGroups[*].{GroupId:GroupId,GroupName:GroupName,VpcId:VpcId}" --output table

echo -e "\n[✓] Diagnostic & Security Audit Completed Successfully."

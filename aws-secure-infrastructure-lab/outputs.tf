output "vpc_id" {
  description = "Deployed Custom VPC ID"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "Public Subnet ID"
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "Private Subnet ID"
  value       = aws_subnet.private.id
}

output "ec2_instance_id" {
  description = "Hardened EC2 Instance ID"
  value       = aws_instance.app_server.id
}

output "security_group_id" {
  description = "Hardened Security Group ID"
  value       = aws_security_group.web_sg.id
}

output "sns_security_topic_arn" {
  description = "SNS Security Alert Topic ARN"
  value       = aws_sns_topic.security_alerts.arn
}

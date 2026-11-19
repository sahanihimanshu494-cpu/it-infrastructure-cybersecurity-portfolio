variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-south-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the custom enterprise VPC"
  type        = string
  default     = "162.168.0.0/16"
}

variable "public_subnet_cidr" {
  description = "Public subnet CIDR block"
  type        = string
  default     = "162.168.1.0/24"
}

variable "private_subnet_cidr" {
  description = "Private subnet CIDR block"
  type        = string
  default     = "162.168.2.0/24"
}

variable "project_name" {
  description = "Project tag prefix"
  type        = string
  default     = "himanshu-secure-vpc"
}

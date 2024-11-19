variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "secret_name" {
  description = "Name of the existing secret in Secrets Manager to read"
  type        = string
}

variable "function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "lambda-secret-string"
}

variable "runtime" {
  description = "Runtime for Lambda function"
  type        = string
  default     = "python3.9"
}

variable "vpc_id" {
  description = "VPC ID where the Lambda will be deployed"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs where the Lambda will be deployed"
  type        = list(string)
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
} 
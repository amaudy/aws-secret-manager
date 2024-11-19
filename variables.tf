variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "secret_value" {
  description = "The secret value to store in Secrets Manager"
  type        = string
  default     = "thisissecret"
  sensitive   = true
} 
output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = module.lambda_secret_reader.lambda_function_arn
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = module.lambda_secret_reader.lambda_function_name
}

output "role_arn" {
  description = "The ARN of the Lambda IAM role"
  value       = module.lambda_secret_reader.role_arn
} 
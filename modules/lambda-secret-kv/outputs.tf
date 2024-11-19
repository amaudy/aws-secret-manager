output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.secret_kv_reader.arn
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.secret_kv_reader.function_name
}

output "role_arn" {
  description = "The ARN of the Lambda IAM role"
  value       = aws_iam_role.lambda_role.arn
} 
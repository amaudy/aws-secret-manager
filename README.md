# AWS Secrets Manager Utility

This utility provides a simple interface to interact with AWS Secrets Manager, allowing you to retrieve and list secrets stored in your AWS account.

## Prerequisites

1. Python 3.6 or higher
2. AWS credentials configured (either through AWS CLI or environment variables)
3. Required Python packages:
   ```bash
   pip install boto3
   ```

## AWS Credentials Setup

Before using the script, ensure you have AWS credentials configured using one of these methods:

1. AWS CLI (recommended):
   ```bash
   aws configure
   ```

2. Environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID="your_access_key"
   export AWS_SECRET_ACCESS_KEY="your_secret_key"
   export AWS_DEFAULT_REGION="us-east-1"
   ```

3. AWS credentials file (`~/.aws/credentials`):
   ```ini
   [default]
   aws_access_key_id = your_access_key
   aws_secret_access_key = your_secret_key
   ```

## Required IAM Permissions

Ensure your AWS user/role has the following permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
                "secretsmanager:ListSecrets"
            ],
            "Resource": "*"
        }
    ]
}
```

## Usage

### Creating Secrets

1. Create a simple secret:
   ```bash
   aws secretsmanager create-secret \
       --name "your/secret/path" \
       --secret-string "your-secret-value" \
       --region your-region
   ```

2. Create a key-value secret:
   ```bash
   aws secretsmanager create-secret \
       --name "your/secret/path" \
       --description "Secret description" \
       --secret-string "{\"key\":\"value\"}" \
       --region your-region
   ```

### Using the Python Script

1. Retrieve a specific secret:
   ```bash
   python secrets_manager_test.py --secret-name your-secret-name
   ```

2. List all available secrets:
   ```bash
   python secrets_manager_test.py --list
   ```

3. Use a different AWS region:
   ```bash
   python secrets_manager_test.py --secret-name your-secret-name --region us-west-2
   ```

4. Enable debug logging:
   ```bash
   python secrets_manager_test.py --secret-name your-secret-name --debug
   ```

## Example Output

### Retrieving a Secret
```bash
$ python secrets_manager_test.py --secret-name example-secret

Secret retrieved successfully!
Secret contents:
{
  "username": "example-user",
  "host": "example-host"
}
```

### Listing Secrets
```bash
$ python secrets_manager_test.py --list

Available secrets:
- example/secret/1
- example/secret/2
```

## Security Considerations

1. Never commit AWS credentials to version control
2. Be cautious when printing secrets in production environments
3. Consider using more restrictive IAM policies in production
4. Rotate your AWS credentials regularly
5. Use appropriate secret naming conventions for better organization

## Troubleshooting

1. **AWS Credentials Error**:
   - Verify AWS credentials are properly configured
   - Check IAM permissions
   - Ensure the correct region is specified

2. **Secret Not Found**:
   - Verify the secret name is correct
   - Check if the secret exists in the specified region
   - Use the `--list` option to see available secrets

3. **Permission Denied**:
   - Review IAM policy
   - Ensure the policy is attached to your user/role
   - Check if you have the necessary permissions

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
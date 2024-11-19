import json
import boto3
import argparse
import logging
from botocore.exceptions import ClientError
from typing import Optional, Dict, Any

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SecretsManagerClient:
    def __init__(self, region_name: str = "us-east-1"):
        """
        Initialize SecretsManager client
        
        Args:
            region_name (str): AWS region name
        """
        self.session = boto3.session.Session()
        self.client = self.session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

    def get_secret(self, secret_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a secret from AWS Secrets Manager
        
        Args:
            secret_name (str): Name of the secret to retrieve
        
        Returns:
            Optional[Dict]: Retrieved secret value or None if binary
        """
        try:
            logger.info(f"Attempting to retrieve secret: {secret_name}")
            response = self.client.get_secret_value(SecretId=secret_name)
            
            if 'SecretString' in response:
                try:
                    return json.loads(response['SecretString'])
                except json.JSONDecodeError:
                    # Handle non-JSON string secrets
                    return {"value": response['SecretString']}
            else:
                logger.warning("Binary secret detected - not supported")
                return None
                
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            
            if error_code == 'DecryptionFailureException':
                logger.error("Decryption failed - check KMS permissions")
            elif error_code == 'InternalServiceErrorException':
                logger.error("Internal service error")
            elif error_code == 'InvalidParameterException':
                logger.error("Invalid parameter provided")
            elif error_code == 'InvalidRequestException':
                logger.error("Invalid request")
            elif error_code == 'ResourceNotFoundException':
                logger.error(f"Secret {secret_name} not found")
            else:
                logger.error(f"Unknown error: {error_code}")
                
            logger.error(f"Error details: {error_message}")
            raise

    def list_secrets(self) -> list:
        """
        List all available secrets in the account
        
        Returns:
            list: List of secret names
        """
        try:
            response = self.client.list_secrets()
            return [secret['Name'] for secret in response['SecretList']]
        except ClientError as e:
            logger.error(f"Failed to list secrets: {str(e)}")
            raise

def main():
    parser = argparse.ArgumentParser(description='AWS Secrets Manager Utility')
    parser.add_argument('--secret-name', help='Name of the secret to retrieve')
    parser.add_argument('--region', default='us-east-1', help='AWS region (default: us-east-1)')
    parser.add_argument('--list', action='store_true', help='List all available secrets')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    try:
        client = SecretsManagerClient(args.region)
        
        if args.list:
            secrets = client.list_secrets()
            print("\nAvailable secrets:")
            for secret in secrets:
                print(f"- {secret}")
            return

        if not args.secret_name:
            parser.error("Either --secret-name or --list is required")

        secret = client.get_secret(args.secret_name)
        
        if secret:
            print("\nSecret retrieved successfully!")
            print("Secret contents:")
            print(json.dumps(secret, indent=2))
        
    except Exception as e:
        logger.error(f"Operation failed: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main() 
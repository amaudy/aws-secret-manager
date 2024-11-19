import json
import boto3
import logging

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Starting Lambda execution")
    
    try:
        # Create a Secrets Manager client
        logger.info("Creating Secrets Manager client")
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager'
        )
        
        # Get the secret value
        secret_name = 'foobar/rds/password'
        logger.info(f"Attempting to retrieve secret: {secret_name}")
        
        secret_response = client.get_secret_value(
            SecretId=secret_name
        )
        
        # Get the secret string
        secret_value = secret_response['SecretString']
        logger.info("Successfully retrieved secret")
        logger.info(f"Secret value: {secret_value}")
        
        return {
            'statusCode': 200,
            'body': 'Secret successfully retrieved and logged'
        }
        
    except Exception as e:
        logger.error(f"Error retrieving secret: {str(e)}")
        logger.error(f"Error type: {type(e).__name__}")
        raise e 
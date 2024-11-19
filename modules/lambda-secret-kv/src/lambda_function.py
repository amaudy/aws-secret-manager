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
        secret_name = 'foobar/rds/kv/password'
        logger.info(f"Attempting to retrieve secret: {secret_name}")
        
        secret_response = client.get_secret_value(
            SecretId=secret_name
        )
        
        # Get and parse the secret JSON string
        secret_string = secret_response['SecretString']
        secret_dict = json.loads(secret_string)
        password = secret_dict.get('password')
        
        logger.info("Successfully retrieved and parsed secret")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'secret_name': secret_name,
                'password': password
            })
        }
        
    except Exception as e:
        logger.error(f"Error retrieving secret: {str(e)}")
        logger.error(f"Error type: {type(e).__name__}")
        raise e 
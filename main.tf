provider "aws" {
  region = "us-east-1"
}

# Original Lambda for reading simple secrets
module "lambda_secret_reader" {
  source = "./modules/lambda-secret-reader"
  
  secret_name   = "foobar/rds/password"
  function_name = "secret-reader-lambda"
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnet_ids
  
  tags = {
    Environment = "production"
    Project     = "secret-reader"
  }
}

# New Lambda for reading KV secrets
module "lambda_secret_kv" {
  source = "./modules/lambda-secret-kv"
  
  secret_name   = "foobar/rds/kv/password"
  function_name = "secret-kv-reader"
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnet_ids
  
  tags = {
    Environment = "production"
    Project     = "secret-kv-reader"
  }
}

module "vpc" {
  source = "./modules/vpc"
}

# Updated outputs to include both Lambda functions
output "vpc_details" {
  value = {
    vpc_id          = module.vpc.vpc_id
    public_subnets  = module.vpc.public_subnet_ids
    private_subnets = module.vpc.private_subnet_ids
  }
}

output "lambda_functions" {
  value = {
    simple_secret_reader = {
      function_name = module.lambda_secret_reader.lambda_function_name
      function_arn  = module.lambda_secret_reader.lambda_function_arn
    }
    kv_secret_reader = {
      function_name = module.lambda_secret_kv.lambda_function_name
      function_arn  = module.lambda_secret_kv.lambda_function_arn
    }
  }
} 
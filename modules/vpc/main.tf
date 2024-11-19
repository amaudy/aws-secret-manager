# Query the default VPC
data "aws_vpc" "default" {
  default = true
}

# Query all subnets in the default VPC
data "aws_subnets" "all" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# Query public subnets (those with route to internet gateway)
data "aws_subnet" "public" {
  for_each = toset(data.aws_subnets.all.ids)
  id       = each.value
}

locals {
  # All subnets in default VPC are typically public
  public_subnet_ids  = [for subnet in data.aws_subnet.public : subnet.id]
  private_subnet_ids = []  # Default VPC typically has no private subnets
} 
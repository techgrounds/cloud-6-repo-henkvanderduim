import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class VpcsStack(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        vpcs_environment = environments.get("vpcs")
        mngt_name = vpcs_environment.get("mngt_name")
        mngt_cidr_block = vpcs_environment.get("mngt_cidr_block")
        mngt_cidr_mask = vpcs_environment.get("mngt_cidr_mask")
        mngt_subnet_name = vpcs_environment.get("mngt_subnet_name")
        mngt_max_azs = vpcs_environment.get("mngt_max_azs")

        asg_name = vpcs_environment.get("asg_name")
        asg_cidr_block = vpcs_environment.get("asg_cidr_block")
        asg_cidr_mask = vpcs_environment.get("asg_cidr_mask")
        public_asg_subnet_name = vpcs_environment.get("public_asg_subnet_name")
        private_asg_subnet_name = vpcs_environment.get("private_asg_subnet_name")
        asg_max_azs = vpcs_environment.get("asg_max_azs")

        ### VPC - Management VPC

        self.vpc1 = ec2.Vpc(
            self,
            mngt_name,
            max_azs=mngt_max_azs,
            cidr=mngt_cidr_block,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=mngt_subnet_name,
                    cidr_mask=mngt_cidr_mask,
                )
            ],
        )

        ### VPC - Autoscaling

        self.vpc2 = ec2.Vpc(
            self,
            asg_name,
            nat_gateway_subnets=ec2.SubnetSelection(
                subnet_group_name=public_asg_subnet_name
            ),
            max_azs=asg_max_azs,
            cidr=asg_cidr_block,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=public_asg_subnet_name,
                    cidr_mask=asg_cidr_mask,
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    name=private_asg_subnet_name,
                    cidr_mask=asg_cidr_mask,
                ),
            ],
        )

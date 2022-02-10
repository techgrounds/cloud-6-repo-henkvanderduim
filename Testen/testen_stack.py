from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct


class TestenStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        self.vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=2,
            cidr="10.10.0.0/24",
            # configuration will create 3 groups in 2 AZs = 6 subnets.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC, name="Public", cidr_mask=32
                )
            ],
            # nat_gateway_provider=ec2.NatProvider.gateway(),
            # nat_gateways=2,
        )
        CfnOutput(self, "Output", value=self.vpc.vpc_id)

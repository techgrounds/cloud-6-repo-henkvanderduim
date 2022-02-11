from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct

class TestenStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        self.vpc = ec2.Vpc(self, "VPC1",
                           max_azs=2,
                           cidr="10.10.10.0/24",
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public1",
                               cidr_mask=25
                           )
                           ]
                           )

        self.vpc = ec2.Vpc(self, "VPC2",
                           max_azs=2,
                           cidr="10.20.20.0/24",
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public2",
                               cidr_mask=25
                           )
                           ]
                           )
        CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)
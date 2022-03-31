import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_ssm as ssm,
)


class RolesStack(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        roles_environment = environments.get("roles")
        iam_ssm_role = roles_environment.get("iam_ssm_role")
        iam_ssm_principal = roles_environment.get("iam_ssm_principal")

        #################### Create Roles & Policies ####################

        ### Role SSM

        self.role = iam.Role(
            self, iam_ssm_role, assumed_by=iam.ServicePrincipal(iam_ssm_principal)
        )
        self.role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

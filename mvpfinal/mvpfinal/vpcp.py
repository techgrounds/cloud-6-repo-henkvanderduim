import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class VpcpStack(cdk.NestedStack):
    def __init__(
        self, scope: Construct, id: str, vpc1: ec2.Vpc, vpc2: ec2.Vpc, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        vpcs_environment = environments.get("vpcs")
        vpcp_name = vpcs_environment.get("vpcp_name")
        vpcp_region = vpcs_environment.get("vpcp_region")
        vpcp_r1name = vpcs_environment.get("vpcp_r1name")
        vpcp_r2name = vpcs_environment.get("vpcp_r2name")
        vpcp_r3name = vpcs_environment.get("vpcp_r3name")

        ### VPC Peering

        self.VPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self,
            vpcp_name,
            peer_vpc_id=vpc1.vpc_id,
            vpc_id=vpc2.vpc_id,
            # Peering Region (optional)
            peer_region=vpcp_region,
        )

        ### VPC Peering Connection

        for i in range(0, 2):
            ec2.CfnRoute(
                self,
                vpcp_r1name + str(i),
                route_table_id=vpc1.public_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc2.vpc_cidr_block,
                vpc_peering_connection_id=self.VPCPeering_connection.ref,
            )

        for i in range(0, 2):
            ec2.CfnRoute(
                self,
                vpcp_r2name + str(i),
                route_table_id=vpc2.public_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc1.vpc_cidr_block,
                vpc_peering_connection_id=self.VPCPeering_connection.ref,
            )

        for i in range(0, 2):
            ec2.CfnRoute(
                self,
                vpcp_r3name + str(i),
                route_table_id=vpc2.private_subnets[i].route_table.route_table_id,
                destination_cidr_block=vpc1.vpc_cidr_block,
                vpc_peering_connection_id=self.VPCPeering_connection.ref,
            )

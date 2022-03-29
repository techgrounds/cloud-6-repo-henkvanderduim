import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)


class SgStack(cdk.NestedStack):
    def __init__(
        self, scope: Construct, id: str, vpc1: ec2.Vpc, vpc2: ec2.Vpc, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        sgs_environment = environments.get("sgs")
        mngt_sg_name = sgs_environment.get("mngt_sg_name")
        mngt_sg_description = sgs_environment.get("mngt_sg_description")
        mngt_sg_allow_all_outbound = sgs_environment.get("mngt_sg_allow_all_outbound")
        mngt_trusted_ip_ssh = sgs_environment.get("mngt_trusted_ip_ssh")
        mngt_trusted_ip_rdp = sgs_environment.get("mngt_trusted_ip_rdp")
        mngt_sg_ssh_rule_port = sgs_environment.get("mngt_sg_ssh_rule_port")
        mngt_sg_rdp_rule_port = sgs_environment.get("mngt_sg_rdp_rule_port")

        asgsg_name = sgs_environment.get("asgsg_name")
        asgsg_description = sgs_environment.get("asgsg_description")
        asgsg_allow_all_outbound = sgs_environment.get("asgsg_allow_all_outbound")
        asgsg_rule_port = sgs_environment.get("asgsg_rule_port")
        asgsg_http_rule_port = sgs_environment.get("asgsg_http_rule_port")
        asgsg_https_rule_port = sgs_environment.get("asgsg_https_rule_port")

        elbsg_name = sgs_environment.get("elbsg_name")
        elbsg_description = sgs_environment.get("elbsg_description")
        elbsg_allow_all_outbound = sgs_environment.get("elbsg_allow_all_outbound")
        elbsg_http_rule_port = sgs_environment.get("elbsg_http_rule_port")
        elbsg_https_rule_port = sgs_environment.get("elbsg_https_rule_port")

        ### Security Group Management Server
        mngtsg = ec2.SecurityGroup(
            self,
            mngt_sg_name,
            vpc=self.vpc1,
            description=mngt_sg_description,
            allow_all_outbound=mngt_sg_allow_all_outbound,
        )
        iplistssh = mngt_trusted_ip_ssh
        for i in range(len(iplistssh)):
            mngtsg.add_ingress_rule(
                ec2.Peer.ipv4(iplistssh[i] + "/32"),
                ec2.Port.tcp(mngt_sg_ssh_rule_port),
                "allow ssh access from the VPC",
            )

        iplistrdp = mngt_trusted_ip_rdp
        for i in range(len(iplistrdp)):
            mngtsg.add_ingress_rule(
                ec2.Peer.ipv4(iplistrdp[i] + "/32"),
                ec2.Port.tcp(mngt_sg_rdp_rule_port),
                "allow RDP access from the VPC",
            )

        ### Security Group ELB
        elbsg = ec2.SecurityGroup(
            self,
            elbsg_name,
            vpc=self.vpc2,
            description=elbsg_description,
            allow_all_outbound=elbsg_allow_all_outbound,
        )

        elbsg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(elbsg_http_rule_port),
            "allow HTTP traffic from anywhere",
        )

        elbsg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(elbsg_https_rule_port),
            "allow HTTPS traffic from anywhere",
        )

        ### Security Group ASG
        asgsg = ec2.SecurityGroup(
            self,
            asgsg_name,
            vpc=self.vpc2,
            description=asgsg_description,
            allow_all_outbound=asgsg_allow_all_outbound,
        )

        asgsg.add_ingress_rule(
            ec2.Peer.security_group_id(mngtsg.security_group_id),
            ec2.Port.tcp(asgsg_rule_port),
            "allow access from the MNGT Security Group",
        )

        asgsg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(asgsg_http_rule_port),
            "allow HTTP traffic from anywhere",
        )

        asgsg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(asgsg_https_rule_port),
            "allow HTTPS traffic from anywhere",
        )

# de benodigde zaken importeren
import os.path
import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as bk,
    aws_events as event,
    aws_s3 as s3,
    CfnOutput,
    App,
    Stack,
    Tags,
)

from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_s3_assets import Asset


# directory variabele
dirname = os.path.dirname(__file__)

# Stack
class MvpscriptsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # De code die de stack definieert is hieronder te vinden

        ####################### VPC's aanmaken #############################

        # VPC 1 - Management VPC

        self.vpc1 = ec2.Vpc(
            self,
            "management-prd-vpc",
            max_azs=2,
            cidr="10.10.10.0/24",
            # configureren van 1 subnet in elke AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public Subnet",
                    cidr_mask=25,
                )
            ],
        )

        # VPC 2 - Webserver VPC

        self.vpc2 = ec2.Vpc(
            self,
            "app-prd-vpc",
            max_azs=2,
            cidr="10.20.20.0/24",
            # configureren van 1 subnet in elke AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public Subnet",
                    cidr_mask=25,
                )
            ],
        )

        # VPC Peering aanzetten

        self.cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self,
            "VPCPeeringConnection-prd",
            peer_vpc_id=self.vpc1.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            # Peering Regio (optioneel)
            peer_region="eu-central-1",
        )

        ####################### AMI's aanmaken #############################

        # AMI Linux
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        # AMI Windows
        amzn_windows = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
        )

        # Rol

        role = iam.Role(
            self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        # S3 bucket maken
        bucket = s3.Bucket(
            self,
            "BootstrapScriptBucket",
            versioned=True,
            encryption=s3.BucketEncryption.KMS,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Security Group Management Server
        mngtsg = ec2.SecurityGroup(
            self,
            "ManagementSecurityGroup",
            vpc=self.vpc1,
            description="Management Security Group",
            allow_all_outbound=True,
        )
        mngtsg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow ssh access from the VPC"
        )

        mngtsg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(3389), "allow ssh access from the VPC"
        )

        # key pair
        key = KeyPair(
            self,
            "KeyPair",
            name="MijnKeyPair",
            description="MijnKeyPair",
            store_public_key=True,
        )

        key.grant_read_on_private_key(role)
        key.grant_read_on_public_key(role)

        # Instance Management Server (Windows)
        management_server = ec2.Instance(
            self,
            "Management Server",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_windows,
            vpc=self.vpc1,
            security_group=mngtsg,
            key_name=key.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=True),
                )
            ],
        )

        # Security Group Web Server
        wssg = ec2.SecurityGroup(
            self,
            "ProductionSecurityGroup",
            vpc=self.vpc2,
            description="Production Security Group",
            allow_all_outbound=True,
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow ssh access from the VPC"
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "allow HTTP traffic from anywhere",
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "allow HTTPS traffic from anywhere"
        )

        # Instance Web Server
        web_server = ec2.Instance(
            self,
            "Web Server",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=amzn_linux,
            vpc=self.vpc2,
            security_group=wssg,
            key_name=key.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(8, encrypted=True),
                )
            ],
        )

        # Tags
        Tags.of(web_server).add("PRD", "WSBackup")
        Tags.of(management_server).add("MNGT", "MSBackup")

        ##################### BACKUP ############################# 

        
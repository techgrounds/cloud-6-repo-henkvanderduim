'''''
PRD-01 Cloud6.Sentia1

Project: MVP v1.0

Ingredients:
- 1 Region
- 2 VPC's with each 2 AZ's

VPC MANAGEMENT-PRD-VPC                    | VPC APP-PRD-VPC
- 2 public subnets (10.10.10.0/24)        | - 2 PUBLIC SUBNETS (10.20.20.0/24)
- 1 EC2 instance (windows server)         | - 1 EC2 instance (linux) with website
- 1 Management Security Group             | - 1 Production Security Group
- Backup 1x a week (1 saved    )          | - daily backup (7 rounds saved)

S3 Bucket for Bootstrap Scripts

VPC Peering Connection
'''''
### Importing the necessary libraries

import os.path
from urllib import response
import aws_cdk as cdk
from aws_cdk import (
    Duration,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
    aws_events as event,
    aws_kms as kms,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_ssm as ssm,
    RemovalPolicy,
    CfnOutput,
    App,
    Stack,
    Tags,
)

from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_events import Schedule
from aws_cdk.aws_s3_assets import Asset


### directory variable
dirname = os.path.dirname(__file__)


#################### STACK ####################


class MvpscriptStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        

        #################### Create 2 VPCs + VPC Peering ####################

        ### VPC 1 - Management VPC

        self.vpc1 = ec2.Vpc(
            self,
            "management-prd-vpc",
            max_azs=2,
            cidr="10.10.10.0/24",
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=25,
                )
            ],
        )

        ### VPC 2 - Webserver VPC

        self.vpc2 = ec2.Vpc(
            self,
            "app-prd-vpc",
            max_azs=2,
            cidr="10.20.20.0/24",
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=25,
                )
            ],
        )

        ### VPC Peering

        self.cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self,
            "VPCPeeringConnection-prd",
            peer_vpc_id=self.vpc1.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            # Peering Region (optional)
            peer_region="eu-central-1",
        )

        ### VPC Peering Connection between VPC1-VPC2 through Route-table
        self.cfn_Route = ec2.CfnRoute(
            self,
            "VPC1-route",
            route_table_id=self.vpc1.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=self.vpc2.vpc_cidr_block,
            vpc_peering_connection_id=self.cfn_vPCPeering_connection.ref,
        )

        ### VPC Peering Connection between VPC2-VPC1 through Route-table
        self.cfn_Route = ec2.CfnRoute(
            self,
            "VPC2-route",
            route_table_id=self.vpc2.public_subnets[0].route_table.route_table_id,
            destination_cidr_block=self.vpc1.vpc_cidr_block,
            vpc_peering_connection_id=self.cfn_vPCPeering_connection.ref,
        )

        #################### Create AMI's ####################

        ### AMI Linux
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        ### AMI Windows
        amzn_windows = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
        )

        #################### Create Roles & Policies ####################

        ### Role SSM

        role = iam.Role(
            self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )

        #################### Create S3 Bucket ####################

        ### S3 bucket
        bootstrapbucket = s3.Bucket(
            self,
            "BootstrapScriptBucket",
            versioned=True,
            encryption=s3.BucketEncryption.KMS,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        
        ### Put file in the bucket
        s3deploy.BucketDeployment(
            self, "S3Deployment",
            sources=[s3deploy.Source.asset("./bucket")],
            destination_bucket=bootstrapbucket,
        )
        
        #################### Create Security Groups ####################

        ### Security Group Management Server
        mngtsg = ec2.SecurityGroup(
            self,
            "ManagementSecurityGroup",
            vpc=self.vpc1,
            description="Management Security Group",
            allow_all_outbound=True,
        )
        mngtsg.add_ingress_rule(
            ec2.Peer.ipv4("84.84.84.9/32"),
            ec2.Port.tcp(22),
            "allow ssh access from the VPC",
        )

        mngtsg.add_ingress_rule(
            ec2.Peer.ipv4("84.84.84.9/32"),
            ec2.Port.tcp(3389),
            "allow RDP access from the VPC",
        )

        ### Security Group Web Server
        wssg = ec2.SecurityGroup(
            self,
            "ProductionSecurityGroup",
            vpc=self.vpc2,
            description="Production Security Group",
            allow_all_outbound=True,
        )

        wssg.add_ingress_rule(
            ec2.Peer.security_group_id(mngtsg.security_group_id),
            ec2.Port.tcp(22),
            "allow ssh access from the management Security Group",
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "allow HTTP traffic from anywhere"
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "allow HTTPS traffic from anywhere"
        )

        #################### Create Key Pair ####################

        ### key pair
        key = KeyPair(
            self,
            "KeyPair",
            name="MijnKeyPair",
            description="MijnKeyPair",
            store_public_key=True,
        )

        key.grant_read_on_private_key(role)
        key.grant_read_on_public_key(role)

        #################### Create EC2 Instances ####################

        ### Instance Management Server (Windows)
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
        
            
        ### Instance Web Server
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
        
        assets = Asset(self, "Asset",
              path="./bucket/webserver.sh"
        )
        
        Local_path = web_server.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region="eu-central-1",
        )

        web_server.user_data.add_execute_file_command(
            file_path=Local_path
        )

        assets.grant_read(web_server.role)

        #################### Create Tags ####################

        ### Tags
        Tags.of(web_server).add("PRD", "WSBackup")
        Tags.of(management_server).add("MNGT", "MSBackup")

        ##################### Create Backup Routines #############################

        ### Backup Webserver
        ### Create Backup Vault
        key = kms.Key(self, "PRD-BACKUP-KEY", removal_policy=RemovalPolicy.DESTROY)
        vault = backup.BackupVault(
            self, "BackupVault1", backup_vault_name="PRD-VAULT", encryption_key=key
        )

        ### Create Backup Plan
        plan = backup.BackupPlan(
            self, "PRD-BACKUP-PLAN", backup_plan_name="PRD-BACKUP-PLAN"
        )

        ### Add Backup Resources through Tags
        plan.add_selection(
            "Selection",
            resources=[backup.BackupResource.from_tag("PRD", "WSBackup")],
        )

        ### Create Backup Rule - Each day at 4:30 hrs and keep for 7 days
        plan.add_rule(
            backup.BackupPlanRule(
                backup_vault=vault,
                rule_name="PRD_Backup_Rule",
                schedule_expression=Schedule.cron(
                    minute="30",
                    hour="4",
                    month="1-12",
                    day="1",
                ),
                delete_after=Duration.days(7),
            )
        )

        ### Backup Management Server
        ### Create Backup Vault
        key = kms.Key(self, "MNGT-BACKUP-KEY", removal_policy=RemovalPolicy.DESTROY)
        vault = backup.BackupVault(
            self, "BackupVault2", backup_vault_name="MNGT-VAULT", encryption_key=key
        )

        ### Create Backup Plan
        plan = backup.BackupPlan(
            self, "MNGT-BACKUP-PLAN", backup_plan_name="MNGT-BACKUP-PLAN"
        )

        ### Add Backup Resources through Tags
        plan.add_selection(
            "Selection",
            resources=[backup.BackupResource.from_tag("MNGT", "WSBackup")],
        )

        ### Create Backup Rule - Once a week and save 1
        plan.add_rule(
            backup.BackupPlanRule(
                backup_vault=vault,
                rule_name="MNGT_Backup_Rule",
                schedule_expression=Schedule.cron(
                    minute="0",
                    hour="0",
                    month="1-12",
                    day="4",
                ),
                delete_after=Duration.days(13),
            )
        )
"""''
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
""" ""
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

        #################### Parameter Setup ####################

        # VPCs
        environments = self.node.try_get_context("ENVIRONMENTS")
        vpcs_environment = environments.get("vpcs")
        mngt_name = vpcs_environment.get("mngt_name")
        mngt_cidr_block = vpcs_environment.get("mngt_cidr_block")
        mngt_cidr_mask = vpcs_environment.get("mngt_cidr_mask")
        mngt_subnet_name = vpcs_environment.get("mngt_subnet_name")
        mngt_max_azs = vpcs_environment.get("mngt_max_azs")

        wsrv_name = vpcs_environment.get("wsrv_name")
        wsrv_cidr_block = vpcs_environment.get("wsrv_cidr_block")
        wsrv_cidr_mask = vpcs_environment.get("wsrv_cidr_mask")
        wsrv_subnet_name = vpcs_environment.get("wsrv_subnet_name")
        wsrv_max_azs = vpcs_environment.get("wsrv_max_azs")

        vpcp_name = vpcs_environment.get("vpcp_name")
        vpcp_region = vpcs_environment.get("vpcp_region")
        mngt_vpcp_route = vpcs_environment.get("mngt_vpcp_route")
        wsrv_vpcp_route = vpcs_environment.get("wsrv_vpcp_route")

        # Roles
        roles_environment = environments.get("roles")
        iam_ssm_role = roles_environment.get("iam_ssm_role")
        iam_ssm_principal = roles_environment.get("iam_ssm_principal")

        # Bucket
        bucket_environment = environments.get("bucket")
        bucket_name = bucket_environment.get("bucket_name")
        versioned = bucket_environment.get("versioned")
        auto_delete_objects = bucket_environment.get("auto_delete_objects")
        # deploy_name = bucket_environment.get("deploy_name")
        # source = bucket_environment.get("source")

        # SGs
        sgs_environment = environments.get("sgs")
        mngt_sg_name = sgs_environment.get("mngt_sg_name")
        mngt_sg_description = sgs_environment.get("mngt_sg_description")
        mngt_sg_allow_all_outbound = sgs_environment.get("mngt_sg_allow_all_outbound")
        mngt_sg_ssh_rule_ip = sgs_environment.get("mngt_sg_ssh_rule_ip")
        mngt_sg_ssh_rule_port = sgs_environment.get("mngt_sg_ssh_rule_port")
        mngt_sg_rdp_rule_ip = sgs_environment.get("mngt_sg_rdp_rule_ip")
        mngt_sg_rdp_rule_port = sgs_environment.get("mngt_sg_rdp_rule_port")

        wsrv_sg_name = sgs_environment.get("wsrv_sg_name")
        wsrv_sg_description = sgs_environment.get("wsrv_sg_description")
        wsrv_sg_allow_all_outbound = sgs_environment.get("wsrv_sg_allow_all_outbound")
        wsrv_sg_rule_port = sgs_environment.get("wsrv_sg_rule_port")
        wsrv_sg_http_rule_port = sgs_environment.get("wsrv_sg_http_rule_port")
        wsrv_sg_https_rule_port = sgs_environment.get("wsrv_sg_https_rule_port")

        # Key Pair
        keypair_environment = environments.get("keypair")
        mngt_kp = keypair_environment.get("mngt_kp")
        mngt_kp_name = keypair_environment.get("mngt_kp_name")
        mngt_kp_description = keypair_environment.get("mngt_kp_description")
        mngt_kp_store = keypair_environment.get("mngt_kp_store")

        wsrv_kp = keypair_environment.get("wsrv_kp")
        wsrv_kp_name = keypair_environment.get("wsrv_kp_name")
        wsrv_kp_description = keypair_environment.get("wsrv_kp_description")
        wsrv_kp_store = keypair_environment.get("wsrv_kp_store")

        # EC2s
        ec2s_environment = environments.get("ec2s")
        mngt_ec2_name = ec2s_environment.get("mngt_ec2_name")
        mngt_ec2_instance_type = ec2s_environment.get("mngt_ec2_instance_type")
        mngt_ec2_encrypted = ec2s_environment.get("mngt_ec2_encrypted")

        wsrv_ec2_name = ec2s_environment.get("wsrv_ec2_name")
        wsrv_ec2_instance_type = ec2s_environment.get("wsrv_ec2_instance_type")
        wsrv_ec2_encrypted = ec2s_environment.get("wsrv_ec2_encrypted")

        # Server Script
        webscript_environment = environments.get("webscript")
        wsrv_asset_name = webscript_environment.get("wsrv_asset_name")
        wsrv_asset_path = webscript_environment.get("wsrv_asset_path")
        wsrv_asset_region = webscript_environment.get("wsrv_asset_region")

        # Tags
        tags_environment = environments.get("tags")
        mngt_tag_key = tags_environment.get("mngt_tag_key")
        mngt_tag_value = tags_environment.get("mngt_tag_value")
        wsrv_tag_key = tags_environment.get("wsrv_tag_key")
        wsrv_tag_value = tags_environment.get("wsrv_tag_value")

        # Backup Vaults/Plans/Rules
        bus_environment = environments.get("bus")
        mngt_vault_key = bus_environment.get("mngt_vault_key")
        mngt_vault_name = bus_environment.get("mngt_vault_name")
        mngt_backup_vault_name = bus_environment.get("mngt_backup_vault_name")
        mngt_backup_plan = bus_environment.get("mngt_backup_plan")
        mngt_backup_plan_name = bus_environment.get("mngt_backup_plan_name")
        mngt_rule_name = bus_environment.get("mngt_rule_name")
        mngt_minute = bus_environment.get("mngt_minute")
        mngt_hour = bus_environment.get("mngt_hour")
        mngt_month = bus_environment.get("mngt_month")
        mngt_weekday = bus_environment.get("mngt_weekday")
        mngt_duration = bus_environment.get("mngt_duration")

        wsrv_vault_key = bus_environment.get("wsrv_vault_key")
        wsrv_vault_name = bus_environment.get("wsrv_vault_name")
        wsrv_backup_vault_name = bus_environment.get("wsrv_backup_vault_name")
        wsrv_backup_plan = bus_environment.get("wsrv_backup_plan")
        wsrv_backup_plan_name = bus_environment.get("wsrv_backup_plan_name")
        wsrv_rule_name = bus_environment.get("wsrv_rule_name")
        wsrv_minute = bus_environment.get("wsrv_minute")
        wsrv_hour = bus_environment.get("wsrv_hour")
        wsrv_month = bus_environment.get("wsrv_month")
        wsrv_weekday = bus_environment.get("wsrv_weekday")
        wsrv_duration = bus_environment.get("wsrv_duration")

        #################### Create 2 VPCs + VPC Peering ####################

        ### VPC 1 - Management VPC

        self.vpc1 = ec2.Vpc(
            self,
            mngt_name,
            max_azs=mngt_max_azs,
            cidr=mngt_cidr_block,
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=mngt_subnet_name,
                    cidr_mask=mngt_cidr_mask,
                )
            ],
        )

        ### VPC 2 - Webserver VPC

        self.vpc2 = ec2.Vpc(
            self,
            wsrv_name,
            max_azs=wsrv_max_azs,
            cidr=wsrv_cidr_block,
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=wsrv_subnet_name,
                    cidr_mask=wsrv_cidr_mask,
                )
            ],
        )

        ### VPC Peering

        self.cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self,
            vpcp_name,
            peer_vpc_id=self.vpc1.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            # Peering Region (optional)
            peer_region=vpcp_region,
        )

        ### VPC Peering Connection between VPC1-VPC2 through Route-table
        self.cfn_Route = ec2.CfnRoute(
            self,
            mngt_vpcp_route,
            route_table_id=self.vpc1.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=self.vpc2.vpc_cidr_block,
            vpc_peering_connection_id=self.cfn_vPCPeering_connection.ref,
        )

        ### VPC Peering Connection between VPC2-VPC1 through Route-table
        self.cfn_Route = ec2.CfnRoute(
            self,
            wsrv_vpcp_route,
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
            self, iam_ssm_role, assumed_by=iam.ServicePrincipal(iam_ssm_principal)
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
            bucket_name,
            versioned=versioned,
            encryption=s3.BucketEncryption.KMS,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=auto_delete_objects,
        )

        ### Put mvpscript folder in the bucket
        # s3deploy.BucketDeployment(
        #     self,
        #     deploy_name,
        #     sources=[s3deploy.Source.asset(source)],
        #     destination_bucket=bootstrapbucket,
        # )

        #################### Create Security Groups ####################

        ### Security Group Management Server
        mngtsg = ec2.SecurityGroup(
            self,
            mngt_sg_name,
            vpc=self.vpc1,
            description=mngt_sg_description,
            allow_all_outbound=mngt_sg_allow_all_outbound,
        )
        mngtsg.add_ingress_rule(
            ec2.Peer.ipv4(mngt_sg_ssh_rule_ip),
            ec2.Port.tcp(mngt_sg_ssh_rule_port),
            "allow ssh access from the VPC",
        )

        mngtsg.add_ingress_rule(
            ec2.Peer.ipv4(mngt_sg_rdp_rule_ip),
            ec2.Port.tcp(mngt_sg_rdp_rule_port),
            "allow RDP access from the VPC",
        )

        ### Security Group Web Server
        wssg = ec2.SecurityGroup(
            self,
            wsrv_sg_name,
            vpc=self.vpc2,
            description=wsrv_sg_description,
            allow_all_outbound=wsrv_sg_allow_all_outbound,
        )

        wssg.add_ingress_rule(
            ec2.Peer.security_group_id(mngtsg.security_group_id),
            ec2.Port.tcp(wsrv_sg_rule_port),
            "allow ssh access from the management Security Group",
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(wsrv_sg_http_rule_port),
            "allow HTTP traffic from anywhere",
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(wsrv_sg_https_rule_port),
            "allow HTTPS traffic from anywhere",
        )

        #################### Create Key Pair ####################

        ### key pair Mangement Server
        mngtkey = KeyPair(
            self,
            mngt_kp,
            name=mngt_kp_name,
            description=mngt_kp_description,
            store_public_key=mngt_kp_store,
        )

        mngtkey.grant_read_on_private_key(role)
        mngtkey.grant_read_on_public_key(role)

        ### key pair webserver
        wsrvkey = KeyPair(
            self,
            wsrv_kp,
            name=wsrv_kp_name,
            description=wsrv_kp_description,
            store_public_key=wsrv_kp_store,
        )

        wsrvkey.grant_read_on_private_key(role)
        wsrvkey.grant_read_on_public_key(role)

        #################### Create EC2 Instances ####################

        ### Instance Management Server (Windows)
        management_server = ec2.Instance(
            self,
            mngt_ec2_name,
            instance_type=ec2.InstanceType(mngt_ec2_instance_type),
            machine_image=amzn_windows,
            vpc=self.vpc1,
            security_group=mngtsg,
            key_name=mngtkey.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=mngt_ec2_encrypted),
                )
            ],
        )

        ### Instance Web Server
        web_server = ec2.Instance(
            self,
            wsrv_ec2_name,
            instance_type=ec2.InstanceType(wsrv_ec2_instance_type),
            machine_image=amzn_linux,
            vpc=self.vpc2,
            security_group=wssg,
            key_name=wsrvkey.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(8, encrypted=wsrv_ec2_encrypted),
                )
            ],
        )

        # Launch script to install webserver

        assets = Asset(
            self,
            wsrv_asset_name,
            path=wsrv_asset_path,
        )

        Local_path = web_server.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=wsrv_asset_region,
        )

        web_server.user_data.add_execute_file_command(file_path=Local_path)

        assets.grant_read(web_server.role)

        #################### Create Tags ####################

        ### Tags
        Tags.of(management_server).add(mngt_tag_key, mngt_tag_value)
        Tags.of(web_server).add(wsrv_tag_key, wsrv_tag_value)

        ##################### Create Backup Routines #############################

        ### Backup Management Server
        ### Create Backup Vault
        mngtvaultkey = kms.Key(
            self, mngt_vault_key, removal_policy=RemovalPolicy.DESTROY
        )
        mngtvault = backup.BackupVault(
            self,
            mngt_vault_name,
            backup_vault_name=mngt_backup_vault_name,
            encryption_key=mngtvaultkey,
        )

        ### Create Backup Plan
        mngtplan = backup.BackupPlan(
            self, mngt_backup_plan, backup_plan_name=mngt_backup_plan_name
        )

        ### Add Backup Resources through Tags
        mngtplan.add_selection(
            "Selection",
            resources=[backup.BackupResource.from_tag(mngt_tag_key, mngt_tag_value)],
        )

        ### Create Backup Rule - Each day at 4:30 hrs and keep for 7 days
        mngtplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=mngtvault,
                rule_name=mngt_rule_name,
                schedule_expression=Schedule.cron(
                    minute=mngt_minute,
                    hour=mngt_hour,
                    month=mngt_month,
                    week_day=mngt_weekday,
                ),
                delete_after=Duration.days(mngt_duration),
            )
        )

        ### Backup Webserver
        ### Create Backup Vault
        wsrvkey = kms.Key(self, wsrv_vault_key, removal_policy=RemovalPolicy.DESTROY)
        wsrvvault = backup.BackupVault(
            self,
            wsrv_vault_name,
            backup_vault_name=wsrv_backup_vault_name,
            encryption_key=wsrvkey,
        )

        ### Create Backup Plan
        wsrvplan = backup.BackupPlan(
            self, wsrv_backup_plan, backup_plan_name=wsrv_backup_plan_name
        )

        ### Add Backup Resources through Tags
        wsrvplan.add_selection(
            "Selection",
            resources=[backup.BackupResource.from_tag(wsrv_tag_key, wsrv_tag_value)],
        )

        ### Create Backup Rule - Once a week and save 1
        wsrvplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=wsrvvault,
                rule_name=wsrv_rule_name,
                schedule_expression=Schedule.cron(
                    minute=wsrv_minute,
                    hour=wsrv_hour,
                    month=wsrv_month,
                    week_day=wsrv_weekday,
                ),
                delete_after=Duration.days(wsrv_duration),
            )
        )

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
        
        #################### Parameter Setup ####################
        
        # VPCs
        environments = self.node.try_get_context("ENVIRONMENTS")
        vpcs_environment = environments.get("vpcs")
        vpc1_name = vpcs_environment.get("vpc1_name")
        vpc1_cidr_block = vpcs_environment.get("vpc1_cidr_block")
        vpc1_cidr_mask = vpcs_environment.get("vpc1_cidr_mask")
        vpc1_subnet_name = vpcs_environment.get("vpc1_subnet_name")
        vpc1_max_azs = vpcs_environment.get("vpc1_max_azs")
        
        vpc2_name = vpcs_environment.get("vpc2_name")
        vpc2_cidr_block = vpcs_environment.get("vpc2_cidr_block")
        vpc2_cidr_mask = vpcs_environment.get("vpc2_cidr_mask")
        vpc2_subnet_name = vpcs_environment.get("vpc2_subnet_name")
        vpc2_max_azs = vpcs_environment.get("vpc2_max_azs")
        
        vpcp_name = vpcs_environment.get("vpcp_name")
        vpcp_region = vpcs_environment.get("vpcp_region")
        vpcp_route_table1 = vpcs_environment.get("vpcp_route_table1")
        vpcp_route_table2 = vpcs_environment.get("vpcp_route_table2")
        
        # Roles
        roles_environment = environments.get("roles")
        iam_ssm_role = roles_environment.get("iam_ssm_role")
        iam_ssm_principal = roles_environment.get("iam_ssm_principal")
        
        # Bucket
        bucket_environment = environments.get("bucket")
        bucket_name = bucket_environment.get("bucket_name")
        versioned = bucket_environment.get("versioned")
        auto_delete_objects = bucket_environment.get("auto_delete_objects")
        deploy_name = bucket_environment.get("deploy_name")
        source = bucket_environment.get("source")
        
        # SGs
        sgs_environment = environments.get("sgs")
        sg1_name = sgs_environment.get("sg1_name")
        sg1_description = sgs_environment.get("sg1_description")
        sg1_allow_all_outbound = sgs_environment.get("sg1_allow_all_outbound")
        sg1_ssh_rule_ip = sgs_environment.get("sg1_ssh_rule_ip")
        sg1_ssh_rule_port = sgs_environment.get("sg1_ssh_rule_port")
        sg1_rdp_rule_ip = sgs_environment.get("sg1_rdp_rule_ip")
        sg1_rdp_rule_port = sgs_environment.get("sg1_rdp_rule_port")
        
        sg2_name = sgs_environment.get("sg2_name")
        sg2_description = sgs_environment.get("sg2_description")
        sg2_allow_all_outbound = sgs_environment.get("sg2_allow_all_outbound")
        sg2_sg_rule_port = sgs_environment.get("sg2_sg_rule_port")
        sg2_http_rule_port = sgs_environment.get("sg2_http_rule_port")
        sg2_https_rule_port = sgs_environment.get("sg2_https_rule_port")
        
        # Key Pair
        keypair_environment = environments.get("keypair")
        kp = keypair_environment.get("kp")
        kp_name = keypair_environment.get("kp_name")
        kp_description = keypair_environment.get("kp_description")
        kp_store = keypair_environment.get("kp_store")
        
        # EC2s
        ec2s_environment = environments.get("ec2s")
        ec1_name = ec2s_environment.get("ec1_name")
        ec1_instance_type = ec2s_environment.get("ec1_instance_type")
        ec1_device_name = ec2s_environment.get("ec1_device_name")
        ec1_encrypted = ec2s_environment.get("ec1_encrypted")
        
        ec2_name = ec2s_environment.get("ec2_name")
        ec2_instance_type = ec2s_environment.get("ec2_instance_type")
        ec2_device_name = ec2s_environment.get("ec2_device_name")
        ec2_encrypted = ec2s_environment.get("ec2_encrypted")
        
        # Server Script
        webscript_environment = environments.get("webscript")
        webscript_name = webscript_environment.get("asset_name")
        webscript_path = webscript_environment.get("asset_path")
        webscript_region = webscript_environment.get("asset_region")
        
        # Backup Vaults/Plans/Rules
        bus_environment = environments.get("bus")
        vault1_key = bus_environment.get("vault1_key")
        vault1_name = bus_environment.get("vault1_name")
        backup_vault1_name = bus_environment.get("backup_vault1_name")
        backup_plan1 = bus_environment.get("backup_plan1")
        backup_plan1_name = bus_environment.get("backup_plan1_name")
        rule1_name = bus_environment.get("rule1_name")
        minute1 = bus_environment.get("minute1")
        hour1 = bus_environment.get("hour1")
        daym1 = bus_environment.get("daym1")
        month1 = bus_environment.get("month1")
        weekday1 = bus_environment.get("weekday1")
        duration1 = bus_environment.get("duration1")
        
        vault2_key = bus_environment.get("vault2_key")
        vault2_name = bus_environment.get("vault2_name")
        backup_vault2_name = bus_environment.get("backup_vault2_name")
        backup_plan2 = bus_environment.get("backup_plan2")
        backup_plan2_name = bus_environment.get("backup_plan2_name")
        rule2_name = bus_environment.get("rule2_name")
        minute2 = bus_environment.get("minute2")
        hour2 = bus_environment.get("hour2")
        daym2 = bus_environment.get("daym2")
        month2 = bus_environment.get("month2")
        weekday2 = bus_environment.get("weekday2")
        duration2 = bus_environment.get("duration2")
        
                

        #################### Create 2 VPCs + VPC Peering ####################

        ### VPC 1 - Management VPC

        self.vpc1 = ec2.Vpc(
            self,
            vpc1_name,
            max_azs=vpc1_max_azs,
            cidr=vpc1_cidr_block,
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=vpc1_subnet_name,
                    cidr_mask=vpc1_cidr_mask,
                )
            ],
        )

        ### VPC 2 - Webserver VPC

        self.vpc2 = ec2.Vpc(
            self,
            vpc2_name,
            max_azs=vpc2_max_azs,
            cidr=vpc2_cidr_block,
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=vpc2_subnet_name,
                    cidr_mask=vpc2_cidr_mask,
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
            vpcp_route_table1,
            route_table_id=self.vpc1.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=self.vpc2.vpc_cidr_block,
            vpc_peering_connection_id=self.cfn_vPCPeering_connection.ref,
        )

        ### VPC Peering Connection between VPC2-VPC1 through Route-table
        self.cfn_Route = ec2.CfnRoute(
            self,
            vpcp_route_table2,
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
            self, 
            iam_ssm_role,
            assumed_by=iam.ServicePrincipal(iam_ssm_principal)
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
        
        ### Put file in the bucket
        s3deploy.BucketDeployment(
            self, 
            deploy_name,
            sources=[s3deploy.Source.asset(source)],
            destination_bucket=bootstrapbucket,
        )
        
        #################### Create Security Groups ####################

        ### Security Group Management Server
        mngtsg = ec2.SecurityGroup(
            self,
            sg1_name,
            vpc=self.vpc1,
            description=sg1_description,
            allow_all_outbound=sg1_allow_all_outbound,
        )
        mngtsg.add_ingress_rule(
            ec2.Peer.ipv4(sg1_ssh_rule_ip),
            ec2.Port.tcp(sg1_ssh_rule_port),
            "allow ssh access from the VPC",
        )

        mngtsg.add_ingress_rule(
            ec2.Peer.ipv4(sg1_rdp_rule_ip),
            ec2.Port.tcp(sg1_rdp_rule_port),
            "allow RDP access from the VPC",
        )

        ### Security Group Web Server
        wssg = ec2.SecurityGroup(
            self,
            sg2_name,
            vpc=self.vpc2,
            description=sg2_description,
            allow_all_outbound=sg2_allow_all_outbound,
        )

        wssg.add_ingress_rule(
            ec2.Peer.security_group_id(mngtsg.security_group_id),
            ec2.Port.tcp(sg2_sg_rule_port),
            "allow ssh access from the management Security Group",
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(), 
            ec2.Port.tcp(sg2_http_rule_port), 
            "allow HTTP traffic from anywhere"
        )

        wssg.add_ingress_rule(
            ec2.Peer.any_ipv4(), 
            ec2.Port.tcp(sg2_https_rule_port), 
            "allow HTTPS traffic from anywhere"
        )

        #################### Create Key Pair ####################

        ### key pair
        key = KeyPair(
            self,
            kp,
            name=kp_name,
            description=kp_name,
            store_public_key=kp_store,
        )

        key.grant_read_on_private_key(role)
        key.grant_read_on_public_key(role)

        #################### Create EC2 Instances ####################

        ### Instance Management Server (Windows)
        management_server = ec2.Instance(
            self,
            ec1_name,
            instance_type=ec2.InstanceType(ec1_instance_type),
            machine_image=amzn_windows,
            vpc=self.vpc1,
            security_group=mngtsg,
            key_name=key.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name=ec1_device_name,
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=ec1_encrypted),
                )
            ],
        )
        
            
        ### Instance Web Server
        web_server = ec2.Instance(
            self,
            ec2_name,
            instance_type=ec2.InstanceType(ec2_instance_type),
            machine_image=amzn_linux,
            vpc=self.vpc2,
            security_group=wssg,
            key_name=key.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name=ec2_device_name,
                    volume=ec2.BlockDeviceVolume.ebs(8, encrypted=ec2_encrypted),
                )
            ],
        )
        
        # Launch script to install webserver
    
        assets = Asset(
            self,
            webscript_name,
            path=webscript_path,
        )
        
        Local_path = web_server.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=webscript_region,
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
        key = kms.Key(
            self,
            vault1_key,
            removal_policy=RemovalPolicy.DESTROY
            )
        vault = backup.BackupVault(
            self,
            vault1_name,
            backup_vault_name=backup_vault1_name,
            encryption_key=key
        )

        ### Create Backup Plan
        plan = backup.BackupPlan(
            self,
            backup_plan1,
            backup_plan_name=backup_plan1_name
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
                rule_name=rule1_name,
                schedule_expression=Schedule.cron(
                    minute=minute1,
                    hour=hour1,
                    day=daym1,
                    month=month1,
                    week_day=weekday1,
                ),
                delete_after=Duration.days(duration1),
            )
        )

        ### Backup Management Server
        ### Create Backup Vault
        key = kms.Key(
            self,
            vault2_key,
            removal_policy=RemovalPolicy.DESTROY)
        vault = backup.BackupVault(
            self,
            vault2_name,
            backup_vault_name=backup_vault2_name,
            encryption_key=key
        )

        ### Create Backup Plan
        plan = backup.BackupPlan(
            self,
            backup_plan2,
            backup_plan_name=backup_plan2_name
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
                rule_name=rule2_name,
                schedule_expression=Schedule.cron(
                    minute=minute2,
                    hour=hour2,
                    day=daym2,
                    month=month2,
                    week_day=weekday2,
                ),
                delete_after=Duration.days(duration2),
            )
        )
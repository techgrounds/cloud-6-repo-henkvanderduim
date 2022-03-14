"""''
PRD-01 Cloud6.Sentia1

Project: MVP v1.1

Ingredients:
- 1 Region
- 2 VPC's with each 2 AZ's

VPC MANAGEMENT-PRD-VPC                    | VPC APP-PRD-VPC
- 2 public subnets (10.10.10.0/24)        | - 2 PUBLIC SUBNETS (10.20.20.0/24)
- 1 EC2 instance (windows server)         | - 1 EC2 instance (linux) with website
- 1 Management Security Group             | - 1 Production Security Group
- Backup 1x a week (1 saved    )          | - daily backup (7 rounds saved)
                                          | - Load Balancer
                                          | - Elastic IP instead of Public IP Address
                                          | - TLS 1.2 or higher
                                          | - HTTP automatically converted to HTTPS
                                          | - Regular Health Checks
                                          | - When Health Check fails -> automatically recover instance
                                          | - High load -> autoscaling with max. 3 instances

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
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as targets,
    aws_autoscaling as autoscaling,
    aws_ssm as ssm,
    RemovalPolicy,
    CfnOutput,
    App,
    Stack,
    Tags,
)
from cdk_iam_floyd import Autoscaling, Elasticloadbalancing, ElasticloadbalancingV2
from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_events import Schedule
from aws_cdk.aws_s3_assets import Asset
from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy


### directory variable
dirname = os.path.dirname(__file__)


#################### STACK ####################


class Mvpscript11Stack(Stack):
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

        asg_name = vpcs_environment.get("asg_name")
        asg_cidr_block = vpcs_environment.get("asg_cidr_block")
        asg_cidr_mask = vpcs_environment.get("asg_cidr_mask")
        public_asg_subnet_name = vpcs_environment.get("public_asg_subnet_name")
        private_asg_subnet_name = vpcs_environment.get("private_asg_subnet_name")
        asg_max_azs = vpcs_environment.get("asg_max_azs")

        vpcp_name = vpcs_environment.get("vpcp_name")
        vpcp_region = vpcs_environment.get("vpcp_region")
        mngt_vpcp_route = vpcs_environment.get("mngt_vpcp_route")
        asg_vpcp_route = vpcs_environment.get("asg_vpcp_route")

        # Roles
        roles_environment = environments.get("roles")
        iam_ssm_role = roles_environment.get("iam_ssm_role")
        iam_ssm_principal = roles_environment.get("iam_ssm_principal")

        # Bucket
        bucket_environment = environments.get("bucket")
        bucket_name = bucket_environment.get("bucket_name")
        versioned = bucket_environment.get("versioned")
        auto_delete_objects = bucket_environment.get("auto_delete_objects")
        deployment_name = bucket_environment.get("deployment_name")
        asset_bucket = bucket_environment.get("asset_bucket")

        # Security Groups
        sgs_environment = environments.get("sgs")
        mngt_sg_name = sgs_environment.get("mngt_sg_name")
        mngt_sg_description = sgs_environment.get("mngt_sg_description")
        mngt_sg_allow_all_outbound = sgs_environment.get("mngt_sg_allow_all_outbound")
        mngt_sg_ssh_rule_ip = sgs_environment.get("mngt_sg_ssh_rule_ip")
        mngt_sg_ssh_rule_port = sgs_environment.get("mngt_sg_ssh_rule_port")
        mngt_sg_rdp_rule_ip = sgs_environment.get("mngt_sg_rdp_rule_ip")
        mngt_sg_rdp_rule_port = sgs_environment.get("mngt_sg_rdp_rule_port")

        asgsg_name = sgs_environment.get("asgsg_name")
        asgsg_description = sgs_environment.get("asgsg_description")
        asgsg_allow_all_outbound = sgs_environment.get("asgsg_allow_all_outbound")
        asgsg_rule_port = sgs_environment.get("asgsg_rule_port")
        asgsg_http_rule_port = sgs_environment.get("asgsg_http_rule_port")
        asgsg_https_rule_port = sgs_environment.get("asgsg_https_rule_port")
        asgsg_elb_port = sgs_environment.get("asgsg_elb_port")

        elbsg_name = sgs_environment.get("elbsg_name")
        elbsg_description = sgs_environment.get("elbsg_description")
        elbsg_allow_all_outbound = sgs_environment.get("elbsg_allow_all_outbound")
        elbsg_http_rule_port = sgs_environment.get("elbsg_http_rule_port")
        elbsg_https_rule_port = sgs_environment.get("elbsg_https_rule_port")

        # Key Pair
        keypair_environment = environments.get("keypair")
        mngt_kp = keypair_environment.get("mngt_kp")
        mngt_kp_name = keypair_environment.get("mngt_kp_name")
        mngt_kp_description = keypair_environment.get("mngt_kp_description")
        mngt_kp_store = keypair_environment.get("mngt_kp_store")

        asg_kp = keypair_environment.get("asg_kp")
        asg_kp_name = keypair_environment.get("asg_kp_name")
        asg_kp_description = keypair_environment.get("asg_kp_description")
        asg_kp_store = keypair_environment.get("asg_kp_store")

        # LBS
        lbs_environment = environments.get("lbs")
        lb_name = lbs_environment.get("lb_name")
        lb_if = lbs_environment.get("lb_if")
        arn_cert = lbs_environment.get("arn_cert")
        list_name = lbs_environment.get("list_name")
        target_group = lbs_environment.get("target_group")

        # EC2s
        ec2s_environment = environments.get("ec2s")
        mngt_ec2_name = ec2s_environment.get("mngt_ec2_name")
        mngt_ec2_instance_type = ec2s_environment.get("mngt_ec2_instance_type")
        mngt_ec2_encrypted = ec2s_environment.get("mngt_ec2_encrypted")

        asg_ec2_name = ec2s_environment.get("asg_ec2_name")
        asg_ec2_instance_type = ec2s_environment.get("asg_ec2_instance_type")
        asg_ec2_encrypted = ec2s_environment.get("asg_ec2_encrypted")
        asg_delete = ec2s_environment.get("asg_delete")

        # Server Script
        webscript_environment = environments.get("webscript")
        wsrv_asset_name = webscript_environment.get("wsrv_asset_name")
        wsrv_asset_path = webscript_environment.get("wsrv_asset_path")
        wsrv_asset_region = webscript_environment.get("wsrv_asset_region")

        # Tags
        tags_environment = environments.get("tags")
        mngt_tag_key = tags_environment.get("mngt_tag_key")
        mngt_tag_value = tags_environment.get("mngt_tag_value")
        asg_tag_key = tags_environment.get("asg_tag_key")
        asg_tag_value = tags_environment.get("asg_tag_value")

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

        asg_vault_key = bus_environment.get("asg_vault_key")
        asg_vault_name = bus_environment.get("asg_vault_name")
        asg_backup_vault_name = bus_environment.get("asg_backup_vault_name")
        asg_backup_plan = bus_environment.get("asg_backup_plan")
        asg_backup_plan_name = bus_environment.get("asg_backup_plan_name")
        asg_rule_name = bus_environment.get("asg_rule_name")
        asg_minute = bus_environment.get("asg_minute")
        asg_hour = bus_environment.get("asg_hour")
        asg_month = bus_environment.get("asg_month")
        asg_weekday = bus_environment.get("asg_weekday")
        asg_duration = bus_environment.get("asg_duration")

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

        ### S3 Bucket file deployment.

        s3deploy.BucketDeployment(
            self,
            deployment_name,
            sources=[s3deploy.Source.asset(asset_bucket)],
            destination_bucket=bootstrapbucket,
        )

        #################### VPC's t.b.v. MNGT Server en Autoscaling ####################

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
            nat_gateways=1,
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
            asg_vpcp_route,
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
            ec2.Peer.security_group_id(elbsg.security_group_id),
            ec2.Port.tcp(asgsg_elb_port),
            "allow access from the ELB Security Group",
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
        asgkey = KeyPair(
            self,
            asg_kp,
            name=asg_kp_name,
            description=asg_kp_description,
            store_public_key=asg_kp_store,
        )

        asgkey.grant_read_on_private_key(role)
        asgkey.grant_read_on_public_key(role)

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

        #################### Create Autoscaling Group ####################

        asg = autoscaling.AutoScalingGroup(
            self,
            asg_ec2_name,
            vpc=self.vpc2,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            instance_type=ec2.InstanceType(asg_ec2_instance_type),
            machine_image=amzn_linux,
            key_name=asgkey.key_pair_name,
            role=role,
            security_group=asgsg,
            desired_capacity=1,
            max_capacity=3,
            min_capacity=1,
            block_devices=[
                autoscaling.BlockDevice(
                    device_name="/dev/xvda",
                    volume=autoscaling.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=asg_ec2_encrypted,
                        delete_on_termination=asg_delete,
                    ),
                )
            ],
        )

        ### Launch script to install webserver

        assets = Asset(
            self,
            wsrv_asset_name,
            path=wsrv_asset_path,
        )

        listener_certificate = elbv2.ListenerCertificate.from_arn(arn_cert)

        Local_path = asg.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=wsrv_asset_region,
        )

        asg.user_data.add_execute_file_command(file_path=Local_path)

        assets.grant_read(asg.role)

        #################### Create Tags ####################

        Tags.of(management_server).add(mngt_tag_key, mngt_tag_value)
        Tags.of(asg).add(asg_tag_key, asg_tag_value)

        #################### Elastic Load Balancer ####################

        ### Create the Load Balancer in the Webserver's VPC
        lb = elbv2.ApplicationLoadBalancer(
            self,
            lb_name,
            vpc=self.vpc2,
            internet_facing=lb_if,
            security_group=elbsg,
            load_balancer_name=lb_name,
        )

        ### Listener
        listener_certificate = elbv2.ListenerCertificate.from_arn(arn_cert)
        listener = lb.add_listener(
            list_name,
            port=443,
            certificates=[listener_certificate],
            ssl_policy=elbv2.SslPolicy.RECOMMENDED,
        )

        ### HTTP => HTTPS redirect
        lb.add_redirect(source_port=80, target_port=443)

        ### Health Check
        health_check = elbv2.HealthCheck(
            interval=Duration.seconds(60), path="/", timeout=Duration.seconds(30)
        )

        ### Listener connections
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")

        ### add target
        listener.add_targets(
            target_group, port=80, targets=[asg], health_check=health_check
        )

        ### Autoscaling Action
        asg.scale_on_cpu_utilization("scale_on_cpu", target_utilization_percent=60)

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
            removal_policy=RemovalPolicy.DESTROY,
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
        asgkey = kms.Key(self, asg_vault_key, removal_policy=RemovalPolicy.DESTROY)
        asgvault = backup.BackupVault(
            self,
            asg_vault_name,
            backup_vault_name=asg_backup_vault_name,
            encryption_key=asgkey,
            removal_policy=RemovalPolicy.DESTROY,
        )

        ### Create Backup Plan
        asgplan = backup.BackupPlan(
            self, asg_backup_plan, backup_plan_name=asg_backup_plan_name
        )

        ### Add Backup Resources through Tags
        asgplan.add_selection(
            "Selection",
            resources=[backup.BackupResource.from_tag(asg_tag_key, asg_tag_value)],
        )

        ### Create Backup Rule - Once a week and save 1
        asgplan.add_rule(
            backup.BackupPlanRule(
                backup_vault=asgvault,
                rule_name=asg_rule_name,
                schedule_expression=Schedule.cron(
                    minute=asg_minute,
                    hour=asg_hour,
                    month=asg_month,
                    week_day=asg_weekday,
                ),
                delete_after=Duration.days(asg_duration),
            )
        )

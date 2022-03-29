from aws_cdk.aws_s3_assets import Asset
from cdk_ec2_key_pair import KeyPair
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_iam as iam,
)


class AsgStack(cdk.NestedStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        asgsg: ec2.SecurityGroup,
        vpc: ec2.Vpc,
        role: iam.Role,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        keypair_environment = environments.get("keypair")
        asg_kp = keypair_environment.get("asg_kp")
        asg_kp_name = keypair_environment.get("asg_kp_name")
        asg_kp_description = keypair_environment.get("asg_kp_description")
        asg_kp_store = keypair_environment.get("asg_kp_store")
        ec2s_environment = environments.get("ec2s")
        asg_ec2_name = ec2s_environment.get("asg_ec2_name")
        asg_ec2_instance_type = ec2s_environment.get("asg_ec2_instance_type")
        asg_ec2_encrypted = ec2s_environment.get("asg_ec2_encrypted")
        asg_delete = ec2s_environment.get("asg_delete")
        webscript_environment = environments.get("webscript")
        wsrv_asset_name = webscript_environment.get("wsrv_asset_name")
        wsrv_asset_path = webscript_environment.get("wsrv_asset_path")
        wsrv_asset_region = webscript_environment.get("wsrv_asset_region")

        ### AMI Linux
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        ### key pair webserver
        asgkey = KeyPair(
            scope=scope,
            id=asg_kp,
            name=asg_kp_name,
            description=asg_kp_description,
            store_public_key=asg_kp_store,
        )

        asgkey.grant_read_on_private_key(role)
        asgkey.grant_read_on_public_key(role)

        #################### Create Autoscaling ####################

        self.asg = autoscaling.AutoScalingGroup(
            self,
            asg_ec2_name,
            vpc=vpc,
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

        Local_path = self.asg.user_data.add_s3_download_command(
            bucket=assets.bucket,
            bucket_key=assets.s3_object_key,
            region=wsrv_asset_region,
        )

        self.asg.user_data.add_execute_file_command(file_path=Local_path)

        assets.grant_read(self.asg.role)

import aws_cdk as cdk
from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk import (
    aws_ec2 as ec2,
)


class MngtStack(cdk.NestedStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        vpc: ec2.Vpc,
        mngtsg: ec2.SecurityGroup,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        keypair_environment = environments.get("keypair")
        mngt_kp = keypair_environment.get("mngt_kp")
        mngt_kp_name = keypair_environment.get("mngt_kp_name")
        mngt_kp_description = keypair_environment.get("mngt_kp_description")
        mngt_kp_store = keypair_environment.get("mngt_kp_store")
        ec2s_environment = environments.get("ec2s")
        mngt_ec2_name = ec2s_environment.get("mngt_ec2_name")
        mngt_ec2_instance_type = ec2s_environment.get("mngt_ec2_instance_type")
        mngt_ec2_encrypted = ec2s_environment.get("mngt_ec2_encrypted")
        webscript_environment = environments.get("webscript")

        ### AMI Windows
        amzn_windows = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
        )

        ## key pair Mangement Server
        mngtkey = KeyPair(
            scope=scope,
            id=mngt_kp,
            name=mngt_kp_name,
            description=mngt_kp_description,
            store_public_key=mngt_kp_store,
        )

        ### Instance Management Server (Windows)
        self.management_server = ec2.Instance(
            self,
            mngt_ec2_name,
            instance_type=ec2.InstanceType(mngt_ec2_instance_type),
            machine_image=amzn_windows,
            vpc=vpc,
            security_group=mngtsg,
            key_name=mngtkey.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=mngt_ec2_encrypted),
                )
            ],
        )

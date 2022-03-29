#!/usr/bin/env python3
import os

from mvpfinal.s3bucket import S3BucketStack
from mvpfinal.vpcs import VpcsStack
from mvpfinal.vpcp import VpcpStack
from mvpfinal.sg import SgStack
from mvpfinal.mngt import MngtStack
from mvpfinal.asg import AsgStack
from mvpfinal.elb import ElbStack
from mvpfinal.backup import BackupStack

import aws_cdk as cdk

app = cdk.App()
main_stack = cdk.Stack(
    app, "MainStack", env=cdk.Environment(account="048127819745", region="eu-central-1")
)
s3bucket = S3BucketStack(main_stack, "S3 Bucket App")
vpc_app = VpcsStack(main_stack, "VPCs app")
vpcp_app = VpcpStack(
    main_stack,
    "VPC Peering App",
    vpc1=vpc_app.vpc1,
    vpc2=vpc_app.vpc2,
)
sg_app = SgStack(
    main_stack,
    "Security Groups App",
    vpc1=vpc_app.vpc1,
    vpc2=vpc_app.vpc2,
)
mngt_app = MngtStack(
    main_stack,
    "MNGT App",
    vpc=vpc_app.vpc1,
    mngtsg=sg_app.mngtsg,
)
asg_app = AsgStack(
    main_stack,
    "ASG App",
    vpc=vpc_app.vpc2,
    asgsg=sg_app.asgsg,
)
elb_app = ElbStack(
    main_stack,
    "ELB App",
    vpc=vpc_app.vpc2,
    asg=asg_app.asg,
)
Backup_app = BackupStack(
    main_stack,
    "Backup App",
    management_server=mngt_app.management_server,
    asg=asg_app.asg,
)


app.synth()

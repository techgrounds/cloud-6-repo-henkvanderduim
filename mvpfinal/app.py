#!/usr/bin/env python3
import os

from mvpfinal.s3bucket import S3BucketStack
from mvpfinal.vpcs import VpcsStack
from mvpfinal.vpcp import VpcpStack
from mvpfinal.roles import RolesStack
from mvpfinal.sg import SgStack
from mvpfinal.mngt import MngtStack
from mvpfinal.asg import AsgStack
from mvpfinal.elb import ElbStack
from mvpfinal.backup import BackupStack

import aws_cdk as cdk

app = cdk.App()
mvp_stack = cdk.Stack(
    app, "MVPStack", env=cdk.Environment(account="048127819745", region="eu-central-1")
)
s3bucket = S3BucketStack(mvp_stack, "S3 Bucket App")
vpc_app = VpcsStack(mvp_stack, "VPCs app")
vpcp_app = VpcpStack(
    mvp_stack,
    "VPC Peering App",
    vpc1=vpc_app.vpc1,
    vpc2=vpc_app.vpc2,
)

roles_app = RolesStack(mvp_stack, "Roles App")

sg_app = SgStack(
    mvp_stack,
    "Security Groups App",
    vpc1=vpc_app.vpc1,
    vpc2=vpc_app.vpc2,
)
mngt_app = MngtStack(
    mvp_stack,
    "MNGT App",
    vpc=vpc_app.vpc1,
    mngtsg=sg_app.mngtsg,
    role=roles_app.role,
)
asg_app = AsgStack(
    mvp_stack,
    "ASG App",
    vpc=vpc_app.vpc2,
    asgsg=sg_app.asgsg,
    role=roles_app.role,
)
elb_app = ElbStack(
    mvp_stack,
    "ELB App",
    vpc=vpc_app.vpc2,
    asg=asg_app.asg,
    elbsg=sg_app.elbsg,
)
Backup_app = BackupStack(
    mvp_stack,
    "Backup App",
    management_server=mngt_app.management_server,
    asg=asg_app.asg,
)


app.synth()

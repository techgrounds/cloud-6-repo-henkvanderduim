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

### Parameters t.b.v de nested stack
stackname = "MVPStack"
account = "048127819745"
region = "eu-central-1"
bucketapp = "S3 Bucket App"
vpcapp = "VPCs App"
vpcpapp = "VPC Peering App"
rolesapp = "Roles App"
sgapp = "Security Groups App"
mngtapp = "Management App"
asgapp = "Auto Scaling Groups App"
elbapp = "Elastic Load Balancer App"
backupapp = "Backup App"


app = cdk.App()
mvp_stack = cdk.Stack(
    app, stackname, env=cdk.Environment(account=account, region=region)
)
s3bucket = S3BucketStack(mvp_stack, bucketapp)
vpc_app = VpcsStack(mvp_stack, vpcapp)
vpcp_app = VpcpStack(
    mvp_stack,
    vpcpapp,
    vpc1=vpc_app.vpc1,
    vpc2=vpc_app.vpc2,
)

roles_app = RolesStack(mvp_stack, rolesapp)

sg_app = SgStack(
    mvp_stack,
    sgapp,
    vpc1=vpc_app.vpc1,
    vpc2=vpc_app.vpc2,
)
mngt_app = MngtStack(
    mvp_stack,
    mngtapp,
    vpc=vpc_app.vpc1,
    mngtsg=sg_app.mngtsg,
    role=roles_app.role,
)
asg_app = AsgStack(
    mvp_stack,
    asgapp,
    vpc=vpc_app.vpc2,
    asgsg=sg_app.asgsg,
    role=roles_app.role,
)
elb_app = ElbStack(
    mvp_stack,
    elbapp,
    vpc=vpc_app.vpc2,
    asg=asg_app.asg,
    elbsg=sg_app.elbsg,
)
Backup_app = BackupStack(
    mvp_stack,
    backupapp,
    management_server=mngt_app.management_server,
    asg=asg_app.asg,
)

app.synth()

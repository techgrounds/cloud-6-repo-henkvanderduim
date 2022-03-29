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
vpcs = VpcsStack(main_stack, "VPCs app")
vpcp = VpcpStack(
    main_stack,
    "VPC Peering App",
    vpc1=vpcs.vpc1,
    vpc2=vpcs.vpc2,
)
sg = SgStack(
    main_stack,
    "Security Groups App",
    vpc1=vpcs.vpc1,
    vpc2=vpcs.vpc2,
)
mngt = MngtStack(main_stack, "MNGT App", vpc=vpcs.vpc1, mngtsg=sg.mngtsg)
asg = AsgStack(
    main_stack,
    "ASG App",
    vpc=vpcs.vpc2,
    asgsg=sg.asgsg,
)
elb = ElbStack(
    main_stack,
    "ELB App",
    vpc=vpcs.vpc2,
    asg=asg.asg,
)
Backup = BackupStack(
    main_stack,
    "Backup App",
    management_server=mngt.management_server,
    asg=asg.asg,
)


app.synth()

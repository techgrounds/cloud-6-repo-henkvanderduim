# PRD-01 Cloud6.Sentia1
#
# Project: MVP v1.1
#
### Importing the necessary libraries

import os.path
import aws_acm_certified as acm
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

from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
import aws_cdk.aws_elasticloadbalancingv2 as elbv2
import aws_acm_certified as acm
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    Duration,
)


class ElbStack(cdk.NestedStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        asg: autoscaling.AutoScalingGroup,
        vpc: ec2.Vpc,
        elbsg: ec2.SecurityGroup,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        lbs_environment = environments.get("lbs")
        lb_name = lbs_environment.get("lb_name")
        lb_if = lbs_environment.get("lb_if")
        list_name = lbs_environment.get("list_name")
        target_group = lbs_environment.get("target_group")
        bucket_environment = environments.get("bucket")
        albbucketname = bucket_environment.get("albbucketname")

        ### Create the Load Balancer in the Webserver's VPC
        self.lb = elbv2.ApplicationLoadBalancer(
            self,
            lb_name,
            vpc=vpc,
            security_group=elbsg,
            internet_facing=lb_if,
            log_access_logs=albbucketname,
            load_balancer_name=lb_name,
        )

        ### Listener
        listener_certificate = elbv2.ListenerCertificate.from_arn(
            acm.generate_certificate(),
        )

        listener = self.lb.add_listener(
            list_name,
            port=443,
            certificates=[listener_certificate],
            ssl_policy=elbv2.SslPolicy.RECOMMENDED,
        )

        ### HTTP => HTTPS redirect
        self.lb.add_redirect(source_port=80, target_port=443)

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

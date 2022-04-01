import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_s3_deployment as s3deploy,
    aws_s3 as s3,
)


class S3BucketStack(cdk.NestedStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        environments = self.node.try_get_context("ENVIRONMENTS")
        bucket_environment = environments.get("bucket")
        bucket_name = bucket_environment.get("bucket_name")
        versioned = bucket_environment.get("versioned")
        auto_delete_objects = bucket_environment.get("auto_delete_objects")
        deployment_name = bucket_environment.get("deployment_name")
        asset_bucket = bucket_environment.get("asset_bucket")

        ### S3 bucket bootstrap
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

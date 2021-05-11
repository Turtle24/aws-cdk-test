#!/usr/bin/env python3
import os

import aws_cdk.aws_s3 as s3
from aws_cdk import core as cdk
from aws_cdk.core import App, Construct
from aws_cdk import aws_iam as iam


# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class S3Bucket:
    def __init__(self, id:str, app: App, **kwargs) -> None:
        super().__init__(app, id)
        myBucket = s3.Bucket(self, 'MyFirstBucket', bucket_name='balkaran-aws-cdk-s3-demo-bucket')
        myBucket.add_to_resource_policy(    #Grant read access to everyone in your account
            iam.PolicyStatement(
                    actions=['s3:GetObject'],
                    resources=[myBucket.arn_for_objects('*')],
                    principals=[iam.AccountPrincipal(account_id=core.Aws.ACCOUNT_ID)]
            )
        )

app = App()
S3Bucket(app, "S3Bucket")
app.synth()

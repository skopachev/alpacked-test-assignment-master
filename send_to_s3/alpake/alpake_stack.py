#from aws_cdk import core as cdk,

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import (
    aws_s3 as s3,
    core   as cdk,
)
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as origins


class AlpakeStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       # s3.Bucket(self, "alpaked-02")
        my_bucket = s3.Bucket(self, "alpaked-03")
        cloudfront.Distribution(self, "myDist",
                                default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket))
                                )




        # The code that defines your stack goes here

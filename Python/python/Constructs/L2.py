from aws_cdk import core
import aws_cdk.aws_s3 as s3

class S3BucketL2Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # L2 construct for S3 Bucket with versioning enabled
        s3.Bucket(self, "MyL2Bucket",
                  bucket_name="my-l2-s3-bucket",
                  versioned=True,
                  removal_policy=core.RemovalPolicy.DESTROY)  # Automatically delete on stack deletion

app = core.App()
S3BucketL2Stack(app, "S3BucketL2Example")

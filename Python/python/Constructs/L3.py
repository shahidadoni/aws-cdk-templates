from aws_cdk import core
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_s3_notifications as s3_notifications
import aws_cdk.aws_lambda as _lambda

class S3BucketL3Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Lambda function to handle S3 event notifications
        my_lambda = _lambda.Function(self, "MyLambda",
                                     runtime=_lambda.Runtime.PYTHON_3_8,
                                     handler="index.handler",
                                     code=_lambda.Code.from_inline("""
import json

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return {'statusCode': 200, 'body': json.dumps('Event processed!')}
                                     """))

        # Create an S3 Bucket with event notification to trigger Lambda function
        my_bucket = s3.Bucket(self, "MyL3Bucket",
                              bucket_name="my-l3-s3-bucket",
                              versioned=True)

        # Add event notification to trigger Lambda function when an object is created
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED,
                                         s3_notifications.LambdaDestination(my_lambda))

app = core.App()
S3BucketL3Stack(app, "S3BucketL3Example")


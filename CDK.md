
# Cloud Development Kit

- Define Iac in most used programming languages such as TypeScript, JavaScript, Python, Java, C#/.Net, and Go
- Two components
  - AWS CDK Construct Library
  - AWS CDK cli
- Project consist of App, App consists of stacks and stacks consists of constructs
- Stacks are in bacic understanding refer to as cloudformation stack
- Constructs are reusable code snippets for creating your resources or infrastructure.
- AWS CDK integrates with AWS CloudFormation to deploy and provision your infrastructure on AWS
- AWS CDK also offers powerful abstractions, which can speed up and simplify the infrastructure development process. For example, the AWS CDK includes constructs that provide sensible default configurations and helper methods that generate boilerplate code for you
- https://docs.aws.amazon.com/cdk/v2/guide/work-with.html#work-with-cdk-compare
- jsii
- aws-cdk-lib of app and stack base classes
- aws-cdk-lib.s3 will import construct modules for s3 services
- https://docs.aws.amazon.com/cdk/v2/guide/apps.html#apps-tree
- https://docs.aws.amazon.com/cdk/v2/guide/stacks.html
- 

## Why CDK integration with CFT

- you can perform infrastructure deployments predictably and repeatedly, with rollback on error
- AWS CloudFormation templates are declarative, meaning they declare the desired state or outcome of your infrastructure
- With the AWS CDK, you can manage your infrastructure imperatively, using general-purpose programming languages. Instead of just defining a desired state declaratively, you can define the logic or sequence necessary to reach the desired state.

## Benefits

- Scalable
- Structured way to mange infra
- programming elements like parameters, conditionals, loops, composition, and inheritance.
- same programming language to define app and infra
- create, deploy, and maintain infrastructure in a programmatic/declarative way.
- Create your own constructs that are customized for your unique use cases and share them across your organization or even with the public.
- Integration with other popular tools like terraform and kubernetes

## Constructs

- low-level constructs to define individual AWS CloudFormation resources and their properties. Use high-level constructs to quickly define larger components of your application, with sensible, secure defaults for your AWS resources, defining more infrastructure with less code.
- Typescript

```typescript
  export class MyEcsConstructStack extends Stack {
  constructor(scope: App, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "MyVpc", {
      maxAzs: 3 // Default is all AZs in region
    });

    const cluster = new ecs.Cluster(this, "MyCluster", {
      vpc: vpc
    });

    // Create a load-balanced Fargate service and make it public
    new ecs_patterns.ApplicationLoadBalancedFargateService(this, "MyFargateService", {
      cluster: cluster, // Required
      cpu: 512, // Default is 256
      desiredCount: 6, // Default is 1
      taskImageOptions: { image: ecs.ContainerImage.fromRegistry("amazon/amazon-ecs-sample") },
      memoryLimitMiB: 2048, // Default is 512
      publicLoadBalancer: true // Default is false
    });
  }
}
```

- Python

```python
class MyEcsConstructStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "MyVpc", max_azs=3)     # default is all AZs in region

        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MyFargateService",
            cluster=cluster,            # Required
            cpu=512,                    # Default is 256
            desired_count=6,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            memory_limit_mib=2048,      # Default is 512
            public_load_balancer=True)  # Default is False
```

## cdk-nag

- CDK-Nag is a tool used with the AWS Cloud Development Kit (CDK) that helps enforce best practices and guidelines for your CDK-based infrastructure code. It provides a way to catch potential issues early by checking your CDK stacks for compliance with certain rules and recommendations, similar to how linters work for programming languages.

- npm install cdk-nag
  
```Typescript
import * as cdk from 'aws-cdk-lib';
import { CfnNagSuppressions } from 'cdk-nag';

class MyStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
    // You can create CloudFormation resources like this:
    const myBucket = new cdk.aws_s3.CfnBucket(this, 'MyBucket', {
      bucketName: 'my-bucket',
      // other properties...
    });

    // Apply CDK-Nag suppressions or checks on the stack's CloudFormation resources
    CfnNagSuppressions.apply(this);
  }
}
```

## Examples

```typescript
// Instantiate default Bucket
const bucket = new s3.Bucket(this, 'amzn-s3-demo-bucket');

// Instantiate Bucket with bucketName and versioned properties
const bucket = new s3.Bucket(this, 'amzn-s3-demo-bucket', {
  bucketName: 'amzn-s3-demo-bucket',
   versioned: true,
});

// Instantiate Bucket with websiteRedirect, which has its own sub-properties
const bucket = new s3.Bucket(this, 'amzn-s3-demo-bucket', {
  websiteRedirect: {host: 'aws.amazon.com'}});
```

```python
# Instantiate default Bucket
bucket = s3.Bucket(self, "amzn-s3-demo-bucket")

# Instantiate Bucket with bucket_name and versioned properties
bucket = s3.Bucket(self, "amzn-s3-demo-bucket", bucket_name="amzn-s3-demo-bucket", versioned=true)

# Instantiate Bucket with website_redirect, which has its own sub-properties
bucket = s3.Bucket(self, "amzn-s3-demo-bucket", website_redirect=s3.WebsiteRedirect(
            host_name="aws.amazon.com"))
```

## Starting with

- cdk init: Creates cdk project. --language typescript flag for defining the programming language
- cdk.json: Configuration file for the AWS CDK. This file provides instruction to the AWS CDK CLI regarding how to run your app.
- https://docs.aws.amazon.com/cdk/v2/guide/projects.html#projects-specific

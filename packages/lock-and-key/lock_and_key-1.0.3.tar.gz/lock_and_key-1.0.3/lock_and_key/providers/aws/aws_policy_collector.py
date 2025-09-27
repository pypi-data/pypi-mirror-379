"""AWS policy collector for all services."""

from typing import TYPE_CHECKING, Any, Callable, Dict, List

from boto3 import Session
from botocore.exceptions import ClientError

from lock_and_key.providers.aws.resources.iam_policy_analyzer import IAMPolicyAnalyzer
from lock_and_key.types import Finding

if TYPE_CHECKING:
    from mypy_boto3_dynamodb import DynamoDBClient
    from mypy_boto3_glue import GlueClient
    from mypy_boto3_lambda import LambdaClient
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_sns import SNSClient
    from mypy_boto3_sqs import SQSClient


class AWSPolicyCollector:
    """Collects and analyzes policies from all AWS services."""

    def __init__(self, session: Session):
        """Initialize with boto3 session."""
        self.session = session
        self.service_collectors: Dict[str, Callable[[str], List[Dict[str, Any]]]] = {
            "s3": self._collect_s3,
            "dynamodb": self._collect_dynamodb,
            "glue": self._collect_glue,
            "lambda": self._collect_lambda,
            "sns": self._collect_sns,
            "sqs": self._collect_sqs,
        }

    def scan_all_policies(self, account_id: str) -> List[Finding]:
        """Scan all AWS resource policies and return findings."""
        findings = []
        analyzer = IAMPolicyAnalyzer(account_id)

        for service_name, collector_func in self.service_collectors.items():
            try:
                policies = collector_func(account_id)
                for policy_data in policies:
                    findings.extend(
                        analyzer.analyze_policy(
                            policy_data["policy"],
                            policy_data["resource_name"],
                            policy_data["resource_id"],
                        )
                    )
            except Exception:
                pass

        return findings

    def _collect_s3(self, account_id: str) -> List[Dict[str, Any]]:
        """Collect S3 bucket policies."""
        policies: List[Dict[str, Any]] = []
        s3: "S3Client" = self.session.client("s3")
        try:
            for bucket in s3.list_buckets()["Buckets"]:
                bucket_name: str = bucket["Name"]
                try:
                    policy: str = s3.get_bucket_policy(Bucket=bucket_name)["Policy"]
                    policies.append(
                        {
                            "resource_name": bucket_name,
                            "resource_id": f"arn:aws:s3:::{bucket_name}",
                            "policy": policy,
                        }
                    )
                except ClientError:
                    pass
        except ClientError:
            pass
        return policies

    def _collect_dynamodb(self, account_id: str) -> List[Dict[str, Any]]:
        """Collect DynamoDB table policies."""
        policies: List[Dict[str, Any]] = []
        dynamodb: "DynamoDBClient" = self.session.client("dynamodb")
        try:
            for page in dynamodb.get_paginator("list_tables").paginate():
                for table_name in page["TableNames"]:
                    try:
                        table_arn: str = dynamodb.describe_table(TableName=table_name)[
                            "Table"
                        ]["TableArn"]
                        policy: str = dynamodb.get_resource_policy(
                            ResourceArn=table_arn
                        )["Policy"]
                        policies.append(
                            {
                                "resource_name": table_name,
                                "resource_id": table_arn,
                                "policy": policy,
                            }
                        )
                    except ClientError:
                        pass
        except ClientError:
            pass
        return policies

    def _collect_glue(self, account_id: str) -> List[Dict[str, Any]]:
        """Collect Glue resource policies."""
        policies: List[Dict[str, Any]] = []
        glue: "GlueClient" = self.session.client("glue")
        region: str = self.session.region_name or "us-east-1"

        # Catalog policy
        try:
            policy: str = glue.get_resource_policy()["PolicyInJson"]
            policies.append(
                {
                    "resource_name": "Glue Data Catalog",
                    "resource_id": f"arn:aws:glue:{region}:{account_id}:catalog",
                    "policy": policy,
                }
            )
        except ClientError:
            pass

        # Database policies
        try:
            for page in glue.get_paginator("get_databases").paginate():
                for db in page["DatabaseList"]:
                    db_name: str = db["Name"]
                    db_arn: str = (
                        f"arn:aws:glue:{region}:{account_id}:database/{db_name}"
                    )
                    try:
                        db_policy: str = glue.get_resource_policy(ResourceArn=db_arn)[
                            "PolicyInJson"
                        ]
                        policies.append(
                            {
                                "resource_name": db_name,
                                "resource_id": db_arn,
                                "policy": db_policy,
                            }
                        )
                    except ClientError:
                        pass
        except ClientError:
            pass
        return policies

    def _collect_lambda(self, account_id: str) -> List[Dict[str, Any]]:
        """Collect Lambda function policies."""
        policies: List[Dict[str, Any]] = []
        lambda_client: "LambdaClient" = self.session.client("lambda")
        try:
            for page in lambda_client.get_paginator("list_functions").paginate():
                for func in page["Functions"]:
                    try:
                        policy: str = lambda_client.get_policy(
                            FunctionName=func["FunctionName"]
                        )["Policy"]
                        policies.append(
                            {
                                "resource_name": func["FunctionName"],
                                "resource_id": func["FunctionArn"],
                                "policy": policy,
                            }
                        )
                    except ClientError:
                        pass
        except ClientError:
            pass
        return policies

    def _collect_sns(self, account_id: str) -> List[Dict[str, Any]]:
        """Collect SNS topic policies."""
        policies: List[Dict[str, Any]] = []
        sns: "SNSClient" = self.session.client("sns")
        try:
            for page in sns.get_paginator("list_topics").paginate():
                for topic in page["Topics"]:
                    topic_arn: str = topic["TopicArn"]
                    try:
                        attrs: Dict[str, str] = sns.get_topic_attributes(
                            TopicArn=topic_arn
                        )["Attributes"]
                        if "Policy" in attrs:
                            policies.append(
                                {
                                    "resource_name": topic_arn.split(":")[-1],
                                    "resource_id": topic_arn,
                                    "policy": attrs["Policy"],
                                }
                            )
                    except ClientError:
                        pass
        except ClientError:
            pass
        return policies

    def _collect_sqs(self, account_id: str) -> List[Dict[str, Any]]:
        """Collect SQS queue policies."""
        policies: List[Dict[str, Any]] = []
        sqs: "SQSClient" = self.session.client("sqs")
        try:
            for queue_url in sqs.list_queues().get("QueueUrls", []):
                try:
                    attrs = sqs.get_queue_attributes(
                        QueueUrl=queue_url, AttributeNames=["Policy", "QueueArn"]
                    )["Attributes"]
                    if "Policy" in attrs:
                        policies.append(
                            {
                                "resource_name": queue_url.split("/")[-1],
                                "resource_id": attrs.get("QueueArn", queue_url),
                                "policy": attrs["Policy"],
                            }
                        )
                except ClientError:
                    pass
        except ClientError:
            pass
        return policies

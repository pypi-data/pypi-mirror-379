"""Base AWS service class."""

from typing import TYPE_CHECKING, Type, TypeVar

import boto3

from lock_and_key.types import AWSCreds

if TYPE_CHECKING:
    from mypy_boto3_sts import STSClient

T = TypeVar("T", bound="AWSServiceBase")


class AWSServiceBase:
    """Base class for AWS services."""

    def __init__(self, session: boto3.Session):
        self.session = session

    @classmethod
    def from_creds(cls: Type[T], creds: AWSCreds) -> T:
        """Create service from credentials."""
        session = cls._create_session(creds)
        return cls(session)

    @staticmethod
    def _create_session(creds: AWSCreds) -> boto3.Session:
        """Create boto3 session from credentials."""
        if creds.profile:
            return boto3.Session(profile_name=creds.profile)
        return boto3.Session(
            aws_access_key_id=creds.access_key,
            aws_secret_access_key=creds.secret_key,
            region_name=creds.region or "us-east-1",
        )

    def get_account_id(self) -> str:
        """Get AWS account ID."""
        sts: "STSClient" = self.session.client("sts")
        return sts.get_caller_identity()["Account"]

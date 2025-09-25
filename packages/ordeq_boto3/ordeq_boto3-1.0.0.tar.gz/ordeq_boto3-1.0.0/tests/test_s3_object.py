import pytest
from mypy_boto3_s3 import S3Client
from ordeq_boto3 import S3Object


@pytest.mark.docker
def test_it_loads(client: S3Client, bucket: str):
    key = "test_it_loads"
    data = b"someKey,someValue"
    client.put_object(Bucket=bucket, Key=key, Body=data)
    assert S3Object(bucket=bucket, key=key, client=client).load() == data


@pytest.mark.docker
def test_it_saves(client: S3Client, bucket: str):
    key = "test_it_loads"
    data = b"someKey,someValue"
    S3Object(bucket=bucket, key=key, client=client).save(data)
    assert client.get_object(Bucket=bucket, Key=key)["Body"].read() == data

import boto3
import json

BUCKET_NAME = "avani-s3-learning-001"
REGION = "us-east-1"

s3 = boto3.client("s3", region_name=REGION)

def save_text(key: str, content: str):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=content,
        ContentType="text/plain"
    )

def save_json(key: str, data: dict):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(data, indent=2),
        ContentType="application/json"
    )


def read_text(key):
    """
    Reads a text file from S3 and returns it as a string
    """
    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=key
    )
    return response["Body"].read().decode("utf-8")


def read_json(key):
    """
    Reads a JSON file from S3 and returns it as a Python dictionary
    """
    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=key
    )
    return json.loads(response["Body"].read().decode("utf-8"))


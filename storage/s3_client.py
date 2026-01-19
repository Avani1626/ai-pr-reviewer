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

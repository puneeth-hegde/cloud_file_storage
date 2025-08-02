import boto3
import logging
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Logger setup
logging.basicConfig(filename="logs.txt", level=logging.INFO)

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def upload_file(file, filename, user):
    s3.upload_fileobj(file, BUCKET_NAME, filename)
    logging.info(f"{user} uploaded {filename}")

def download_file(filename, user):
    s3.download_file(BUCKET_NAME, filename, filename)
    logging.info(f"{user} downloaded {filename}")
    return filename

def list_files():
    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)
    return [obj['Key'] for obj in objects.get('Contents', [])]

def delete_file(filename, user):
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
    logging.info(f"{user} deleted {filename}")

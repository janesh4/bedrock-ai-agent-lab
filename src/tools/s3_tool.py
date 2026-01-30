import boto3


class S3Tool:

    def __init__(self):
        self.client = boto3.client("s3")

    def list_buckets(self):

        response = self.client.list_buckets()

        bucket_names = []

        for bucket in response["Buckets"]:
            bucket_names.append(bucket["Name"])

        return bucket_names

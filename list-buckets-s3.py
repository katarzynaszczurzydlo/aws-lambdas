import json
import boto3
from collections import OrderedDict

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    lst_buckets = []
    s3client = boto3.client('s3')
    response = s3client.list_buckets()
    for buckets in response["Buckets"]:
        lst_buckets.append({"Bucket Name": buckets["Name"]})

    print(lst_buckets)

    AWS_BUCKET_NAME = 'YOUTBUCKETNAME'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    path = 'bucketslist.txt'
    data = json.dumps(lst_buckets)
    bucket.put_object(Key=path, Body=data, )

    return 0

import json
import boto3
import os
from collections import OrderedDict

s3 = boto3.resource('s3')
s3 = boto3.client('s3')
client = boto3.client('ec2')

def lambda_handler(event, context):
    lst_instances = []
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            for x in range(0, len(reservation["Instances"])):
                lst_instances.append({"instanceId": reservation["Instances"][x]["InstanceId"],
                                      "publicIp": reservation["Instances"][x]["PublicIpAddress"]})
    print(lst_instances)

    AWS_BUCKET_NAME = 'YOUTBUCKETNAME'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    path = 'instancesslist.txt'
    data = json.dumps(lst_instances)
    bucket.put_object(Key=path, Body=data, )

    return 0

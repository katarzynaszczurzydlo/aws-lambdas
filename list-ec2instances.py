import json
import boto3

client = boto3.client('ec2')

def handler(event, context):
    lst_instances = []
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance)
            for x in range(0, len(reservation["Instances"])):
                lst_instances.append({"instanceId": reservation["Instances"][x]["InstanceId"],"publicIp": reservation["Instances"][x]["PublicIpAddress"]})
    print(lst_instances)
    return lst_instances

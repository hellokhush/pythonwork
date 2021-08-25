import boto3
from botocore.exceptions import BotoCoreError, ClientError
region = 'us-east-1'
client = boto3.client('ec2', region_name = region)
#output = {}
try:
            
    response = client.describe_vpcs(Filters=[{'Name': 'isDefault', 'Values': ['true']}])
    if not len(response['Vpcs']):
        vpc_id = None
    else:
        vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
        
    ec2 = boto3.resource('ec2', region_name = region)       
    vpc = ec2.Vpc(vpc_id)
#print(vpc)
    print ("\t{0}\t\t {1}".format('Id', 'Instance_Name'))
    for instance in vpc.instances.all():
        for tag in instance.tags:
            if instance.instance_type == 'm5.large':
                if tag['Key'] == 'Name':  
                    print (" {0}\t {1}".format(instance.id, tag['Value']))
except ValueError as err:
    print(err.args )
         

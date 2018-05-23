import boto3
from secrets import *

client = boto3.client(
    'lambda',
    region_name=gimme_aws_region(),
    aws_access_key_id = gimme_aws_access_id(),
    aws_secret_access_key= gimme_aws_secret_access_key()
)

client.invoke(
    FunctionName='amibackup',
    InvocationType='Event',
    LogType='Tail',
)
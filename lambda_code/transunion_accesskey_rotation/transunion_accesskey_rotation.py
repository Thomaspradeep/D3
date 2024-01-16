import json
import boto3
import logging

#Configure the logging system
logging.basicConfig(level=logging.INFO)


UserName = 'datauser3'
iam = boto3.client("iam")
sns = boto3.client('sns', region_name='us-east-1')

#Listing the exist keys

def ListKey(UserName):
    ListKey = iam.list_access_keys(
        UserName = UserName
    )
    OldAccessKey = ListKey['AccessKeyMetadata'][0]['AccessKeyId']
    print('\n')
    return OldAccessKey

#delete existing Access key 

def DeleteKey(OldAccessKey,UserName):
    DeleteKey = iam.delete_access_key(
        AccessKeyId = OldAccessKey,
        UserName = UserName
    )

#Create the New AccessKey and SecretKey

def CreateKey(UserName):
    CreateKey = iam.create_access_key(
        UserName=UserName
    )
    NewAccessKey = CreateKey['AccessKey']['AccessKeyId']
    NewSecretAccessKey = CreateKey['AccessKey']['SecretAccessKey']
    return NewAccessKey, NewSecretAccessKey

# Send SNS notification to user

def SnsPublish(AccessKey,SecretKey,UserName):
    TargetArn = 'arn:aws:sns:us-east-1:941598205732:sns101'
    Message = f'''
Hi {UserName}, 

Your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY has been renewed for {UserName}.
Please find details below: 

USER_NAME={UserName}
AWS_ACCESS_KEY_ID={AccessKey}
AWS_SECRET_ACCESS_KEY={SecretKey}

Pleaser reach out to support for any queries or concerns.

Regards.
'''
    SendResponse = sns.publish(
        TargetArn = TargetArn,
        Message = Message,
        Subject='AWS Key has been renewed'
)

def lambda_handler(event, context):
    logging.info("Listing Old Access Key")
    OldAccessKey = ListKey(UserName)
    logging.info("Deleting Old Access Key")
    DeleteKey = DeleteKey(OldAccessKey,UserName)
    logging.info("Generating Old Access Key")
    CreateKey = CreateKey(UserName)
    AccessKey = CreateKey[0]
    SecretAccessKey = CreateKey[1]
    logging.info("Sending Email to End User with Latest Access ID and Secret Key")
    sns = SnsPublish(AccessKey, SecretAccessKey,UserName)
# This file can be used to subscribe to a SNS topic

# Import boto3 library
import boto3

# Specify region
AWS_REGION = "us-east-2"
# Choose SNS client
sns_client = boto3.client('sns', region_name=AWS_REGION)

'''
Function subscribe(topic, protocol, endpoint)

Description  : A function that can be used to create topic 

Arguments    : topic-- the ARN of topic to subscribe to
               protocol-- the protocol of communication, in our case we choose it to be email
               enpoint-- the email address which needs to be subscribed
                

Return       : Returns subscription ARN
'''

def subscribe(topic_arn, protocol, endpoint):
    """
    Subscribe to a topic using endpoint as email OR SMS
    """
    
    subscription = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol=protocol,
    Endpoint=endpoint,
    ReturnSubscriptionArn=True)['SubscriptionArn']
    return subscription


# ===============================Main code=============================================

# ARN of topic to which the email needs to be subscribed
topic_arn = 'arn:aws:sns:us-east-2:315997497220:alarms_testing'
# Defining protocol of communication
protocol = 'email'
# Email address
endpoint = 'rizwan.s@skipq.org'

# Calling the function
response = subscribe(topic_arn, protocol, endpoint)

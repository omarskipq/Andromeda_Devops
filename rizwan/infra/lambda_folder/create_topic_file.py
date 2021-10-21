# This file can be used to create a SNS topic

# Import boto3 library
import boto3

# Specify region
AWS_REGION = "us-east-2"

# Choose SNS client
sns_client = boto3.client('sns', region_name=AWS_REGION)

'''
Function create_topic(name)

Description  : A function that can be used to create topic 

Arguments    : name- the name of the SNS topic to be created
                

Return       : Returns a topic after creating it
'''


def create_topic(name):
    """
    Creates a SNS notification topic.
    """
    
    topic = sns_client.create_topic(Name=name)
    return topic
    

# Creating SNS 

# Choosing topic name
topic_name = 'alarms_testing'

# Calling create topic function
topic = create_topic(topic_name)

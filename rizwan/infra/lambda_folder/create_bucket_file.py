# This file can be used to create a S3 bucket

# Import boto3 library
import boto3

# Choose S3 as boto client
s3_client=boto3.client('s3')

# Create a bucket using function create_bucket, the fucntion needs two arguments bucket name and the location
# Bucket has been named rizwanbucket2021 and location has been chosen as us-east-2
s3_client.create_bucket(Bucket="rizwanbucket2021", CreateBucketConfiguration={'LocationConstraint':'us-east-2'})

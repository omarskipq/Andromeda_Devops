# Using CloudWatch to Write Metrics and Generate Alarms that are published to SNS for a Periodic Lambda Function Deployed on CDK.


## Description

The code performs three major functions: 
* Writing metrics to CloudWatch 
* Generating alarms on CloudWatch
* Publishing alarms via SNS

The metrics observed are latency and availability of websites. If any of the metrics breach the threshold values set by the user, an alarm is generated and published to a topic subscribed by the user on SNS.

## Files in the Project

* infra_stack.py file defines the InfraStack and the Lambda function to be used by the stack. CloudWatch metrics, alarms and SNS has been set up in this file.
* mult_whp.py file contains definition of handler function named health_web used by Lambda function. Availability and latency of each website is found using functions defined in this file. 
* url_retriever.py file contains a function named url_list that is used to retrieve websites list from S3 bucket.
* constants.py file contains constants such as namespace names, metric names etc. used by the project. Threshold values for metrics have also been defined here.
* create_bucket_file.py can be used to create a S3 bucket to hold a file containing website list whose metrics need to be observed.
* create_topic_file.py file can be used to create a topic on SNS. 
* subscribe_topic_file.py can be used to subscribe to a topic on SNS.
* cloud_watch.py defines CloudWatchMetrics class that defines a method to put metrics on CloudWatch.
* app.py defines the InfraStack to be used by the project.

## Setting up the Project

First change directory to infra folder using following CLI command:
```bash
cd infra/
```
Then you need to initiate a Python virtual environment by using following CLI commands:
```bash
source .venv/bin/activate
```
Install the libraries needed for the project to run by using the file named 'requirements.txt'. In order to do that you need to run the following CLI command:
```bash
pip install -r requirements.txt
```
This completes the process of setting up the project.

The user also needs to create a S3 bucket that holds the website list in json file. A topic needs to be created on SNS and user needs to subscribe to that topic for getting alarm updates.

### Creating the S3 Bucket

Use the file create_bucket_file.py to create the S3 bucket. The method for using the file has been described in detail in the file. This file only creates the bucket, the user needs to visit AWS S3 service to upload the json file.  

### Creating a SNS Topic

Use the file create_topic_file.py to create a SNS topic. The method for using the file has been described in detail in the file.

### Subscribing to the SNS Topic

Use the file subscribe_topic_file.py to subscribe to the newly created topic. The method for using the file has been described in detail in the file. After running the code you need to confirm subscription by visiting your email service.  ​

## Deploying the Project

First you need to synthesize the architecture using the following command at CLI:

```bash
cdk synth
```
In the next step you need to deploy the CDK architecture using the following bash command:
```bash
cdk deploy
```
After the code has been successfully deployed you need to use the AWS services to see the results.

## Checking the Results

### Testing Code on AWS Lambda
* After opening up the AWS Lambda service , go to the Functions tab and choose your Lambda function in the list provided, and click on it. 
* In the Code tab of the new page, click on Test button to check your results.

### Testing on CloudWatch 
* On CloudWatch you can test whether your metrics of availability and latency for every website are producing correct results.
* If threshold is breached for any metric, the alarm must show In Alert state.
* Check whether actions have been enabled for each alarm

### Checking Email for Alerts
If your code is working properly, you should be getting an email every time the alarm changes state.

## Maintainer
Rizwan Amir, email: rizwan.s@skipq.org 
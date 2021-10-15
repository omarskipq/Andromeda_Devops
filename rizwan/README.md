# Periodic Lambda Function Deployed on CDK for Checking Availability and Latency of a Website


## Description

The code deploys a Lambda function on AWS CDK to find latency and availability of a website i.e. www.skipq.org. The Lambda function has been made periodic, thus, it reports the latency and availability of the website every five minutes.

## Important Files in the Project
* app.py defines the InfraStack to be used by the project.
* infra_stack.py file defines the InfraStack and the Lambda function to be used by the stack.
* handler.py file contains definition of handler function used by Lambda function. This file is used to test HelloWorld Lambda function case.
* web_health_publisher.py file is define the handler function for Lambda function to perform our desired task of monitoring availability and health of a website.
* contants.py has been made to contain the URLs of websites that need to be monitored.

## Setting up the Project

First change directory to infra folder using following CLI command:
```bash
cd infra/
```
Then you need to initiate a Python virtual environment by using following CLI commands:
```bash
source .venv/bin/activate
```
Then you need to install libraries present in the file named 'requirements.txt'. In order to do that you need to run the following CLI command:
```bash
pip install -r requirements.txt
```
This completes the process of setting up the project.

## Running the Project

First you need to synthesize the architecture using the following command at CLI:

```bash
cdk synth
```
In the next step you need to deploy the CDK architecture using the following bash command:
```bash
cdk deploy
```
During the process of deployment you will be asked a question, just reply with  letter y to the question. After the code has been successfully deployed you need to use the AWS Lambda service to see the results.

## Testing Code on AWS Lambda
* After opening up the AWS Lambda service , go to Functions tab and choose your Function in the list provided, and click on it. 
* In the Code tab of this new page, click on Test button to check your results.

## Maintainer
Rizwan Amir, email: rizwan.s@skipq.org 

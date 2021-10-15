# Welcome to a Web Health Monitoring App using AWS Lambda

## Description
This app uses a lambda function which is scheduled to called every five minutes to track the latency and 
availability of our website to monitor its health. You can use the app by simply cloning the repository.

## Tech/Frameworks Used

<b>Tools Used</b>
<ul>
  <li>Python3</li>
  <li>AWS CDK</li>
</ul>


## Features

This project contains the following features:
<ul>
  <li>Infrastructure is built with a stack containing a lambda function.</li>
  <li>Lambda function measure the latency and checks the availability of the website.</li>
</ul>

## Code Explanation

### InfraStack
Stack is created inside the infra_stack.py file to create the infrastructure. AWS lambda function is created inside it to monitor the web health, which is defined in web_health_publisher file.
This lambda function is scheduled to run for every five minutes using event bridge i.e. AWS Lambda Event Target.

### AWS Lambda Function
Lambda function runs our code on a high-availability compute infrastructure and performs all of the administration of the compute resources, 
including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging. 


# How to run the project

You can visit <a href=https://docs.aws.amazon.com/cdk/latest/guide/work-with.html#work-with-prerequisites>AWS CDK installation link</a>. After installing it you can simply clone this repository and follow the instructions provided below: 

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
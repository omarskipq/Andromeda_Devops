# Public Website's Health Monitoring App
This project is about monitoring the health of public websites by measuring availability, and latency.

# Motivation
This project represents a part of my journey towards mastering cloud DevOps on Amazon Web Services(AWS). It shows that I can use AWS CDK in python for deploying AWS Lambda functions periodically.

# Screenshots
#### AWS CloudWatch Metrics
![image](https://user-images.githubusercontent.com/92221357/137349629-3123ce5a-e2cd-414a-b3c4-db41afcbfd91.png)

#### Stack Map built by Cloud Formation after Deployment

![image](https://user-images.githubusercontent.com/92221357/137350814-96a53dee-514e-4b69-a897-8349e0770d58.png)

# Tech/Frameworks Used

<b>Built with</b>
<ul>
  <li>Python</li>
  <li>AWS CDK</li>
</ul>

# Features
This project contains the following features:
<ul>
  <li>It contains a fully functioning AWS stack configuring in infra_stack.py file.</li>
  <li>Contains AWS Lambda Scheduling and you can easily change the duration by changing the minutes specified in the infra_stack.py file</li>
  <li>Contains a web_constants.py file where you can add/remove urls in a list called URL</li>
</ul>

# Code Explanation

## AWS CDK Stack

The file infra_stack.py contains the code that makes my stack. This file was created by AWS CDK upon project creation. It contains a class with the name of my stack which contains a construct. Inside this constructor I have defined an AWS Lambda Event Schedule, an AWS Lambda Event Target,an AWS Event Rule, and a call to a function that creates our AWS lambda function instance.

## AWS Lambda Function

The lambda handler present in web_metrics.py file calls a function read_url_FROMConstants to read constants defined in web_constants.py file and extract the url. On the extracted url we run the web_metrics function that using urllib3 and time python packages gives us information on the availability and latency of that url.

# Installation

You can visit <a href=https://docs.aws.amazon.com/cdk/latest/guide/work-with.html#work-with-prerequisites>AWS CDK installation link</a>. After installing it you can simply fork this repository and follow the usage instructions provided below 

# Usage

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

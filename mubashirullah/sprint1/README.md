
# Welcome to a simple Web Health App using Cloudwatch and AWS Lambda

This simply app creates a Lambda function and deploys it on AWS. Every 5 minutes it checks if SkipQ.org's website is available
and what latency the request has.

Simply clone the repo in an environment where you have the CDK up and running.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

You can use the following step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ python -m pip install -r requirements.txt

$ python -m pip install --target=./lambda/ requests==2.26.0
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `python -m pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

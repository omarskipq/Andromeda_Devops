from aws_cdk import core as cdk
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
# Importing the required libraries
from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_events
from aws_cdk import aws_events_targets

class InfraStackRizwan(cdk.Stack):
    # InfraStackRizwan constructor
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # Creating  the lamda function below, function has been named firstlambda, and its handler function named health_web
        # is available in file named web_health_publisher
        web_health_lambda = self.create_lambda('firstlambda', './lambda','web_health_publisher.health_web')
        
        # Defining schedule to run Lambda function periodically
        lambda_schedule=aws_events.Schedule.rate(core.Duration.minutes(5))
        # Defining which event will occur periodically, in our case Lambda function will be called periodically
        event_lambda_target=aws_events_targets.LambdaFunction(handler=web_health_lambda)
        # Combining the schedule and target 
        lambda_run_rule=aws_events.Rule(self,"web_health_lambdarule", description="Periodic_lambda",schedule=lambda_schedule, targets=[event_lambda_target])
        
    # A function to create lambda function
    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self, id,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6)
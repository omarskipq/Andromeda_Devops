from aws_cdk import core as cdk
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from aws_cdk import aws_lambda as lambda_

from aws_cdk import aws_events

from aws_cdk import aws_events_targets

class InfraStackShaharyar(cdk.Stack):
    
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # hw_lambda = self.create_lambda('Andromeda_shaharyar', './lambda','handler.lambda_handler')
        
        web_health_lambda = self.create_lambda('Andromeda_shaharyar','./lambda','handler.health_web')
        
        schedule_lambda = aws_events.Schedule.rate(core.Duration.minutes(5)) # Lambda set to run every 5 minutes
        
        event_lambda_target = aws_events_targets.LambdaFunction(handler=web_health_lambda) # Target (Lambda Function set for events)
        
        # Combining schedule and Target to run it periodically
        lambda_run_rule = aws_events.Rule(self,'web_health_lambda_rule',
        description='Periodic Lambda', 
        schedule=schedule_lambda, 
        targets=[event_lambda_target])
        
    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self, id,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6)
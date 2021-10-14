from aws_cdk import core as cdk
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_events, aws_events_targets

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class InfraStackMubashirWebHealth(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        web_health_lambda = self.create_lambda("Mubashir_WebHealth", "./lambda", "web.lambda_health")
        
        
        myRule = aws_events.Rule(
            self, "Checker",
            schedule=aws_events.Schedule.rate(cdk.Duration.minutes(5)),
            )
            
        myRule.add_target(aws_events_targets.LambdaFunction(web_health_lambda))
    
    
    def create_lambda(self, id, asset, handler):
        return lambda_.Function(self, id, 
            code=lambda_.Code.asset(asset),
            handler=handler,
            runtime=lambda_.Runtime.PYTHON_3_6)
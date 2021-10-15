
from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_events
from aws_cdk import aws_events_targets

class InfraStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        latency_lambda = self.create_lambda('AndromedaLambdaShazib','./lambda', 'latency_handler.handler')
    
        # Add a scheduler 
        self.create_periodic_lambda(self, "AndromedaShazibPeriodicLambda", 5, latency_lambda)

    def create_periodic_lambda(self, id, time_interval, lambda_function):
        lambda_schedule = aws_events.Schedule.rate(core.Duration.minutes(time_interval))
        lambda_event_target = aws_events_targets.LambdaFunction(handler=lambda_function)
        lambda_run_rule = aws_events.Rule(self, id, schedule = lambda_schedule, targets = [lambda_event_target])

    def create_lambda(self, id, asset, handler):
        return lambda_.Function(
            self, 
            id, 
            code = lambda_.Code.asset(asset), 
            handler = handler,
            runtime = lambda_.Runtime.PYTHON_3_6
            )

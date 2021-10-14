from aws_cdk import core as cdk
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_iam
from aws_cdk import aws_events
from aws_cdk import aws_events_targets

class InfraStackOsama(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        role = self.create_lambda_role()
        
        web_health_lambda = self.create_lambda('AndromedaLambda','./lambda','handler.lambda_handler',role)
    
        lambda_schedule = aws_events.Schedule.rate(core.Duration.minutes(5))
        event_lambda_target = aws_events_targets.LambdaFunction(handler = web_health_lambda)
        lambda_run_rule = aws_events.Rule(self,"web_health_lambda_rule",
        description = "Periodic_Lambda",schedule = lambda_schedule,targets = [event_lambda_target])
        
        
        
    
    def create_lambda_role(self):
        lambdaRole = aws_iam.Role(self,'lambdaRole',
        assumed_by = aws_iam.ServicePrincipal('lambda.amazonaws.com'),
        managed_policies = [
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole')])
        return lambdaRole
    def create_lambda(self,id,asset,handler,role):
        return lambda_.Function(self,id,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6,
        role = role)
    
    
    
    
    
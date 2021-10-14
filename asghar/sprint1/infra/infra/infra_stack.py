from aws_cdk import core as cdk
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_iam
from aws_cdk import aws_events as event_
from aws_cdk import aws_events_targets as event_target_
#from lambda_functions.lambda_services import web_health_checker

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

class InfraStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # The code that defines your stack goes here
        role  = self.lambda_role()
        lambda1_service = self.create_lambda('Andromeda_asghar', './infra/lambda_functions/', 'lambda_services.web_health_checker', role)
        ## Caling the aws_cdk.aws_events.Rule here that is defined below as a lambda_event. 
        lambda_event = self.create_event('AsgharLambdaEvent', event_target_.LambdaFunction(handler =lambda1_service))
    
    def lambda_role(self):
        LambdaRole = aws_iam.Role(self, "lambda_role",
        assumed_by = aws_iam.ServicePrincipal("lambda.amazonaws.com"),
        managed_policies= [
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
            )
        return LambdaRole
    
    def create_lambda(self, id, asset, handler, role):
        return lambda_.Function(self, id, 
        code = lambda_.Code.asset(asset),
        handler = handler,
        runtime = lambda_.Runtime.PYTHON_3_6,
        role = role
        )
        
    def create_event(self, id, target):
        return event_.Rule(self,id,
        schedule = event_.Schedule.rate(core.Duration.minutes(5)),
        targets   = [ target])
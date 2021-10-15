from aws_cdk import core as cdk
from aws_cdk import aws_lambda
from aws_cdk import aws_iam
from aws_cdk import aws_events 
from aws_cdk import aws_events_targets


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

class AsgharInfraStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # The code that defines your stack goes here
        role  = self.lambda_role()
        #The lambda construct that will run lambda function with given parameters below.
        lambda1_service = self.create_lambda('Andromeda_asghar', './infra/lambda_functions/', 'lambda_services.web_health_checker', role)
        ## Caling the aws_cdk.aws_events.Rule here that is defined below as a lambda_event. 
        lambda_event = self.create_event('AsgharLambdaEvent',5,lambda1_service) #handler = object of lambda function constructor.
    
    
    def lambda_role(self):
        LambdaRole = aws_iam.Role(self, "lambda_role",
        assumed_by = aws_iam.ServicePrincipal("lambda.amazonaws.com"),
        managed_policies= [
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
            )
        return LambdaRole
    
    def create_lambda(self, id, asset, handler, role):
        return aws_lambda.Function(self, id, 
        code = aws_lambda.Code.asset(asset),
        handler = handler,
        runtime = aws_lambda.Runtime.PYTHON_3_6,
        role = role
        )
        
    def create_event(self, id, time, target):
        return aws_events.Rule(self,id,
        schedule = aws_events.Schedule.rate(core.Duration.minutes(time)),#defining time duration of time minutes
        targets   = [ aws_events_targets.LambdaFunction(handler =target)]) #targets should be returned as a sequence here.
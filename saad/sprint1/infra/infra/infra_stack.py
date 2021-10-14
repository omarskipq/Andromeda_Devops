from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_events,aws_events_targets

class InfraStackSaad(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        """
        InfraStackSaad Construct where every resource to be used in my stack is set up.
        """
        #Calling my create_lambda function
        web_metric_lambda=self.create_lambda('saadWebMetricLambda','./lambda','web_metrics.lambda_handler')
        #Declaring AWS Schedule Event For AWS Lambda so that it can run periodically for 5 minutes
        lambda_schedule=aws_events.Schedule.rate(core.Duration.minutes(5))
        #Defining the lambda handler on which AWS Events Schedule would run 
        lambda_event_target=aws_events_targets.LambdaFunction(web_metric_lambda)
        #Defining an AWS Event Rule that links the schedule with the target and creates a CloudWatch EventRule
        lambda_run_rule=aws_events.Rule(self,'saadWebMetricSchedules',#id
        description='Monitoring Website Health Every 5 mnutes',
        schedule=lambda_schedule,
        targets=[lambda_event_target])

    def create_lambda(self,id,asset,handler):
        """
        Invokes aws_lambda class Function
        
        Args:
            id (str) : Contains a string which acts as an ID
            asset (str) : Contains name of a directory that contians my lambda handler function
            handler (str): Contains name of the python file and the lambda handler functions name separated by a '.'
            
        Returns:
            
        """
        return lambda_.Function(self,id,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6
        )

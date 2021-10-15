'''
This file defines Lambda handler function that acts as HelloWorld for Lambda function


Function     : lambda_handler(event, context)

Description  : A handler function that displays Hello along with your first and last name
                
Parameters   : event, context

               event- An event is a JSON-formatted document that contains data for a Lambda function to process. 
               The Lambda runtime converts the event to an object and passes it to your function code. 
               It is usually of the Python dict type. It can also be list, str, int, float, or the NoneType type.
               
               context- A context object is passed to your function by Lambda at runtime. 
               This object provides methods and properties that provide information about the invocation, function, 
               and runtime environment.
   
Return       : Returns a dictionary containing the key named message with value of  "Hello First_name Last_name"

'''


def lambda_handler(event, context):
    message="Hello {} {}!".format(event['first_name'], event['last_name'])
    return{
        'message':message
    }
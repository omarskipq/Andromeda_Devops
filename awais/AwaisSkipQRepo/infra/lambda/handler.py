def lambda_handler(event, context):
    message = "hello {} {}!".format(event["firstname"],event["lastname"])
    return {"message" : message }
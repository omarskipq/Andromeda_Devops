def lambda_handler(event, context):
    message = f"Hello {event.get('first_name', '')} {event.get('second_name', '')} !"

    return {
        'message': message
    }
     
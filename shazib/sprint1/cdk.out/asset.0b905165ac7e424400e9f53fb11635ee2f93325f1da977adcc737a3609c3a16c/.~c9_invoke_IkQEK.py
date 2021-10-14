import constants as CONSTANTS

def latency_lambda_handler(event, context):
    
    url = CONSTANTS.URL
    availability = get_availability(url)
    latency = get_latency(url)
    
    
    
    
    message = 'Latency: {} Availability: {}\n'.format('latency', 'availability')
    return {
        'message': message
    }

def get_availability(url: str):
    availability = 1
    
    return availability

def get_latency(url: str):
    latency = 0.5
    return latency
    
    

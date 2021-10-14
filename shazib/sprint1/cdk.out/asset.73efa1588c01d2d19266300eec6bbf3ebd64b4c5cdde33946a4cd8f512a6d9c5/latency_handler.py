import constants as CONSTANTS

def handler(event, context):
    print("inside latency lambda handler")
    url = CONSTANTS.URL
    return dict(
            {
                'latency': get_latency(url),
                'availability': get_availability(url)
            }
        )

def get_availability(url: str):
    availability = 1
    return availability

def get_latency(url: str):
    latency = 0.5
    return latency
    
    

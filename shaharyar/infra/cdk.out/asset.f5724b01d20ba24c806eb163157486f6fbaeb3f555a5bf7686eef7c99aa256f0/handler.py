# def lambda_handler(event,context):
    # message = 'Hello {} {}!'.format(event['first_name'],event['last_name'])
    # return {
    #     'message':message
    # }
from requests import get
import constants
def health_web(event,context):
    url = constants.URLs
    availability = get_availability(url)
    latency = get_latency(url)
    return {
        'Availability':availability,
        'Latency':latency
    }
    
def get_availability(url):
    response = get(url)
    if response == 200:
        availability =1
    else:
        availability=0    
    return availability

def get_latency(url):
    latency = get(url).elapsed.total_seconds()
    return latency

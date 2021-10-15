# def lambda_handler(event,context):
    # message = 'Hello {} {}!'.format(event['first_name'],event['last_name'])
    # return {
    #     'message':message
    # }
import urllib3
import constants
def health_web(event,context):
    url = constants.URLs
    availability = get_availability(url)
    # latency = get_latency(url)
    return {
        'Availability':availability,
        # 'Latency':latency
    }
    
def get_availability(url):
    availability = urllib3.get_availability(url)
    return availability

def get_latency(url):
    latency = urllib3.latency(url)
    return latency

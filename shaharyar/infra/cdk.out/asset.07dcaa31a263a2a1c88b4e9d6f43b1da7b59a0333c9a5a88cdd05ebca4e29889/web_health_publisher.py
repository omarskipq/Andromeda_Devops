# def lambda_handler(event,context):
#     message = 'Hello {} {}!'.format(event['first_name'],event['last_name'])
#     return {
#         'message':message
#     }
from aws_lambda import urllib3
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
    http = urllib3.PoolManager()
    resp = http('GET',url)
    # print(resp.status)
    # availability = 1
    return resp.status

def get_latency(url):
    http = urllib3.PoolManager()
    resp = http('GET',url)
    print(resp)
    latency = 0.3
    return latency

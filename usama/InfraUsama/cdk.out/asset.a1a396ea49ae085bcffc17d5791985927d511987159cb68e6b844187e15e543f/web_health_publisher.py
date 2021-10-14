import urllib.request
import json
import constants


def health_monitor(event, context):
    
    url = constants.URLS_TO_MONITOR
    
    # message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
    # return {
    #     'message':message
    # }
    
    availability = get_availability(url)
    # latency = get_latency(url)
    result = {'Availability': availability}
    return result
    
def get_availability(url):
    res = urllib.request.urlopen(urllib.request.Request(
        url='http://asdfast.beobit.net/api/',
        headers={'Accept': 'application/json'},
        method='GET'),
    timeout=5)
    return res
    
# def get_latency(url):
    
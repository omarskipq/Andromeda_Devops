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



def get_availability(web_url):
    res = urllib.request.urlopen(urllib.request.Request(
        url=web_url,
        headers={'Accept': 'application/json'},
        method='GET'),
    timeout=5)
    availability = res.status
    return availability
    
# def get_latency(url):
    
import datetime
import urllib3
import json
import constants


def health_monitor(event, context):
    
    url = constants.URLS_TO_MONITOR
    availability = get_availability(url)
    latency = get_latency(url)
    result = {'Availability': availability, 'Latency': "{}ms".format(latency)}
    return result


def get_availability(web_url):

    http = urllib3.PoolManager()
    res = http.request('GET', web_url)
    availability = res.status
    return 1 if availability==200 else 0
    
def get_latency(web_url):
    
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    response = http.request('GET', web_url)
    end = datetime.datetime.now()
    GET_time = end - start
    latency_in_ms = round(GET_time.microseconds * .000001, 6)
    return latency_in_ms
    
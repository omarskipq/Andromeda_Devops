import datetime
import urllib3
import urllib.request
import json
import constants


def health_monitor(event, context):
    
    url = constants.URLS_TO_MONITOR
    availability = get_availability(url)
    latency = get_latency(url)
    result = {'Availability': availability, 'Latency': "{}ms".format(latency)}
    return result


def get_availability(web_url):

    res = urllib.request.urlopen(urllib.request.Request(
        url=web_url,
        headers={'Accept': 'application/json'},
        method='GET'),
        timeout=5)
    availability = res.status
    return 1 if availability==200 else 0
    
def get_latency(web_url):
    
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    response = http.request('GET', web_url)
    end = datetime.datetime.now()
    delta = end - start
    latency_in_ms = round(delta.microseconds * .000001, 6)
    return latency_in_ms
    
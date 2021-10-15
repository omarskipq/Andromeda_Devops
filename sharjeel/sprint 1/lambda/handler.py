import datetime
import urllib3

import constants
def web_health(event, context):
    
    url = constants.URLS_TO_MONITOR
   
    dict_metrics = dict()
    dict_metrics['latency'] = get_latency(url)
    dict_metrics['availibility'] = get_avail(url)
    
    return dict_metrics
    
def get_latency(url):
    http = urllib3.PoolManager()
    # Start Timer
    start = datetime.datetime.now()
    response = http.request('GET', url)
    # End Timer
    end = datetime.datetime.now()
    delta = end - start

    return round(delta.microseconds * .000001, 6)
        
def get_avail(url):
    http = urllib3.PoolManager()
    request = http.request('GET', url)

    return 1 if request.status == 200 else 0
    
   
    

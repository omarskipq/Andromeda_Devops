import constants
import urllib3 
import time


def health_web(event, context):
    web_metric = dict()
    for url in constants.URLS_TO_MONITOR:
        web_metric[url] = get_availability_latency(url)
    
    return web_metric

    
def get_availability_latency(url):
    
    latency_availability= dict()  # Initializing an empty dictionary
    http = urllib3.PoolManager()
    start = time.time() 
    response = http.request("GET", url)
    end = time.time()
    
    availability = 1 if response.status == 200 else 0 
    latency = round((end - start),6)
    
    
    latency_availability['latency_in_secodes']= latency
    latency_availability['availablilty']= availability
    return latency_availability
                
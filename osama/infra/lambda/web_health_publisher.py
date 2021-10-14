

import constants
import urllib3

# import requests


def health_web(event, context):
    
    url = constants.URLS_TO_MONITOR
    latency_url = get_latency(url)
    availability_url = get_availability(url)
    
    dict_latency_availability = dict()
    dict_latency_availability["latency_in_seconds"] = latency_url
    dict_latency_availability["page_available"] = availability_url
    return dict_latency_availability 
     
   
def get_availability(url):
    availability = 1
    return availability
        
def get_latency(url):
    latency = 0.3
    return latency
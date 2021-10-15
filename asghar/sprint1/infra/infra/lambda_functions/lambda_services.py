'''
def print_fun(event, contex):
    message = f"Hello and Welcome {event.get('first_name','')} {event.get('last_name','')}"
    return message
'''
import urllib3
import time
from urls_data_file import urls_data as urls_


def web_availability():
    url = urls_['SkipQ']
    availability = (urllib3.PoolManager().request('GET', url)).status
    if availability>= 100 and availability<=199:
        availability = f"Website {urls_['SkipQ']} is giving us Informational response"
    elif availability>= 200 and availability<=299:
        availability = f"Website {urls_['SkipQ']} is giving us Successful response"
    elif availability>= 300 and availability<=399:
        availability = f"Website {urls_['SkipQ']} is giving us Redirects"
    elif availability>= 400 and availability<=499:
        availability = f"Website {urls_['SkipQ']} is giving us Client errors"
    elif availability>= 500 and availability<=599:
        availability = f"Website {urls_['SkipQ']} is giving us Server errors"
    
    #SLEF NOTE FOR LATER UPGRADATION
    '''
    Informational responses (100–199)
    Successful responses (200–299)
    Redirects (300–399)
    Client errors (400–499)
    Server errors (500–599)
    '''
    
    
    return availability

def web_latency():
    url = urls_['SkipQ']
    start_time = time.time()
    time_watch = urllib3.PoolManager().request('GET', url)
    latency = time.time()
    
    
    latency -= start_time
    latency =f"The Response time for ({urls_['SkipQ']}) is {latency} seconds" 
    return latency

def web_health_checker(event, contex):
    if event.get('availability','') == 'check':
        
        availability = web_availability()
    else:
        availability = 'Check availability by using check as a value in key'
    if event.get('latency', '') == 'check':
        latency =  web_latency()
    else:
        latency = 'Check latency by using check as a value in key'
    
    results = {
        'Website:': urls_['SkipQ'],
        'availability': availability,
        'latency': latency
    }
    
    
    return results



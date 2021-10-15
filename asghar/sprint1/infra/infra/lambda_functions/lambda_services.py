import urllib3
import time
from urls_data_file import urls_data 


def print_fun(event, contex):
    
    '''
    print_fun(): Function Defination
    This is simple lambda print function for checking how lambda function can be used to send out print message on clourls_data 

    '''

    message = f"Hello and Welcome {event.get('first_name','')} {event.get('last_name','')}"
    return message



def web_availability():
    '''
    web_availability (): function Defination
    
    This function will check the availability of website that is pointed by using dictionary urls_data[]
    urls_data[] is a dictionary that will contain urls data (that we need to check) and is located in url_data_file.py
        
    urllib3 is being used for genrating request and to check that status of request.
        
    The returned availability variable will contain string according to the request status we recieved.
        
    Following are request statuses.
        
    Informational responses (100–199)
    Successful responses (200–299)
    Redirects (300–399)
    Client errors (400–499)
    Server errors (500–599)
    
    '''
    
    url = urls_data['SkipQ']
    availability = (urllib3.PoolManager().request('GET', url)).status
    if      availability>= 100 and availability<=199:
            availability = f"Website {urls_data['SkipQ']} is giving us Informational response"
    
    elif    availability>= 200 and availability<=299:
            availability = f"Website {urls_data['SkipQ']} is giving us Successful response"
    
    elif    availability>= 300 and availability<=399:
            availability = f"Website {urls_data['SkipQ']} is giving us Redirects"
    
    elif    availability>= 400 and availability<=499:
            availability = f"Website {urls_data['SkipQ']} is giving us Client errors"
    
    elif    availability>= 500 and availability<=599:
            availability = f"Website {urls_data['SkipQ']} is giving us Server errors"
    
    return  availability


def web_latency():
    '''
    web_latency():  function Defination
    
    This function will check the availability of website that is pointed by using dictionary urls_data[]
    urls_data[] is a dictionary that will contain urls data (that we need to check) and is located in url_data_file.py
        
    first time function is used to capture the instantaneous time 
    Then urllib3 is being used for genrating request and to check that status of request.
    Then Latency is calculated by checking again the time taken by website to send back reqeust - initial time
        
    The returned latency variable will contain string containig website name and time in seconds.
    
    '''
    
    url = urls_data['SkipQ']
    start_time = time.time()
    _  = urllib3.PoolManager().request('GET', url)
    latency = time.time() - start_time
    latency = f"The Response time for ({urls_data['SkipQ']}) is {latency} seconds" 
    return latency


def web_health_checker(event, contex):

    '''
    web_health_checker(event, contex):  function Defination
    
    This is lambda function which will call web_latency and web_availability functions to check latency and
    availability of website and send it back to aws cloud that is being defined by aws CDK.
        
    The function will have a test case scenario where it will only check web_availability if user on lambda
    console have provided dictionary key "availability" as "check", otherwise user will get message
    to provide key.
        
    Similarl case is with web_latency check. 
        
    The function will return dictionary with website name, website availability and web_latency latency data.
    '''
    
    if event.get('availability','') == 'check':
        
        availability = web_availability()
    else:
        availability = 'Check availability by using check as a value in availability key'
    if event.get('latency', '') == 'check':
        latency =  web_latency()
    else:
        latency = 'Check latency by using check as a value in latency key'
    
    return  {   'Website:': urls_data['SkipQ'],
                'availability': availability,'latency': latency }
                
    
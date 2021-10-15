import constants
import urllib3 
import time

# Monitoring the health of all websites in constants.py
def health_web(event, context):
    """
    Creates an empty dictionary and then read the URLs to monitor the health from a constants.py
    Resutl is stored inside the dictionary by using get_availability_latency function.
    
    Args:
        event (dict,optional) : Contains the data for a lambda function to process
        context (object) : Passed by AWS Lambda at runtime. Contains methods and 
        properties that provide information about the invocation, function, and runtime environments
        
    Returns:
        dict: Contains website health metrics: availability, and latency 
    """
    
    web_metric = dict()
    for url in constants.URLS_TO_MONITOR:
        web_metric[url] = get_availability_latency(url)
    
    return web_metric

# Function to measure the availability and latency of website    
def get_availability_latency(url):
    """
    Measures the availability and latency of a public website
    Args:
        url (str) : A string containing a website's url
        
    Returns:
        dict: containing latency in seconds and availability as 1 or 0 
        depending on the response status
        
    """
    latency_availability= dict()  # Initializing an empty dictionary
    http = urllib3.PoolManager()
    start = time.time() 
    response = http.request("GET", url)
    end = time.time()
    
    availability = 1 if response.status == 200 else 0 
    latency = round((end - start),6)
    
    
    latency_availability['latency_in_secondes']= latency
    latency_availability['availablilty']= availability
    return latency_availability
                
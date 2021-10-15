import urllib3
from time import time
import web_constants

def lambda_handler(event,context):
    """
    Calls A function that reads URLs to monitor from a file
    
    Args:
        event (dict,optional) : Contains the data for a lambda function to process
        context (object) : Passed by AWS Lambda at runtime. Contains methods and 
        properties that provide information about the invocation,function, and runtime environments
        
    Returns:
        dict: Contains website health metrics: availability, and latency 
    """
    #Call read_url_FromConstants function and store a dict in message
    message=read_url_FromConstants()
    return message

def web_metrics(url):
    """
    Measures the availability and latency of a public website
    
    Args:
        url (str) : A string containing a website's url
        
    Returns:
        bool: Contains True if GET Request returns 200 otherwise False
        float: Contains a floating point number representing latency in seconds
        
    """
    availability=False 
    http=urllib3.PoolManager() #Automatically handles ConnectionPool instances for each host as needed
    start_time=time() #getting the start time
    r=http.request('GET',url) #generating a GET request to a url
    end_time=time() #Getting the end time
    duration=end_time-start_time #Subtracting start time from end time 
    
    
    ## Checking the status of http get request
    if r.status==200: 
        availability=True
    else:
        availability=False
    
    return availability,duration

def read_url_FromConstants():
    """
    Extracts URLs from web_constants.py and calls web_metrics
    
    Args:
    
    Returns:
        dict: Contains web health metrics as the value and website url as the key.
    """
    
    #Reading a list of urls from my web_constants.py file
    urls=web_constants.URLS
    #Declaring an empty dictionary
    web_dict={}
    #Running a loop over all the urls present in the list
    for url in urls:
        #Calling web_metrics function for every url
        x,y=web_metrics(url)
        #Storing the output in the web_dict dictionary
        web_dict[url]={web_constants.MEASURE_AVAILABILITY:x,
        web_constants.MEASURE_LATENCY:y}
    return web_dict
    


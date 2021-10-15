import requests
import constants

def health_web(event,context):
    
    url = constants.URLs
    availability = get_availability(url)
    latency = get_latency(url)
    # Returning availability and latency as dictionary
    return {
        'Availability':availability,
        'Latency':latency
    }
    
def get_availability(url):
    # Arguments
    # Input: url (Url of website to monitor)
    # Returns 1 if website is available, 0 if it is not
    if requests.get(url).status_code == 200: # Status code 200 means website loaded successfully hence available
        return 1
    else:
        return 0    

def get_latency(url):
    # Arguments
    # Input: url (Url of website to monitor)
    # Returns (Latency of website in seconds)
    return  requests.get(url).elapsed.total_seconds() #Latency in seconds

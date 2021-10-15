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
    response = requests.get(url)
    if response.status_code == 200: # Status code 200 means website loaded successfully hence available
        availability =1
    else:
        availability=0    
    return availability

def get_latency(url):
    latency = requests.get(url).elapsed.total_seconds() #Latency in seconds
    return latency

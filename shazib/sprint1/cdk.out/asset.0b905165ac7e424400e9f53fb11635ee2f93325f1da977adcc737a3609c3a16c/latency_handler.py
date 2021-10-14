import constants as CONSTANTS
import urllib.request
import time

def handler(event, context):
    print("inside latency lambda handler")
    url = CONSTANTS.URL
    return dict(
            {
                'latency': get_latency(url),
                'availability': get_availability(url)
            }
        )

def get_availability(url: str) -> int:
    return 1 if urllib.request.urlopen(url).getcode() == 200 else 0

def get_latency(url: str) -> float:

    # Send a request
    web_request = urllib.request.urlopen(url)
    # Start the timer
    start = time.time()
    # Read reponse
    page = web_request.read()
    # Stop timer
    end = time.time()
    # Close connection
    web_request.close()
    # Calculate latency
    latency = (end - start) * 1000 # Returning latency in ms

    return latency
    
    

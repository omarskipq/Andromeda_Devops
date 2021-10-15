import constants as CONSTANTS
import urllib.request
import time

def handler(event, context):
    """
    Returns a dict with latency and availability as keypairs with their corresponding values.
    
    """
    url = CONSTANTS.URL
    return dict(
            {
                'latency': get_latency(url),
                'availability': get_availability(url)
            }
        )

def get_availability(url: str) -> int:
    """
    Returns the availability status of the target site.

        Parameters:
                url (str): A string containing the url of the site.

        Returns:
                    (int): A interger, either 1 or 0 based on the conditions
    """
    return 1 if urllib.request.urlopen(url).getcode() == 200 else 0

def get_latency(url: str) -> float:
    """
    Returns the latency (in ms) of the target site.

        Parameters:
                url (str): A string containing the url.

        Returns:
                latency (float): Latency in ms
    """
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
    
    

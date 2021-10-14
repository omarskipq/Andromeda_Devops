import datetime
import urllib3
import constants
import logging
url=constants.URLS_TO_MONITER
def health_web(event,context):
    '''
    We create a PoolManager to generate a request. It handles all of the details of connection pooling and thread safety.
    '''
    http = urllib3.PoolManager()
    try:
            start = datetime.datetime.now()
            #With the request() method, we make a GET request to the specified URL.
            response = http.request('HEAD', url)
            server=response.headers['Server']
            end = datetime.datetime.now()
            delta = end - start
            elapsed_seconds = round(delta.microseconds * .000001, 6)
            if(response.status==200):
                assecible="Available"
            else:
                assecible="Not Aavailable"
                   
            return {
                    "Latency": elapsed_seconds,
                    "availability":assecible
                }
            
    except:
            logging.info("Failed to fetch service config rollout strategy " + \
                "from the metadata server: " + url);
            return None
   
        
            
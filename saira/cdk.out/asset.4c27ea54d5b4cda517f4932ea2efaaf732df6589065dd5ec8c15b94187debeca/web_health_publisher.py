import datetime
import urllib3
import constants
url = constants.URLS_TO_MONITER
def health_web(event,context):
    http = urllib3.PoolManager()

    start = datetime.datetime.now()
    response = http.request('GET', url)
    end = datetime.datetime.now()
    delta = end - start
    
    elapsed_seconds = round(delta.microseconds * .000001, 6)
    return{
        "Latency": elapsed_seconds,
        "availability":response.status_code
        
    }
   
     
            
        
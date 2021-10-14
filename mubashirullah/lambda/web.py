
import constants
import requests

def lambda_health(event, context) -> dict:
    """
    Finds latency and availability of url
    Returns in dictionary: dic_latency_availability
    """
    url = constants.URLS_TO_MONITOR
    dic_latency_availability = dict()
    
    dic_latency_availability['latency'] = get_latency(url)
    dic_latency_availability['availability'] = get_availability(url)
    
    return dic_latency_availability
    
    
def get_latency(url: str):
    response = requests.get(url)
    # Assert that there were no errors
    response.raise_for_status()
    return response.elapsed.total_seconds()
    
    
def get_availability(url: str):
    response = requests.head(url)
    return response.status_code
    
    


    
    

    
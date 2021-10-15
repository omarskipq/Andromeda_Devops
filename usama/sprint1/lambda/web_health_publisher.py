import datetime
import urllib3
import constants 


def health_monitor(event, context):
    """Read the lists of URL in constants.py, collect the availability and latency of each and return the results.
    """
    
    url_list = constants.URLS_TO_MONITOR
    result_list = []
    http = urllib3.PoolManager()
    
    for url in url_list:        # Iterating over lists of url
        availability = get_availability(http, url)
        latency = get_latency(http, url)
        result = {'URL': url, 'Availability': availability, 'Latency_in_sec': latency}
        result_list.append(result)
    
    return result_list

def get_availability(http, web_url):
    """Determine whether or not a public website is available. This function use http.request method to send a GET request.

    Args:
    http: A pckage inside PoolManager() able to send GET requests
    web_url: url of the website whose availability is required

    Returns:
    bool: Depending upon the response of GET request, this function will return a bool indicating availability of web_url
    """

    res = http.request('GET', web_url)
    availability = res.status
    
    return 1 if availability==200 else 0
    

def get_latency(http, web_url):
    """Determine latency / response time in seconds of a public website. It also use http request to send a GET  request.

    Args:
    http: A pckage inside PoolManager() able to send GET requests
    web_url: url of the website whose availability is required

    Returns:
    latency_in_seconds: Difference in start and end time of GET request.
    """
    
    start = datetime.datetime.now()
    response = http.request('GET', web_url)
    end = datetime.datetime.now()
    response_time = end - start
    latency_in_seconds = round(response_time.microseconds * 0.000001, 6) #Coverting datetimme object int micrsecoonds and then in seconds
    
    return latency_in_seconds
    
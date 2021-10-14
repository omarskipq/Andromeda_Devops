import urllib3
from time import time
import web_constants

def lambda_handler(event,context):
    message=read_url_FromFile('website_list.txt')
    return message

def web_metrics(url):
    availability=False
    http=urllib3.PoolManager()
    start_time=time()
    r=http.request('GET',url)
    end_time=time()
    duration=end_time-start_time
    if r.status==200:
        availability=True
    else:
        availability=False
    message={'Availability':availability,
            'Latency':duration}
    return message
    
def read_url_FromFile(filename):
    web_dict={}
    with open(filename,'r') as url_file:
        for url in url_file:
           url_final= url.strip('\n')
           web_dict[url_final]=web_metrics(url_final)
    return web_dict


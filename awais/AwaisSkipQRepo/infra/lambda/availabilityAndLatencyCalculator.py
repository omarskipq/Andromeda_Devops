import urllib3
import time

def uptime(event, context):
    event = {"url":"https://www.skipq.org/"}
    return checkAvailabilityAndLatency(event)

def checkAvailabilityAndLatency(event):
    url = event["url"]
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    if response.status == 200:
        availability = True
    else:
        availability = False
    startTime = time.time()
    openurl = http.request('GET', url)
    latency = time.time()-startTime
    return {"availability":availability, "latency":latency}
    
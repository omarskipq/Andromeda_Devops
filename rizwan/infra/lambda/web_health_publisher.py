import constants
import urllib3
import datetime

def health_web(event, context):
	url=constants.URLS_TO_MONITOR
	latency_url=get_latency(url)
	availability_url=get_availability(url)
	dict_latency_availability=dict()
	dict_latency_availability["latency_in_seconds"]=latency_url
	dict_latency_availability["page_available"]=availability_url
	return dict_latency_availability

def get_availability(url):
	http = urllib3.PoolManager()
	resp = http.request('GET', url)
	print(type(resp.status))
	if resp.status==200:
		return "Success"
	else:
		return "Failure"
		

def get_latency(url):
	http = urllib3.PoolManager()
	start = datetime.datetime.now()
	response = http.request('GET', url)
	end = datetime.datetime.now()
	delta = end - start
	elapsed_seconds = round(delta.microseconds * .000001, 6)
	return elapsed_seconds

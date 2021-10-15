# This file defines handler function for Lambda function
# Import files that need to be used in the project
import constants
# Import libraries that need to be used in the project
import urllib3
import datetime

'''
Function health_web(event, context)

Description  : A handler function that finds latency and page availability of a website
                
Parameters   : event, context

			   event- An event is a JSON-formatted document that contains data for a Lambda function to process. 
               The Lambda runtime converts the event to an object and passes it to your function code. 
               It is usually of the Python dict type. It can also be list, str, int, float, or the NoneType type.
               
               context- A context object is passed to your function by Lambda at runtime. 
               This object provides methods and properties that provide information about the invocation, function, 
               and runtime environment.
   
Return       : Returns a dictionary named dict_latency_availability that contains info about latency and page availability of a website.
   			   The dictionary key "page_available" has key value "Success" if website is available else the key
			   has value of "Failure"
			   The dictionary key "latency_in_seconds"  has key value of latency in seconds
'''

def health_web(event, context):
	# Get the url of website
	url=constants.URLS_TO_MONITOR
	http = urllib3.PoolManager()
	# Call function get_latency to get latency
	latency_url=get_latency(url, http)
	# Call function get_availability to get availability
	availability_url=get_availability(url, http)
	# Initialize a dictionary to store latency and availability results
	dict_latency_availability=dict()
	dict_latency_availability["latency_in_seconds"]=latency_url
	dict_latency_availability["page_available"]=availability_url
	return dict_latency_availability

'''
Function get _availability(url, http)

Description  : A function that finds whether a website is available by taking its URL as input
                
Parameters   : url-  The URL of website whose availability need to be checked
			   http- Allows for arbitrary requests while transparently keeping track of necessary connection pools for you.
   
Return       : Returns "Success" if website is available. If a website in unavailable it returns "Failure"
 
Example of Usage:
				url="https://www.skipq.org/"
				get_availability(url)		====> returns "Success" if available, else returns "Failure"

'''				
def get_availability(url, http):
	# request the website
	resp = http.request('GET', url)
	if resp.status==200:
		return "Success"
	else:
		return "Failure"
		

'''
Function get _latency(url, http)

Description  : A function that finds latency of a website.
                
Parameters   : url- The URL of website whose latency needs to be found.
			   http- Allows for arbitrary requests while transparently keeping track of necessary connection pools for you.
   
Return       : Returns time in seconds upto accuracy of three decimal numbers. Decimal numbers can be adjusted in second parameter
			   of round function according to your own needs.
 
Example of Usage:
				url="https://www.skipq.org/"
				get_latency(url)		====> returns latency value i.e. 0.034
				
'''

def get_latency(url, http):
	# Store current date and time in a variable named start before requesting website
	start = datetime.datetime.now()
	# request the website
	response = http.request('GET', url)
	# Store the current date and time in a variable named end after requesting the website
	end = datetime.datetime.now()
	# Time elapsed can be found by subtracting end date and time from start one and storing it in delta variable
	delta = end - start
	# Now convert that time to seconds
	elapsed_seconds = round(delta.microseconds * 1E-6, 3)
	return elapsed_seconds

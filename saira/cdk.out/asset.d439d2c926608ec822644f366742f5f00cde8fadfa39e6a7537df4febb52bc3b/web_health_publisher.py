# Import required packages 
import requests
import urllib
import constants
# Define URL  
url = constants.URLS_TO_MONITER
def health_web(event,context):
# API request url
    status_code = urllib.request.urlopen(url).getcode()
    website_is_up = status_code == 200
    return{
        "Availibiltiy":website_is_up
    }

# Import required packages 
import json
import requests
import pandas as pd
import urllib
import time
import constants
# Define URL  
url = constants.URLS_TO_MONITER
def lambda_handler(event,context):
# API request url
    status_code = urllib.request.urlopen(url).getcode()
    website_is_up = status_code == 200
    return{
        "Availibiltiy":website_is_up
    }

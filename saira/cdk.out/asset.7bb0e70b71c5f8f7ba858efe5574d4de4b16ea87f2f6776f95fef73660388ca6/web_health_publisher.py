# Import required packages 
import json
import requests
import pandas as pd
import urllib
import time
import constants
# Define URL  
url = constants.URLS_TO_MONITER
def health_web():
# API request url
    result = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
    .format(url)).read().decode('UTF-8')
    return result

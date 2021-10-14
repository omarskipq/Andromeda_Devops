from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import constants
url = Request(constants.URLS_TO_MONITER)
def health_web(event,context):
    try:
        response = urlopen(url)
    except HTTPError as e:
        availibility= 'The server couldn\'t fulfill the request.'

    else:
       
        availibility= response.read()
        
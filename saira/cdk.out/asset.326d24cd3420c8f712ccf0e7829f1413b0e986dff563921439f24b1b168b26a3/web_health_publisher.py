from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import constants
url = Request(constants.URLS_TO_MONITER)
def health_web():
  return {
      "url":"it worked"
  }
import requests
import pandas as pd

url = "https://thevirustracker.com/free-api"
params = {"countryTimeline": "DE"}
headers = {"accept": "text/html", "authority": "thevirustracker.com", "method": "get",
           "accept-encoding": "deflate, gzip", "content-type": "application-json"}
response = requests.get(url, params=params, headers=headers)
print(response.status_code)

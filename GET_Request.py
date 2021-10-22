"""
How do I send an HTTP GET request?

The GET request method is used to fetch data from the server. In this HTTP GET
request example, we are downloading the content of the ReqBin echo URL. The
Accept: */* request header tells the server that the client accepts all media
types. The Content-Type: text/html response header informs the client that the
server returned HTML for this HTTP GET request.
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo"

headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"


resp = requests.get(url, headers=headers)

print(resp.status_code)

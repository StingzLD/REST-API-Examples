"""
How do I use JSON pagination?

If the number of items returned in the server's JSON response is too large, the
server can limit the number of items in the JSON to a small subset ("page") of
the total available set to reduce the amount of data transferred from the
server and speed up the server response time. In this case, the server will
provide links to get the previous and next JSON pages from the dataset. In this
JSON pagination example, we limit the number of resources in JSON to 3 and
provide links to the previous and next JSON pages in the links JSON object.
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/get/json/page/2"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp.status_code)

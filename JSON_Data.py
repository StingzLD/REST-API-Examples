"""
JSON Data Example

JSON is a widely used lightweight format for storing and transmitting data.
JSON is often used to transfer data over the Internet between web and mobile
apps and a server. JSON is smaller and more convenient than XML. In this JSON
data example, we send sample JSON data to the ReqBin endpoint and walk through
the different JSON data types and JSON formats.
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
  "Id": 1,
  "Customer": "Jason Sweet",
  "OrderIds": [1, 2, 3, 4, 5],
  "Details": {
    "Age": 45
  }
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

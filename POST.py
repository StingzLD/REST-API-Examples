"""
How do I post JSON to a REST API endpoint?

To post JSON to a REST API endpoint, you must send an HTTP POST (PUT or PATCH)
request to the REST API server and provide JSON data in the body of the POST
message. You also need to specify the data type in the body of the POST message
using the Content-Type: application/json request header. In this REST API POST
example, we also send the Accept: application/json request header to tell the
REST API server that the API client expects JSON.
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
  "Id": 78912,
  "Customer": "Jason Sweet",
  "Quantity": 1,
  "Price": 18.00
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

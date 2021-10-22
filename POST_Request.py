"""
How do I send an HTTP POST request?

The POST method is used to send data to the server to create/update a resource
on the server. In this HTTP POST request example, the Content-Type request
header indicates the data type in the body of the POST message, and the
Content-Length request header indicates the size of the data in the body of the
POST request. The data is stored in the body of the POST message.
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/json"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer mt0dgHmLJMVQhvjpNXDyA83vA_PxH23Y"
headers["Content-Type"] = "application/json"

data = """
{
  "Id": 12345,
  "Customer": "John Smith",
  "Quantity": 1,
  "Price": 10.00
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

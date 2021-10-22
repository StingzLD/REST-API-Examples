"""
How do I post JSON to the server?

To post JSON data to the server, you need to use the HTTP POST method and set
the correct MIME type for the request body. The correct MIME type for JSON is
application/json. In this POST JSON example, the Content-Type: application/json
request header specifies the media type for the resource in the body, and the
Accept: application/json header tells the server that the client is expecting
JSON.
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

"""
How to post HTML Form Data to the Server?

To post HTML form data to the server in URL-encoded format, you need to make an
HTTP POST request to the server and provide the HTML form data in the body of
the POST message. You also need to specify the data type using the Content-Type:
application/x-www-form-urlencoded request header. HTML form data can also be
sent to the server using the HTTP GET method. In this case, HTML form data is
passed in the URL as key/value pairs separated by ampersands (&), and keys are
separated from values by equality (=).
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/form"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "key1=value1&key2=value2"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
